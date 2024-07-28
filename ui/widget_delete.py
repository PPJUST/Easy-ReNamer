from PySide6.QtCore import Signal
from PySide6.QtWidgets import QWidget, QApplication

from module.class_.class_rename_type import TypeNormal
from ui.src.ui_widget_delete import Ui_Form


class WidgetDelete(QWidget):
    signal_delete_character = Signal(TypeNormal)
    signal_delete_index = Signal(TypeNormal)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.delete_character_changed()

        self.ui.checkBox_delete_character.stateChanged.connect(self.emit_signal_delete_character)
        self.ui.lineEdit_delete_character.textChanged.connect(self.delete_character_changed)

        self.ui.checkBox_delete_index.stateChanged.connect(self.emit_signal_delete_index)
        self.ui.spinBox_index.valueChanged.connect(self.delete_index_changed)
        self.ui.spinBox_delete_count.valueChanged.connect(self.delete_index_changed)

    def emit_signal_delete_character(self):
        """发送信号"""
        is_enable = self.ui.checkBox_delete_character.isChecked()
        delete_char = self.ui.lineEdit_delete_character.text()

        rule_class = TypeNormal.DeleteChar(is_enable, delete_char)
        self.signal_delete_character.emit(rule_class)

    def delete_character_changed(self):
        """选项变动"""
        text = self.ui.lineEdit_delete_character.text()
        if len(text):
            self.ui.checkBox_delete_character.setCheckable(True)
            self.ui.checkBox_delete_character.setChecked(True)
        else:
            self.ui.checkBox_delete_character.setCheckable(False)
            self.ui.checkBox_delete_character.setChecked(False)

        self.emit_signal_delete_character()

    def emit_signal_delete_index(self):
        """发送信号"""
        is_enable = self.ui.checkBox_delete_index.isChecked()
        start_index = self.ui.spinBox_index.value()
        delete_count = self.ui.spinBox_delete_count.value()

        rule_class = TypeNormal.DeleteIndex(is_enable, start_index, delete_count)
        self.signal_delete_index.emit(rule_class)

    def delete_index_changed(self):
        """选项变动"""
        # 变动后直接勾选即可
        self.ui.checkBox_delete_index.setChecked(True)
        self.emit_signal_delete_index()


if __name__ == '__main__':
    app = QApplication()
    app.setStyle('Fusion')  # 设置风格
    show_ui = WidgetDelete()
    show_ui.show()
    app.exec()
