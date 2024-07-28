# 汇总的重命名规则类
# 重命名各个模块优先关系：替换>删除>添加>标准化>模版>文件扩展名
import os.path
from typing import Union

from module import function_class
from module.class_.class_rename_info import RenameInfo
from module.class_.class_rename_type import TypePattern, TypeConvert, TypeFileExtension, TypeNormal


class RenameRule:
    """汇总的重命名规则类"""
    _instance = None
    _is_init = False

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self):
        if not self._is_init:
            super().__init__()
            self._is_init = True

            self._rule_pattern_dict = dict()  # 模板类
            self._rule_filename_dict = dict()  # 文件名类
            self._rule_file_extension_dict = dict()  # 文件扩展名类
            self._set_default_class()  # 设置初始键值对

    def update(self, rename_class):
        """添加"""
        class_ = type(rename_class)
        if class_ in self._rule_pattern_dict:
            self._rule_pattern_dict[class_] = rename_class
        elif class_ in self._rule_filename_dict:
            self._rule_filename_dict[class_] = rename_class
        elif class_ in self._rule_file_extension_dict:
            self._rule_file_extension_dict[class_] = rename_class

    def calc_new_name(self, path: Union[str, RenameInfo], index) -> RenameInfo:
        """计算新的文件名"""
        if isinstance(path, RenameInfo):
            path_need = path.path_need
        else:
            path_need = path

        if os.path.isdir(path_need):
            parent_dirpath, filetitle = os.path.split(path_need)
            file_extension = ''
        else:
            _temp, file_extension = os.path.splitext(path_need)
            parent_dirpath, filetitle = os.path.split(_temp)

        # 重命名各个模块优先关系：替换>删除>添加>标准化>模版>文件扩展名
        # 处理文件名 替换>删除>添加>标准化
        new_filetitle = filetitle
        for rule_type in self._rule_filename_dict.values():
            if rule_type and rule_type.is_enable:
                rule = rule_type.rule
                new_filetitle = rule.rename_method(new_filetitle)

        # 套用模板
        for rule_type in self._rule_pattern_dict.values():
            if rule_type and rule_type.is_enable:
                new_filetitle = rule_type.rename_method(new_filetitle, path_need, index)  # 单独适用模板重命名模块

        # 处理文件扩展名
        new_file_extension = file_extension
        if os.path.isfile(path_need):
            for rule_type in self._rule_file_extension_dict.values():
                if rule_type and rule_type.is_enable:
                    rule = rule_type.rule
                    guess_filetype = rule.rename_method(new_file_extension)
                    if guess_filetype:
                        new_file_extension = guess_filetype

        # 返回信息类
        if isinstance(path, RenameInfo):
            info = path
            info.update_new(new_filetitle, new_file_extension)
        else:
            info = RenameInfo(path)
            info.update_old(filetitle, file_extension)
            info.update_new(new_filetitle, new_file_extension)
        return info

    def _set_default_class(self):
        """设置初始类"""
        # 添加增删查改类，替换>删除>添加
        self._rule_filename_dict[TypeNormal.Replace] = None
        self._rule_filename_dict[TypeNormal.DeleteIndex] = None
        self._rule_filename_dict[TypeNormal.DeleteChar] = None
        self._rule_filename_dict[TypeNormal.Insert] = None
        self._rule_filename_dict[TypeNormal.AddPrefix] = None
        self._rule_filename_dict[TypeNormal.AddSuffix] = None

        # 添加文件名转换类
        child_class = function_class.get_subclasses(TypeConvert._Model)
        for class_ in child_class:
            self._rule_filename_dict[class_] = None

        # 添加模版类
        self._rule_pattern_dict[TypePattern] = None

        # 添加文件扩展名类
        child_class = function_class.get_subclasses(TypeFileExtension._Model)
        for class_ in child_class:
            self._rule_file_extension_dict[class_] = None
