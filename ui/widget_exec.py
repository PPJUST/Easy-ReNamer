import base64
import sys

from PySide6.QtCore import Signal
from PySide6.QtGui import QPixmap, QIcon
from PySide6.QtWidgets import QWidget, QApplication

from res.icon import *
from ui.src.ui_widget_exec import Ui_Form


class WidgetExec(QWidget):
    signal_rename = Signal(bool)
    signal_cancel = Signal()

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.set_tips()
        self._set_icon()

        # 设置槽函数
        self.ui.pushButton_quit.clicked.connect(lambda: sys.exit())
        self.ui.pushButton_rename.clicked.connect(self.emit_signal_rename)
        self.ui.pushButton_cancel.clicked.connect(self.emit_signal_cancel)

    def set_tips(self):
        """设置说明文本"""
        tips_auto_dup = '不再弹出重复文件名提示，在文件名后自动添加后缀\n（参照Windows规则，在文件名后添加" (2)“等后缀'
        self.ui.checkBox_auto_deal_dup.setToolTip(tips_auto_dup)

        tips_cancel = '撤销对应文件的所有重命名操作，恢复到最开始的文件名'
        self.ui.pushButton_cancel.setToolTip(tips_cancel)

    def _set_icon(self):
        """设置图标"""
        pixmap = QPixmap()
        pixmap.loadFromData(base64.b64decode(rename_base64))
        self.ui.pushButton_rename.setIcon(QIcon(pixmap))

        pixmap = QPixmap()
        pixmap.loadFromData(base64.b64decode(cancel_base64))
        self.ui.pushButton_cancel.setIcon(QIcon(pixmap))

        pixmap = QPixmap()
        pixmap.loadFromData(base64.b64decode(quit_base64))
        self.ui.pushButton_quit.setIcon(QIcon(pixmap))

    def emit_signal_rename(self):
        """发送信号"""
        self.signal_rename.emit(self.ui.checkBox_auto_deal_dup.isChecked())

    def emit_signal_cancel(self):
        """发送信号"""
        self.signal_cancel.emit()


if __name__ == '__main__':
    app = QApplication()
    app.setStyle('Fusion')  # 设置风格
    show_ui = WidgetExec()
    show_ui.show()
    app.exec()
