import base64
import inspect
import os
import time
from typing import Union

import filetype
import unicodedata
from opencc import OpenCC

from module import WindowsSorted
from module.class_.class_rename_info import RenameInfo
from res.icon import *


def print_function_info(mode: str = 'current'):
    """
    打印当前/上一个执行的函数信息
    :param mode: str类型，'current' 或 'last'
    """
    # pass

    if mode == 'current':
        print(time.strftime('%H:%M:%S ', time.localtime()),
              inspect.getframeinfo(inspect.currentframe().f_back).function)
    elif mode == 'last':
        print(time.strftime('%H:%M:%S ', time.localtime()),
              inspect.getframeinfo(inspect.currentframe().f_back.f_back).function)


def to_half_width(text):
    """将传入字符串转换为半角字符"""
    # 先将字符串进行Unicode规范化为NFKC格式（兼容性组合用序列）
    normalized_string = unicodedata.normalize('NFKC', text)

    # 对于ASCII范围内的全角字符，将其替换为对应的半角字符
    half_width_string = []
    for char in normalized_string:
        code_point = ord(char)
        if 0xFF01 <= code_point <= 0xFF5E:
            half_width_string.append(chr(code_point - 0xFEE0))
        else:
            half_width_string.append(char)

    return ''.join(half_width_string)


def to_full_width(text):
    """将传入字符串转换为全角字符"""
    # 将字符串进行Unicode规范化为NFKC格式（兼容性组合用序列）
    normalized_string = unicodedata.normalize('NFKC', text)

    # 对于ASCII范围内的字符，将其替换为对应的全角字符
    full_width_string = []
    for char in normalized_string:
        code_point = ord(char)
        if 0x0020 <= code_point <= 0x007E:
            full_width_string.append(chr(code_point + 0xFF00 - 0x0020))
        else:
            full_width_string.append(char)

    return ''.join(full_width_string)


def half_to_full_width(input_str):
    full_width_str = []
    for char in input_str:
        code = ord(char)
        # Convert only if the character is within the ASCII range of half-width characters
        if 0x0021 <= code <= 0x007e:
            full_width_str.append(chr(code + 0xfee0))
        else:
            full_width_str.append(char)
    return ''.join(full_width_str)


def to_chs(text):
    """将字符串中的中文转换为简体中文"""
    cc = OpenCC('t2s')
    text_converted = cc.convert(text)
    return text_converted


def to_cht(text):
    """将字符串中的中文转换为繁体中文"""
    cc = OpenCC('s2t')
    text_converted = cc.convert(text)
    return text_converted


def guess_filetype(path):
    """判断文件类型"""
    kind = filetype.guess(path)
    if kind is None:
        return False

    type_ = kind.extension
    if type_:
        return type_
    else:
        return False


def check_filename_feasible(filename: str, replace: bool = False, replace_word: str = '') -> Union[str, bool]:
    """检查一个文件名是否符合Windows文件命名规范
    :param filename: str，仅文件名（不含路径）
    :param replace: bool，是否替换非法字符
    :param replace_word: 替换不合规字符的字符"""
    # 官方文档：文件和文件夹不能命名为“.”或“..”，也不能包含以下任何字符: \ / : * ? " < > |
    except_word = ['\\', '/', ':', '*', '?', '"', '<', '>', '|']
    if not replace:  # 不替换时，仅检查
        # 检查.
        if filename[0] == '.':
            return False

        # 检查其余符号
        for key in except_word:
            if key in filename:
                return False
        return True

    else:
        for word in except_word:  # 替换符号
            filename = filename.replace(word, replace_word)
        while filename[0] == '.':  # 替换.
            filename = replace_word + filename[1:]

        return filename.strip()


def sort_paths_by_filename(paths: list, order):
    """根据文件名排序路径"""
    f_dict = dict()
    for index, path in enumerate(paths):
        filename = os.path.basename(path)
        filename_index = filename + f'_____{index}'
        f_dict[filename_index] = path

    filenames_sorted = WindowsSorted.sort_list(list(f_dict.keys()), order)
    paths_sorted = [f_dict[i] for i in filenames_sorted]
    return paths_sorted


def calc_final_path(rename_info_class: RenameInfo) -> RenameInfo:
    """计算最终重命名的文件名（无重复文件名）"""
    # 首先判断是否需要重命名（考虑大小写英文）
    old_path = rename_info_class.path_need
    calc_path = rename_info_class.calc_path
    if old_path.lower() == calc_path.lower():
        rename_info_class.update_rename_no_dup()
        return rename_info_class

    # 然后判断同级是否有重复文件名（考虑大小写英文）
    parent_dirpath = rename_info_class.parent_dirpath
    listdir = [i.lower() for i in os.listdir(parent_dirpath)]
    calc_filename = rename_info_class.calc_filename
    if calc_filename.lower() not in listdir:  # 文件夹内无重复文件名
        rename_info_class.update_rename_no_dup()
        return rename_info_class
    else:  # 文件夹内有重复文件名，则需要添加后缀
        index = 2
        calc_filetitle = rename_info_class.calc_filetitle
        calc_file_extension = rename_info_class.calc_file_extension
        no_dup_filetitle = calc_filetitle + f' ({index})'
        no_dup_filename = no_dup_filetitle + calc_file_extension
        while True:
            if no_dup_filename.lower() not in listdir:
                break
            else:
                index += 1
                no_dup_filetitle = calc_filetitle + f' ({index})'
                no_dup_filename = no_dup_filetitle + calc_file_extension
        rename_info_class.update_rename(no_dup_filetitle)
        return rename_info_class


def calc_cancelled_path(rename_info_class: RenameInfo) -> RenameInfo:
    """计算撤销重命名时的原始文件名（无重复文件名）"""
    # 首先判断是否需要重命名（考虑大小写英文）
    old_path = rename_info_class.path_need
    original_path = rename_info_class.original_path
    if old_path.lower() == original_path.lower():
        rename_info_class.update_cancel_rename_no_dup()
        return rename_info_class

    # 然后判断同级是否有重复文件名（考虑大小写英文）
    parent_dirpath = rename_info_class.parent_dirpath
    listdir = [i.lower() for i in os.listdir(parent_dirpath)]
    original_filename = rename_info_class.original_filename
    if original_filename.lower() not in listdir:  # 文件夹内无重复文件名
        rename_info_class.update_cancel_rename_no_dup()
        return rename_info_class
    else:  # 文件夹内有重复文件名，则需要添加后缀
        index = 2
        original_filetitle = rename_info_class.original_filetitle
        original_file_extension = rename_info_class.original_file_extension
        no_dup_filetitle = original_filetitle + f' ({index})'
        no_dup_filename = no_dup_filetitle + original_file_extension
        while True:
            if no_dup_filename.lower() not in listdir:
                break
            else:
                index += 1
                no_dup_filetitle = original_filetitle + f' ({index})'
                no_dup_filename = no_dup_filetitle + original_file_extension
        rename_info_class.update_cancel_rename(no_dup_filetitle)
        return rename_info_class


def get_icon_result(result: str):
    """获取结果对应的图标"""
    if result == 'renamed':
        return base64.b64decode(right_base64)
    elif result == 'unknown_error':
        return base64.b64decode(error_base64)
    elif result == 'skipped':
        return base64.b64decode(skip_base64)
    elif result == 'not_exist':
        return base64.b64decode(not_exist_base64)
    elif result == 'occupied':
        return base64.b64decode(occupied_base64)
    elif result == 'cancelled':
        return base64.b64decode(cancelled_base64)
