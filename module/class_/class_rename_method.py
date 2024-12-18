# 具体的重命名方法类，包含具体执行的内容
import os

from module import function_normal


class MethodNormal:
    """重命名方法类-一般方法，增删查改"""

    class _Model:
        def __init__(self, index=None, char=None, new_char=None, count=None):
            self.index = index
            self.char = char
            self.new_char = new_char
            self.count = count

        def rename_method(self, filetitle: str):
            """执行该类的重命名方法
            :return: 适用规则后的新文本"""
            pass

    class Insert(_Model):
        """插入"""

        def __init__(self, index, char):
            super().__init__(index=index, char=char)

        def rename_method(self, filetitle: str):
            new_filetitle = filetitle[0:self.index] + self.char + filetitle[self.index:]
            return new_filetitle

    class InsertBack(Insert):
        """插入（反向）"""

    class DeleteIndex(_Model):
        """删除"""

        def __init__(self, index, count):
            super().__init__(index=index, count=count)

        def rename_method(self, filetitle: str):
            # index为第n个字符开始，将其设置为0和1为同一个含义
            if self.index == 0:
                index = 0
                new_filetitle = filetitle[index + self.count:]
            else:
                if self.index > 0:
                    index = self.index - 1
                else:
                    if abs(self.index) <= len(filetitle):
                        index = len(filetitle) + self.index
                    else:
                        index = 0
                new_filetitle = filetitle[0:index] + filetitle[index + self.count:]

            return new_filetitle

    class DeleteIndexBack(DeleteIndex):
        """删除（反向）"""

    class Replace(_Model):
        """替换"""

        def __init__(self, char, new_char):
            super().__init__(char=char, new_char=new_char)

        def rename_method(self, filetitle: str):
            new_filetitle = filetitle.replace(self.char, self.new_char)
            return new_filetitle


class MethodConvert:
    """重命名方法类-文件名转换"""

    class _Model:
        def __init__(self):
            pass

        def rename_method(self, filetitle: str):
            """执行该类的重命名方法
            :return: 适用规则后的新文本"""
            pass

    class ConvertToLowercase(_Model):
        """转为小写字母"""

        def rename_method(self, filetitle: str):
            new_filetitle = filetitle.lower()
            return new_filetitle

    class ConvertToCapital(_Model):
        """转为大写字母"""

        def rename_method(self, filetitle: str):
            new_filetitle = filetitle.upper()
            return new_filetitle

    class ConvertToChs(_Model):
        """转为简体中文"""

        def rename_method(self, filetitle: str):
            new_filetitle = function_normal.to_chs(filetitle)
            return new_filetitle

    class ConvertToCht(_Model):
        """转为繁体中文"""

        def rename_method(self, filetitle: str):
            new_filetitle = function_normal.to_cht(filetitle)
            return new_filetitle

    class ConvertToHalfWidth(_Model):
        """转为半角字符"""

        def rename_method(self, filetitle: str):
            new_filetitle = function_normal.to_half_width(filetitle)
            return new_filetitle

    class ConvertToFullWidth(_Model):
        """转为全角字符"""

        def rename_method(self, filetitle: str):
            new_filetitle = function_normal.to_full_width(filetitle)
            return new_filetitle

    class ClearExcessSpaces(_Model):
        """清除多余空格"""

        def rename_method(self, filetitle: str):
            while True:
                if filetitle[0] == ' ' or filetitle[-1] == ' ':
                    filetitle = filetitle.strip(' ')
                elif '  ' in filetitle:
                    filetitle = filetitle.replace('  ', ' ')
                else:
                    break

            return filetitle


class MethodFileExtension:
    """重命名方法类-处理文件扩展名（仅传入后缀）"""

    class _Model:
        def __init__(self):
            pass

        def rename_method(self, file_extension: str):
            """执行该类的重命名方法
            :return: 适用规则后的新文本"""
            pass

    class ChangeTo(_Model):
        """改为指定扩展名"""

        def __init__(self, file_extension):
            super().__init__()
            if file_extension and file_extension[0] != '.':
                self.file_extension = '.' + file_extension
            else:
                self.file_extension = file_extension

        def rename_method(self, file_extension: str):
            return self.file_extension

    class ConvertToLowercase(_Model):
        """转为小写字母"""

        def rename_method(self, file_extension: str):
            new_file_extension = file_extension.lower()
            return new_file_extension

    class ConvertToCapital(_Model):
        """转为大写字母"""

        def rename_method(self, file_extension: str):
            new_file_extension = file_extension.upper()
            return new_file_extension

    class ChangeToRealType(_Model):
        """改为真实文件类型"""

        def rename_method(self, filepath: str):
            # 注意，该函数需要传入原始路径，原调用方法传入的是后缀名，需要单独处理传入的参数
            if not os.path.exists(filepath) or not os.path.isfile(filepath):
                return ''

            new_file_extension = function_normal.guess_filetype(filepath)
            if new_file_extension:
                return '.' + new_file_extension  # filetype库返回的后缀名不包含.，需要手工添加
            else:
                return ''
