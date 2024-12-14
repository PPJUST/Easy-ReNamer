from PySide6.QtCore import Signal
from PySide6.QtWidgets import QWidget, QApplication

from module.class_.class_rename_type import TypeConvert
from ui.src.ui_widget_filename_standard import Ui_Form


class WidgetFilenameStandard(QWidget):
    signal_standard_letter = Signal(TypeConvert)
    signal_standard_chinese = Signal(TypeConvert)
    signal_standard_character = Signal(TypeConvert)
    signal_excess_spaces = Signal(TypeConvert)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.set_tips()

        self.ui.checkBox_letter.stateChanged.connect(self.emit_signal_letter)
        self.ui.comboBox_letter.currentTextChanged.connect(self.signal_letter_changed)
        self.ui.checkBox_chinese.stateChanged.connect(self.emit_signal_chinese)
        self.ui.comboBox_chinese.currentTextChanged.connect(self.chinese_changed)
        self.ui.checkBox_character.stateChanged.connect(self.emit_signal_character)
        self.ui.comboBox_character.currentTextChanged.connect(self.character_changed)
        self.ui.checkBox_excess_spaces.stateChanged.connect(self.emit_signal_excess_spaces)

        self.ui.checkBox_excess_spaces.setChecked(True)

    def set_tips(self):
        """设置说明文本"""
        tips_auto_dig = '删除两端的空格、连续的空格'
        self.ui.checkBox_excess_spaces.setToolTip(tips_auto_dig)

    def emit_signal_letter(self):
        """发送信号"""
        is_enable = self.ui.checkBox_letter.isChecked()
        type_ = self.ui.comboBox_letter.currentText()

        rule_class = TypeConvert.ConvertLetter(is_enable, type_)
        self.signal_standard_letter.emit(rule_class)

    def signal_letter_changed(self):
        """选项变动"""
        # 变动后直接勾选即可
        self.ui.checkBox_letter.setChecked(True)
        self.emit_signal_letter()

    def emit_signal_chinese(self):
        """发送信号"""
        is_enable = self.ui.checkBox_chinese.isChecked()
        type_ = self.ui.comboBox_chinese.currentText()

        rule_class = TypeConvert.ConvertChinese(is_enable, type_)
        self.signal_standard_chinese.emit(rule_class)

    def chinese_changed(self):
        """选项变动"""
        # 变动后直接勾选即可
        self.ui.checkBox_chinese.setChecked(True)
        self.emit_signal_chinese()

    def emit_signal_character(self):
        """发送信号"""
        is_enable = self.ui.checkBox_character.isChecked()
        type_ = self.ui.comboBox_character.currentText()

        rule_class = TypeConvert.ConvertCharacter(is_enable, type_)
        self.signal_standard_character.emit(rule_class)

    def character_changed(self):
        """选项变动"""
        # 变动后直接勾选即可
        self.ui.checkBox_character.setChecked(True)
        self.emit_signal_character()

    def emit_signal_excess_spaces(self):
        """发送信号"""
        is_enable = self.ui.checkBox_excess_spaces.isChecked()

        rule_class = TypeConvert.ClearExcessSpaces(is_enable)
        self.signal_excess_spaces.emit(rule_class)


if __name__ == '__main__':
    app = QApplication()
    app.setStyle('Fusion')  # 设置风格
    show_ui = WidgetFilenameStandard()
    show_ui.show()
    app.exec()
