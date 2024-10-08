from PySide6.QtCore import Signal
from PySide6.QtGui import QFont
from PySide6.QtWidgets import QWidget, QApplication

from module.class_.class_rename_type import TypeNormal, TypePattern
from ui.src.ui_widget_filename_pattern import Ui_Form


class WidgetFilenamePattern(QWidget):
    signal_pattern = Signal(TypeNormal)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        # self._show_layout_digit(False)  # 隐藏数字的更多选项控件
        # self._show_layout_char(False)# 隐藏字符的更多选项控件
        self.set_tips()

        self.ui.checkBox_pattern.stateChanged.connect(self.emit_signal)
        self.ui.lineEdit_pattern.textChanged.connect(self.pattern_changed)
        self.ui.spinBox_digit_start.valueChanged.connect(self.emit_signal)
        self.ui.spinBox_digit_step.valueChanged.connect(self.emit_signal)
        self.ui.spinBox_digit_length.valueChanged.connect(self.emit_signal)
        self.ui.checkBox_auto_fill_digit_length.stateChanged.connect(self.emit_signal)
        self.ui.checkBox_random_digit.stateChanged.connect(self.emit_signal)
        self.ui.checkBox_random_lowercase.stateChanged.connect(self.emit_signal)
        self.ui.checkBox_random_capital.stateChanged.connect(self.emit_signal)
        self.ui.checkBox_random_punctuation.stateChanged.connect(self.emit_signal)
        self.ui.spinBox_char_length.valueChanged.connect(self.emit_signal)

        # self.ui.lineEdit_pattern.textChanged.connect(self._show_more_option)  # 用于隐藏/显示数字、字符的更多选项

        # 设置字体
        font = QFont()
        font.setPointSize(12)
        self.ui.lineEdit_pattern.setFont(font)

    def set_tips(self):
        """设置说明文本"""
        tips_auto_dig = '示例：\n1 --> 001\n2 --> 002'
        self.ui.checkBox_auto_fill_digit_length.setToolTip(tips_auto_dig)

        tips_pattern = ('示例：'
                        '\n1.修改为指定文本（例如修改为"目标文件名"）：目标文件名'
                        '\n2. 在文件名前添加父文件夹名（即<父目录名> - <原文件名>）：/ - *'
                        '\n3.在文件名后添加随机字符（即<原文件名>_<随机字符>）：*_?'
                        '\n4.在文件名后添加数字编号（即<原文件名>#<数字编号>）：*###')
        self.ui.checkBox_pattern.setToolTip(tips_pattern)
        self.ui.lineEdit_pattern.setToolTip(tips_pattern)

    def emit_signal(self):
        """发送信号"""
        pattern = self.ui.lineEdit_pattern.text()
        if len(pattern):
            is_enable = self.ui.checkBox_pattern.isChecked()
        else:
            is_enable = False

        digit_start = self.ui.spinBox_digit_start.value()
        digit_step = self.ui.spinBox_digit_step.value()
        digit_length = self.ui.spinBox_digit_length.value()
        auto_fill = self.ui.checkBox_auto_fill_digit_length.isChecked()

        random_digit = self.ui.checkBox_random_digit.isChecked()
        random_lowercase = self.ui.checkBox_random_lowercase.isChecked()
        random_capital = self.ui.checkBox_random_capital.isChecked()
        random_punctuation = self.ui.checkBox_random_punctuation.isChecked()
        random_length = self.ui.spinBox_char_length.value()

        rule_class = TypePattern(is_enable, pattern)
        rule_class.update_digit(digit_start, digit_step, digit_length, auto_fill)
        rule_class.update_char(random_digit, random_lowercase, random_capital, random_punctuation, random_length)
        self.signal_pattern.emit(rule_class)
        self._set_preview_tips(rule_class.get_preview())

    def pattern_changed(self):
        """选项变动"""
        text = self.ui.lineEdit_pattern.text()
        if len(text):
            self.ui.checkBox_pattern.setChecked(True)

        self.emit_signal()

    def _show_layout_digit(self, is_show):
        """显示数字选项布局"""
        self.ui.widget_digit.setVisible(is_show)

    def _show_layout_char(self, is_show):
        """显示字符选项布局"""
        self.ui.widget_char.setVisible(is_show)

    def _show_more_option(self):
        """显示更多选项"""
        pattern = self.ui.lineEdit_pattern.text()
        if '##' in pattern or '"' in pattern:
            self._show_layout_digit(True)
        else:
            self._show_layout_digit(False)

        if '?' in pattern:
            self._show_layout_char(True)
        else:
            self._show_layout_char(False)

    def _set_preview_tips(self, tip: str):
        """设置预览文本"""
        if tip:
            self.ui.lineEdit_pattern.setToolTip(tip)


if __name__ == '__main__':
    app = QApplication()
    app.setStyle('Fusion')  # 设置风格
    show_ui = WidgetFilenamePattern()
    show_ui.show()
    app.exec()
