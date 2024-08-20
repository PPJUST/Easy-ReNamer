# 具体的重命名类型类，用于连接主程序和具体方法
import os
import random
import string

from module import function_normal
from module.class_.class_rename_method import MethodNormal, MethodFileExtension, MethodConvert

import re


class TypePattern:
    """重命名类型类-通用模板"""

    def __init__(self, is_enable=False, pattern=None):
        self.is_enable = is_enable
        self.pattern = pattern
        self.pattern_preview = None
        # 数字编号
        self.digit_start = None
        self.digit_step = None
        self.digit_length = None
        self.is_enable_auto_fill_digit_length = None
        # 随机字母
        self.is_enable_random_digit = None
        self.is_enable_random_lowercase = None
        self.is_enable_random_capital = None
        self.is_enable_random_punctuation = None
        self.random_length = None

    def update_digit(self, digit_start, digit_step, digit_length, auto_fill):
        """更新数字编号规则"""
        self.digit_start = digit_start
        self.digit_step = digit_step
        self.digit_length = digit_length
        self.is_enable_auto_fill_digit_length = auto_fill
        self._calc_preview()

    def update_char(self, random_digit, random_lowercase, random_capital, random_punctuation, random_length):
        """更新随机字符规则"""
        self.is_enable_random_digit = random_digit
        self.is_enable_random_lowercase = random_lowercase
        self.is_enable_random_capital = random_capital
        self.is_enable_random_punctuation = random_punctuation
        self.random_length = random_length
        self._calc_preview()

    def get_preview(self):
        return self.pattern_preview

    def _calc_preview(self):
        """计算模板的预览文本"""
        """
        * 原文件名
        ##/" 数字编号
        ? 随机字符
        / 父目录名
        """
        if self.pattern:
            self.pattern_preview = self.pattern.replace('*', '<原文件名>')
            self.pattern_preview = re.sub(r'(?<!#)###(?!#)', '#"', self.pattern_preview)  # 单独处理###的情况（用于显示#1）
            self.pattern_preview = self.pattern_preview.replace('##', '<数字编号>')
            self.pattern_preview = self.pattern_preview.replace('"', '<数字编号>')
            self.pattern_preview = self.pattern_preview.replace('?', '<随机字符>')
            self.pattern_preview = self.pattern_preview.replace('/', '<父目录名>')

    def get_current_digit(self, index):
        """生成当前数字编号"""
        current_digit = str(self.digit_start + index * self.digit_step)
        if self.is_enable_auto_fill_digit_length:
            current_digit = current_digit.zfill(self.digit_length)

        return current_digit

    def get_current_random_character(self):
        """生成随机字符序列"""
        random_characters = ''
        if self.is_enable_random_digit:
            random_characters += string.digits
        if self.is_enable_random_lowercase:
            random_characters += string.ascii_lowercase
        if self.is_enable_random_capital:
            random_characters += string.ascii_uppercase
        if self.is_enable_random_punctuation:
            punctuation = string.punctuation
            punctuation = function_normal.check_filename_feasible(punctuation, replace=True)  # 替换不能作为windows文件名的符号
            random_characters += punctuation

        if random_characters:
            random_str = ''.join(random.choice(random_characters) for _ in range(self.random_length))
        else:
            random_str = ''
        return random_str

    @staticmethod
    def get_parent_dirname(path):
        """获取父目录名"""
        return os.path.basename(os.path.dirname(path))

    def rename_method(self, filetitle: str, path: str, index: int):
        new_filetitle = filetitle
        if self.pattern:
            new_filetitle = self.pattern.replace('*', filetitle)  # 替换原文件名
            new_filetitle = re.sub(r'(?<!#)###(?!#)', '#"', new_filetitle)  # 单独处理###的情况（用于显示#1）
            new_filetitle = new_filetitle.replace('##', self.get_current_digit(index))  # 替换数字编号
            new_filetitle = new_filetitle.replace('"', self.get_current_digit(index))  # 替换数字编号
            new_filetitle = new_filetitle.replace('?', self.get_current_random_character())  # 替换随机字符序列
            new_filetitle = new_filetitle.replace('/', self.get_parent_dirname(path))  # 替换父目录名

        return new_filetitle


