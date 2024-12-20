import base64

from PySide6.QtCore import Signal
from PySide6.QtGui import QPixmap, QIcon
from PySide6.QtWidgets import QWidget, QApplication, QFileDialog

from res.icon import *
from ui.src.ui_widget_file_list import Ui_Form
from ui.tableWidget_file_list import TabWidgetFileList


class WidgetFileList(QWidget):
    signal_dropped = Signal()

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        # 添加列表控件
        self.tableWidget_file_list = TabWidgetFileList(self)
        self.ui.verticalLayout__place.addWidget(self.tableWidget_file_list)
        # 设置图标
        self.set_tips()
        self._set_icon()

        # 绑定槽函数
        self.ui.pushButton_add_file.clicked.connect(self.select_file)
        self.ui.pushButton_add_folder.clicked.connect(self.select_folder)
        self.ui.pushButton_remove.clicked.connect(self.remove_item)
        self.ui.pushButton_clear.clicked.connect(self.clear_items)
        self.ui.toolButton_move_top.clicked.connect(self.move_top)
        self.ui.toolButton_move_bottom.clicked.connect(self.move_bottom)
        self.ui.toolButton_move_up.clicked.connect(self.move_up)
        self.ui.toolButton_move_down.clicked.connect(self.move_down)

        # 备忘录 - 屏蔽未完成的按钮
        self.ui.pushButton_add_folder.setVisible(False)

    def set_tips(self):
        """设置说明文本"""
        tips_top = '移动至顶部'
        self.ui.toolButton_move_top.setToolTip(tips_top)

        tips_bottom = '移动至底部'
        self.ui.toolButton_move_bottom.setToolTip(tips_bottom)

        tips_up = '上移一位'
        self.ui.toolButton_move_up.setToolTip(tips_up)

        tips_down = '下移一位'
        self.ui.toolButton_move_down.setToolTip(tips_down)

    def calc_filename(self):
        """实时计算新的文件名"""
        self.tableWidget_file_list.calc_new_filename()

    def select_file(self):
        """弹出文件选择框"""
        options = QFileDialog.Options()
        file_path, _ = QFileDialog.getOpenFileNames(self, "选择文件", "", "所有文件 (*);",
                                                    options=options)
        if file_path:
            self.tableWidget_file_list.insert_path_item(file_path)

    def select_folder(self):
        """弹出文件夹选择框"""
        pass

    def run_rename(self, is_auto_dup):
        self.tableWidget_file_list.rename(is_auto_dup)

    def cancel_rename(self):
        self.tableWidget_file_list.cancel_rename()

    def remove_item(self):
        """删除当前项目"""
        self.tableWidget_file_list.remove_item()

    def clear_items(self):
        """移除全部项目"""
        self.tableWidget_file_list.clear_items()

    def move_up(self):
        """将当前项目向上移动一位"""
        self.tableWidget_file_list.move_item_up()

    def move_down(self):
        """将当前项目向下移动一位"""
        self.tableWidget_file_list.move_item_down()

    def move_top(self):
        """将当前项目移动到顶部"""
        self.tableWidget_file_list.move_item_top()

    def move_bottom(self):
        """将当前项目移动到底部"""
        self.tableWidget_file_list.move_item_bottom()

    def _set_icon(self):
        """设置图标"""
        pixmap = QPixmap()
        pixmap.loadFromData(base64.b64decode(add_base64))
        self.ui.pushButton_add_file.setIcon(QIcon(pixmap))
        self.ui.pushButton_add_folder.setIcon(QIcon(pixmap))

        pixmap = QPixmap()
        pixmap.loadFromData(base64.b64decode(remove_base64))
        self.ui.pushButton_remove.setIcon(QIcon(pixmap))

        pixmap = QPixmap()
        pixmap.loadFromData(base64.b64decode(clear_base64))
        self.ui.pushButton_clear.setIcon(QIcon(pixmap))

        pixmap = QPixmap()
        pixmap.loadFromData(base64.b64decode(top_base64))
        self.ui.toolButton_move_top.setIcon(QIcon(pixmap))

        pixmap = QPixmap()
        pixmap.loadFromData(base64.b64decode(up_base64))
        self.ui.toolButton_move_up.setIcon(QIcon(pixmap))

        pixmap = QPixmap()
        pixmap.loadFromData(base64.b64decode(down_base64))
        self.ui.toolButton_move_down.setIcon(QIcon(pixmap))

        pixmap = QPixmap()
        pixmap.loadFromData(base64.b64decode(bottom_base64))
        self.ui.toolButton_move_bottom.setIcon(QIcon(pixmap))


if __name__ == '__main__':
    app = QApplication()
    app.setStyle('Fusion')  # 设置风格
    show_ui = WidgetFileList()
    show_ui.show()
    app.exec()
