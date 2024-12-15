import base64

from PySide6.QtGui import QPixmap, QIcon
from PySide6.QtWidgets import QMainWindow

from module.class_.class_rename_rule import RenameRule
from res.icon import app_base64
from ui.src.ui_main import Ui_MainWindow
from ui.widget_delete import WidgetDelete
from ui.widget_exec import WidgetExec
from ui.widget_file_extension import WidgetFileExtension
from ui.widget_file_list import WidgetFileList
from ui.widget_filename_pattern import WidgetFilenamePattern
from ui.widget_filename_standard import WidgetFilenameStandard
from ui.widget_insert import WidgetInsert
from ui.widget_replace import WidgetReplace


class MainWindow(QMainWindow):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # 设置图标
        pixmap = QPixmap()
        pixmap.loadFromData(base64.b64decode(app_base64))
        self.setWindowIcon(QIcon(pixmap))

        self.class_collect = RenameRule()

        # 添加控件组1
        # 模板控件
        self.widget_filename_pattern = WidgetFilenamePattern()
        self.ui.tab_pattern.layout().addWidget(self.widget_filename_pattern)
        self.widget_filename_pattern.signal_pattern.connect(self.collect_rename_rule)
        # 标准文件名控件
        self.widget_filename_standard = WidgetFilenameStandard()
        self.widget_filename_pattern.ui.verticalLayout_standard.addWidget(self.widget_filename_standard)
        self.widget_filename_standard.signal_standard_letter.connect(self.collect_rename_rule)
        self.widget_filename_standard.signal_standard_chinese.connect(self.collect_rename_rule)
        self.widget_filename_standard.signal_standard_character.connect(self.collect_rename_rule)
        self.widget_filename_standard.signal_excess_spaces.connect(self.collect_rename_rule)
        # 后缀控件
        self.widget_file_extension = WidgetFileExtension()
        self.widget_filename_pattern.ui.verticalLayout_file_extension.addWidget(self.widget_file_extension)
        self.widget_file_extension.signal_file_extension_change_to.connect(self.collect_rename_rule)
        self.widget_file_extension.signal_convert_to_capital.connect(self.collect_rename_rule)
        self.widget_file_extension.signal_convert_to_lowercase.connect(self.collect_rename_rule)
        self.widget_file_extension.signal_change_to_real_type.connect(self.collect_rename_rule)

        # 添加控件组2
        # 增
        self.widget_insert = WidgetInsert()
        self.ui.verticalLayout_place.addWidget(self.widget_insert)
        self.widget_insert.signal_insert.connect(self.collect_rename_rule)
        self.widget_insert.signal_insert_back.connect(self.collect_rename_rule)
        self.widget_insert.signal_add_prefix.connect(self.collect_rename_rule)
        self.widget_insert.signal_add_suffix.connect(self.collect_rename_rule)
        # 删
        self.widget_delete = WidgetDelete()
        self.ui.verticalLayout_place.addWidget(self.widget_delete)
        self.widget_delete.signal_delete_character.connect(self.collect_rename_rule)
        self.widget_delete.signal_delete_index.connect(self.collect_rename_rule)
        self.widget_delete.signal_delete_index_back.connect(self.collect_rename_rule)
        self.widget_delete.signal_delete_index_after.connect(self.collect_rename_rule)
        self.widget_delete.signal_delete_index_after_back.connect(self.collect_rename_rule)
        # 改
        self.widget_replace = WidgetReplace()
        self.ui.verticalLayout_place.addWidget(self.widget_replace)
        self.widget_replace.signal_replace.connect(self.collect_rename_rule)

        # 添加控件组3
        # 文件列表
        self.widget_file_list = WidgetFileList(self)
        self.ui.widget_file_list.layout().addWidget(self.widget_file_list)
        # 执行功能区
        self.widget_exec = WidgetExec()
        self.ui.widget_exec.layout().addWidget(self.widget_exec)
        self.widget_exec.signal_rename.connect(self.run_rename)
        self.widget_exec.signal_cancel.connect(self.cancel_rename)

    def collect_rename_rule(self, rule_class):
        """收集重命名规则"""
        self.class_collect.update(rule_class)
        self.widget_file_list.calc_filename()

    def run_rename(self, is_auto_dup):
        """执行重命名操作"""
        self.widget_file_list.run_rename(is_auto_dup)

    def cancel_rename(self):
        """撤销重命名操作"""
        self.widget_file_list.cancel_rename()
