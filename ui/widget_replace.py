from PySide6.QtCore import Signal
from PySide6.QtWidgets import QWidget, QApplication

from module.class_.class_rename_type import TypeNormal
from ui.src.ui_widget_replace import Ui_Form


class WidgetReplace(QWidget):
    signal_replace = Signal(TypeNormal)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.ui.checkBox_replace.stateChanged.connect(self.emit_signal)
        self.ui.lineEdit_old_character.textChanged.connect(self.prefix_changed)
        self.ui.lineEdit_new_character.textChanged.connect(self.prefix_changed)

    def emit_signal(self):
        """发送信号"""
        old_char = self.ui.lineEdit_old_character.text()
        new_char = self.ui.lineEdit_new_character.text()
        if len(old_char) and len(new_char):
            is_enable = self.ui.checkBox_replace.isChecked()
        else:
            is_enable = False

        rule_class = TypeNormal.Replace(is_enable, old_char, new_char)
        self.signal_replace.emit(rule_class)

    def prefix_changed(self):
        """选项变动"""
        text_old = self.ui.lineEdit_old_character.text()
        text_new = self.ui.lineEdit_new_character.text()
        if len(text_old) and len(text_new):
            self.ui.checkBox_replace.setCheckable(True)
            self.ui.checkBox_replace.setChecked(True)

        self.emit_signal()


if __name__ == '__main__':
    app = QApplication()
    app.setStyle('Fusion')  # 设置风格
    show_ui = WidgetReplace()
    show_ui.show()
    app.exec()
