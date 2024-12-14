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

        self.set_tips()

        self.ui.lineEdit_file_extension.textChanged.connect(self.change_to_changed)
        self.ui.checkBox_change_to.stateChanged.connect(self.emit_signal_change_to)
        self.ui.checkBox_change_to.stateChanged.connect(self.set_exclusive_group_change)
        self.ui.checkBox_real_type.stateChanged.connect(self.emit_signal_real_type)
        self.ui.checkBox_real_type.stateChanged.connect(self.set_exclusive_group_real)
        self.ui.checkBox_lowercase.stateChanged.connect(self.emit_signal_lowercase)
        self.ui.checkBox_lowercase.stateChanged.connect(self.set_exclusive_group_lowercase)
        self.ui.checkBox_capital.stateChanged.connect(self.emit_signal_capital)
        self.ui.checkBox_capital.stateChanged.connect(self.set_exclusive_group_capital)

    def set_tips(self):
        """设置说明文本"""
        tips_change_to = '修改后缀名，请勿将文件的后缀名修改为空'
        self.ui.checkBox_change_to.setToolTip(tips_change_to)

        tips_real_type = ('修改后缀名为文件的真实类型\n'
                          '注意：\n'
                          '  1. 仅支持部分常见的文件类型\n'
                          '  2.结果可能存在偏差，请手工检查（例：分卷压缩包的分卷包会被识别为压缩包）')
        self.ui.checkBox_real_type.setToolTip(tips_real_type)

    def emit_signal_change_to(self):
        """发送信号"""
        file_extension = self.ui.lineEdit_file_extension.text()
        if len(file_extension.strip()):
            is_enable = self.ui.checkBox_change_to.isChecked()
        else:
            is_enable = False

        rule_class = TypeFileExtension.ChangeTo(is_enable, file_extension)
        self.signal_file_extension_change_to.emit(rule_class)

    def change_to_changed(self):
        """选项变动"""
        text = self.ui.lineEdit_file_extension.text()
        if len(text.strip()):
            self.ui.checkBox_change_to.setChecked(True)
        else:
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

    def set_exclusive_group_lowercase(self):
        """大小写互斥勾选"""
        group_low = self.ui.checkBox_lowercase
        group_cap = self.ui.checkBox_capital

        if group_low.isChecked() and group_cap.isChecked():
            group_cap.setChecked(False)

    def set_exclusive_group_capital(self):
        """大小写互斥勾选"""
        group_low = self.ui.checkBox_lowercase
        group_cap = self.ui.checkBox_capital

        if group_low.isChecked() and group_cap.isChecked():
            group_low.setChecked(False)

    def set_exclusive_group_change(self):
        """手工修改与自动修改互斥"""
        group_change = self.ui.checkBox_change_to
        group_real = self.ui.checkBox_real_type

        if group_change.isChecked() and group_real.isChecked():
            group_real.setChecked(False)

    def set_exclusive_group_real(self):
        """手工修改与自动修改互斥"""
        group_change = self.ui.checkBox_change_to
        group_real = self.ui.checkBox_real_type

        if group_change.isChecked() and group_real.isChecked():
            group_change.setChecked(False)


if __name__ == '__main__':
    app = QApplication()
    app.setStyle('Fusion')  # 设置风格
    show_ui = WidgetFileExtension()
    show_ui.show()
    app.exec()
