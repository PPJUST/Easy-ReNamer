from PySide6.QtCore import Signal
from PySide6.QtWidgets import QWidget, QApplication

from module.class_.class_rename_type import TypeFileExtension
from ui.src.ui_widget_file_extension import Ui_Form


class WidgetFileExtension(QWidget):
    signal_file_extension_change_to = Signal(TypeFileExtension)
    signal_convert_to_lowercase = Signal(TypeFileExtension)
    signal_convert_to_capital = Signal(TypeFileExtension)
    signal_change_to_real_type = Signal(TypeFileExtension)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.change_to_changed()

        self.ui.checkBox_change_to.stateChanged.connect(self.emit_signal_change_to)
        self.ui.lineEdit_file_extension.textChanged.connect(self.change_to_changed)
        self.ui.checkBox_lowercase.stateChanged.connect(self.emit_signal_lowercase)
        self.ui.checkBox_lowercase.stateChanged.connect(self.set_button_group_lowercase)
        self.ui.checkBox_capital.stateChanged.connect(self.emit_signal_capital)
        self.ui.checkBox_capital.stateChanged.connect(self.set_button_group_capital)
        self.ui.checkBox_real_type.stateChanged.connect(self.emit_signal_real_type)

        # 屏蔽功能
        self.ui.checkBox_real_type.setEnabled(False)
        self.ui.checkBox_real_type.setVisible(False)

    def emit_signal_change_to(self):
        """发送信号"""
        is_enable = self.ui.checkBox_change_to.isChecked()
        file_extension = self.ui.lineEdit_file_extension.text()

        rule_class = TypeFileExtension.ChangeTo(is_enable, file_extension)
        self.signal_file_extension_change_to.emit(rule_class)

    def change_to_changed(self):
        """选项变动"""
        text = self.ui.lineEdit_file_extension.text()
        if len(text):
            self.ui.checkBox_change_to.setCheckable(True)
            self.ui.checkBox_change_to.setChecked(True)
        else:
            self.ui.checkBox_change_to.setCheckable(False)
            self.ui.checkBox_change_to.setChecked(False)

        self.emit_signal_change_to()

    def emit_signal_lowercase(self):
        """发送信号"""
        is_enable = self.ui.checkBox_lowercase.isChecked()

        rule_class = TypeFileExtension.ConvertToLowercase(is_enable)
        self.signal_convert_to_lowercase.emit(rule_class)

    def emit_signal_capital(self):
        """发送信号"""
        is_enable = self.ui.checkBox_capital.isChecked()

        rule_class = TypeFileExtension.ConvertToCapital(is_enable)
        self.signal_convert_to_capital.emit(rule_class)

    def emit_signal_real_type(self):
        """发送信号"""
        is_enable = self.ui.checkBox_real_type.isChecked()

        rule_class = TypeFileExtension.ChangeToRealType(is_enable)
        self.signal_change_to_real_type.emit(rule_class)

    def set_button_group_lowercase(self):
        """设置大小写冲突的按钮组"""
        button_low = self.ui.checkBox_lowercase
        button_cap = self.ui.checkBox_capital

        if button_low.isChecked() and button_cap.isChecked():
            button_cap.setChecked(False)

    def set_button_group_capital(self):
        """设置大小写冲突的按钮组"""
        button_low = self.ui.checkBox_lowercase
        button_cap = self.ui.checkBox_capital

        if button_low.isChecked() and button_cap.isChecked():
            button_low.setChecked(False)


if __name__ == '__main__':
    app = QApplication()
    app.setStyle('Fusion')  # 设置风格
    show_ui = WidgetFileExtension()
    show_ui.show()
    app.exec()