# 重命名的信息类（仅包含信息，不包含相关执行方法）
import os


class RenameInfo:
    """重命名的信息类"""

    def __init__(self, path):
        # 原始路径的信息
        if os.path.isdir(path):
            self.filetype = 'folder'
        else:
            self.filetype = 'file'
        self.original_path = os.path.normpath(path)
        self.parent_dirpath = os.path.dirname(path)
        self.original_filetitle = None
        self.original_file_extension = None
        self.original_filename = None
        # 根据重命名规则计算的新路径和文件名信息（未检查重复项）
        self.calc_filetitle = None
        self.calc_file_extension = None
        self.calc_filename = None
        self.calc_path = None
        # 执行重命名后的路径和文件名信息（重命名结果）
        self.rename_result = None
        self.is_dup = None
        self.filetitle_renamed = None
        self.file_extension_renamed = None
        self.filename_renamed = None
        self.path_renamed = None
        # 需要进行改名的文件路径和文件名信息（单独用于外部调用，在重命名后进行更新，使得原始路径信息不被修改）
        self.filetitle_need = None
        self.file_extension_need = None
        self.filename_need = None
        self.path_need = self.original_path
        # 撤销重命名时使用的文件路径和文件名信息
        self.is_dup_cancel = None
        self.filetitle_cancel = None
        self.file_extension_cancel = None
        self.filename_cancel = None
        self.path_cancel = self.original_path

    def update_old(self, filetitle, file_extension):
        self.original_filetitle = filetitle
        self.original_file_extension = file_extension
        self.original_filename = filetitle + file_extension

        self.filetitle_need = self.original_filetitle
        self.file_extension_need = self.original_file_extension
        self.filename_need = self.original_filename

    def update_new(self, filetitle, file_extension):
        self.calc_filetitle = filetitle
        self.calc_file_extension = file_extension
        self.calc_filename = filetitle + file_extension
        self.calc_path = os.path.normpath(os.path.join(self.parent_dirpath, self.calc_filename))

    def update_rename_no_dup(self):
        """更新重命名信息（无重复文件名的情况）"""
        self.is_dup = False
        self.filetitle_renamed = self.calc_filetitle
        self.file_extension_renamed = self.calc_file_extension
        self.filename_renamed = self.calc_filename
        self.path_renamed = self.calc_path

    def update_rename(self, filetitle):
        """更新重命名信息（存在重复文件名的情况）"""
        self.is_dup = True
        self.filetitle_renamed = filetitle
        self.file_extension_renamed = self.calc_file_extension
        self.filename_renamed = filetitle + self.file_extension_renamed
        self.path_renamed = os.path.normpath(os.path.join(self.parent_dirpath, self.filename_renamed))

    def update_cancel_rename_no_dup(self):
        """更新撤销重命名信息（无重复文件名的情况）"""
        self.is_dup_cancel = False
        self.filetitle_cancel = self.original_filetitle
        self.file_extension_cancel = self.original_file_extension
        self.filename_cancel = self.original_filename
        self.path_cancel = self.original_path

    def update_cancel_rename(self, filetitle):
        """更新撤销重命名信息（存在重复文件名的情况）"""
        self.is_dup = True
        self.filetitle_cancel = filetitle
        self.file_extension_cancel = self.original_file_extension
        self.filename_cancel = filetitle + self.file_extension_cancel
        self.path_cancel = os.path.normpath(os.path.join(self.parent_dirpath, self.filename_cancel))

    def set_result_renamed(self):
        """设置重命名结果"""
        self.rename_result = 'renamed'

        self.filetitle_need = self.filetitle_renamed
        self.file_extension_need = self.file_extension_renamed
        self.filename_need = self.filename_renamed
        self.path_need = self.path_renamed

    def set_result_unknown_error(self):
        """设置重命名结果"""
        self.rename_result = 'unknown_error'

    def set_result_skipped(self):
        """设置重命名结果"""
        self.rename_result = 'skipped'

    def set_result_not_exist(self):
        """设置重命名结果"""
        self.rename_result = 'not_exist'

    def set_result_occupied(self):
        """设置重命名结果"""
        self.rename_result = 'occupied'

    def set_result_cancelled(self):
        """设置重命名结果"""
        self.rename_result = 'cancelled'

        # 原始文件信息不做修改
        # self.original_path = self.path_cancel
        # self.original_filetitle = self.filetitle_cancel
        # self.original_file_extension = self.file_extension_cancel
        # self.original_filename = self.filename_cancel

        self.filetitle_need = self.filetitle_cancel
        self.file_extension_need = self.file_extension_cancel
        self.filename_need = self.filename_cancel
        self.path_need = self.path_cancel
