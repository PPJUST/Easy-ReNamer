from PySide6.QtCore import Signal
from PySide6.QtWidgets import QWidget, QApplication

from module.class_.class_rename_type import TypeNormal
from ui.src.ui_widget_insert import Ui_Form


class WidgetInsert(QWidget):
    signal_add_prefix = Signal(TypeNormal)
    signal_add_suffix = Signal(TypeNormal)
    signal_insert = Signal(TypeNormal)
    signal_insert_back = Signal(TypeNormal)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.insert_changed()

        self.ui.checkBox_add_prefix.stateChanged.connect(self.emit_signal_prefix)
        self.ui.lineEdit_add_prefix.textChanged.connect(self.prefix_changed)
        self.ui.checkBox_add_suffix.stateChanged.connect(self.emit_signal_suffix)
        self.ui.lineEdit_add_suffix.textChanged.connect(self.suffix_changed)
        self.ui.checkBox_insert_index.stateChanged.connect(self.emit_signal_insert)
        self.ui.spinBox_index.valueChanged.connect(self.insert_changed)
        self.ui.lineEdit_insert_character.textChanged.connect(self.insert_changed)
        self.ui.checkBox_insert_index_back.stateChanged.connect(self.emit_signal_insert_back)
        self.ui.spinBox_index_back.valueChanged.connect(self.insert_back_changed)
        self.ui.lineEdit_insert_character_back.textChanged.connect(self.insert_back_changed)

    def emit_signal_prefix(self):
        """发送信号"""
        char = self.ui.lineEdit_add_prefix.text()
        if len(char):
            is_enable = self.ui.checkBox_add_prefix.isChecked()
        else:
            is_enable = False

        rule_class = TypeNormal.AddPrefix(is_enable, char)
        self.signal_add_prefix.emit(rule_class)

    def prefix_changed(self):
        """选项变动"""
        text = self.ui.lineEdit_add_prefix.text()
        if len(text):
            self.ui.checkBox_add_prefix.setChecked(True)
        else:
            self.ui.checkBox_add_prefix.setChecked(False)

        self.emit_signal_prefix()

    def emit_signal_suffix(self):
        """发送信号"""
        char = self.ui.lineEdit_add_suffix.text()
        if len(char):
            is_enable = self.ui.checkBox_add_suffix.isChecked()
        else:
            is_enable = False

        rule_class = TypeNormal.AddSuffix(is_enable, char)
        self.signal_add_suffix.emit(rule_class)

    def suffix_changed(self):
        """选项变动"""
        text = self.ui.lineEdit_add_suffix.text()
        if len(text):
            self.ui.checkBox_add_suffix.setChecked(True)
        else:
            self.ui.checkBox_add_suffix.setChecked(False)

        self.emit_signal_suffix()

    def emit_signal_insert(self):
        """发送信号"""
        index = self.ui.spinBox_index.value()
        char = self.ui.lineEdit_insert_character.text()
        if len(char):
            is_enable = self.ui.checkBox_insert_index.isChecked()
        else:
            is_enable = False

        rule_class = TypeNormal.Insert(is_enable, index, char)
        self.signal_insert.emit(rule_class)

    def insert_changed(self):
        """选项变动"""
        text = self.ui.lineEdit_insert_character.text()
        if len(text):
            self.ui.checkBox_insert_index.setChecked(True)
        else:
            self.ui.checkBox_insert_index.setChecked(False)

        self.emit_signal_insert()

    def emit_signal_insert_back(self):
        """发送信号"""
        index = self.ui.spinBox_index_back.value()
        char = self.ui.lineEdit_insert_character_back.text()
        if len(char):
            is_enable = self.ui.checkBox_insert_index_back.isChecked()
        else:
            is_enable = False

        rule_class = TypeNormal.InsertBack(is_enable, index, char)
        self.signal_insert_back.emit(rule_class)

    def insert_back_changed(self):
        """选项变动"""
        text = self.ui.lineEdit_insert_character_back.text()
        if len(text):
            self.ui.checkBox_insert_index_back.setChecked(True)
        else:
            self.ui.checkBox_insert_index_back.setChecked(False)

        self.emit_signal_insert_back()


if __name__ == '__main__':
    app = QApplication()
    app.setStyle('Fusion')  # 设置风格
    show_ui = WidgetInsert()
    show_ui.show()
    app.exec()