class TypeNormal:
    """重命名类型类-一般方法，增删查改"""

    class _Model:
        def __init__(self, is_enable=False):
            self.is_enable = is_enable

    class Replace(_Model):
        """替换字符"""

        def __init__(self, is_enable, char, new_char):
            super().__init__(is_enable)
            self.rule = MethodNormal.Replace(char, new_char)

    class AddPrefix(_Model):
        """添加前缀"""

        def __init__(self, is_enable, char):
            super().__init__(is_enable)
            self.rule = MethodNormal.Insert(0, char)

    class AddSuffix(_Model):
        """添加后缀"""

        def __init__(self, is_enable, char):
            super().__init__(is_enable)
            self.rule = MethodNormal.Insert(999, char)

    class Insert(_Model):
        """插入字符"""

        def __init__(self, is_enable, index, char):
            super().__init__(is_enable)
            self.rule = MethodNormal.Insert(index, char)

    class DeleteChar(_Model):
        """删除字符"""

        def __init__(self, is_enable, delete_char):
            super().__init__(is_enable)
            self.rule = MethodNormal.Replace(delete_char, '')

    class DeleteIndex(_Model):
        """删除N个字符"""

        def __init__(self, is_enable, start_index, delete_count):
            super().__init__(is_enable)
            self.rule = MethodNormal.DeleteIndex(start_index, delete_count)

    class DeleteIndexAfter(_Model):
        """删除N个字符后的所有字符"""

        def __init__(self, is_enable, index):
            super().__init__(is_enable)
            self.rule = MethodNormal.DeleteIndex(index + 1, 999)  # 该类型为n个字符后，所以需要+1.删除字符个数为999即可


class TypeConvert:
    """重命名类型类-文件名转换"""

    class _Model:
        def __init__(self, is_enable=False):
            self.is_enable = is_enable

    class ConvertLetter(_Model):
        """字母转换小写/大写"""

        def __init__(self, is_enable, type_):
            super().__init__(is_enable)
            if type_ == '小写':
                self.rule = MethodConvert.ConvertToLowercase()
            elif type_ == '大写':
                self.rule = MethodConvert.ConvertToCapital()

    class ConvertChinese(_Model):
        """中文转转换简体/繁体"""

        def __init__(self, is_enable, type_):
            super().__init__(is_enable)
            if type_ == '简体':
                self.rule = MethodConvert.ConvertToChs()
            elif type_ == '繁体':
                self.rule = MethodConvert.ConvertToCht()

    class ConvertCharacter(_Model):
        """字符转换半角/全角"""

        def __init__(self, is_enable, type_):
            super().__init__(is_enable)
            if type_ == '半角':
                self.rule = MethodConvert.ConvertToHalfWidth()
            elif type_ == '全角':
                self.rule = MethodConvert.ConvertToFullWidth()

    class ClearExcessSpaces(_Model):
        """清除多余空格"""

        def __init__(self, is_enable):
            super().__init__(is_enable)
            self.rule = MethodConvert.ClearExcessSpaces()


class TypeFileExtension:
    """重命名类型类-处理文件扩展名"""

    class _Model:
        def __init__(self, is_enable=False):
            self.is_enable = is_enable

    class ChangeTo(_Model):
        """改为指定扩展名"""

        def __init__(self, is_enable, file_extension):
            super().__init__(is_enable)
            self.rule = MethodFileExtension.ChangeTo(file_extension)

    class ConvertToLowercase(_Model):
        """转为小写字母"""

        def __init__(self, is_enable):
            super().__init__(is_enable)
            self.rule = MethodFileExtension.ConvertToLowercase()

    class ConvertToCapital(_Model):
        """转为大写字母"""

        def __init__(self, is_enable):
            super().__init__(is_enable)
            self.rule = MethodFileExtension.ConvertToCapital()

    class ChangeToRealType(_Model):
        """改为真实文件类型"""

        def __init__(self, is_enable):
            super().__init__(is_enable)
            self.rule = MethodFileExtension.ChangeToRealType()
