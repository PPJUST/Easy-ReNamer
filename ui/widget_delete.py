from PySide6.QtCore import Signal
from PySide6.QtWidgets import QWidget, QApplication

from module.class_.class_rename_type import TypeNormal
from ui.src.ui_widget_delete import Ui_Form


class WidgetDelete(QWidget):
    signal_delete_character = Signal(TypeNormal)
    signal_delete_index = Signal(TypeNormal)
    signal_delete_index_back = Signal(TypeNormal)
    signal_delete_index_after = Signal(TypeNormal)
    signal_delete_index_after_back = Signal(TypeNormal)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.set_tips()

        self.ui.checkBox_delete_character.stateChanged.connect(self.emit_signal_delete_character)
        self.ui.lineEdit_delete_character.textChanged.connect(self.delete_character_changed)

        self.ui.checkBox_delete_index.stateChanged.connect(self.emit_signal_delete_index)
        self.ui.spinBox_index.valueChanged.connect(self.delete_index_changed)
        self.ui.spinBox_delete_count.valueChanged.connect(self.delete_index_changed)

        self.ui.checkBox_delete_index_back.stateChanged.connect(self.emit_signal_delete_index_back)
        self.ui.spinBox_index_back.valueChanged.connect(self.delete_index_back_changed)
        self.ui.spinBox_delete_count_back.valueChanged.connect(self.delete_index_back_changed)

        self.ui.checkBox_delete_index_after.stateChanged.connect(self.emit_signal_delete_after)
        self.ui.spinBox_index_del_after.valueChanged.connect(self.delete_index_after_changed)

        self.ui.checkBox_delete_index_after_back.stateChanged.connect(self.emit_signal_delete_after_back)
        self.ui.spinBox_index_del_after_back.valueChanged.connect(self.delete_index_after_back_changed)

    def set_tips(self):
        """设置说明文本"""
        tips_delete_delete_character = '删除文件名中的指定字符'
        self.ui.checkBox_delete_character.setToolTip(tips_delete_delete_character)

        tips_delete_delete_index = '从第N个字符起删除x个字符（包含第N个字符）'
        self.ui.checkBox_delete_index.setToolTip(tips_delete_delete_index)

        tips_delete_delete_index_back = '从倒数第N个字符起删除x个字符（包含倒数第N个字符）'
        self.ui.checkBox_delete_index_back.setToolTip(tips_delete_delete_index_back)

        tips_delete_delete_index_after = '删除第N个字符后的全部字符（不包含第N个字符）'
        self.ui.checkBox_delete_index_after.setToolTip(tips_delete_delete_index_after)

        tips_delete_delete_index_after_back = '删除倒数第N个字符后的全部字符（不包含倒数第N个字符）'
        self.ui.checkBox_delete_index_after_back.setToolTip(tips_delete_delete_index_after_back)

    def emit_signal_delete_character(self):
        """发送信号"""
        delete_char = self.ui.lineEdit_delete_character.text()
        if delete_char:
            is_enable = self.ui.checkBox_delete_character.isChecked()
        else:
            is_enable = False

        rule_class = TypeNormal.DeleteChar(is_enable, delete_char)
        self.signal_delete_character.emit(rule_class)

    def delete_character_changed(self):
        """选项变动"""
        text = self.ui.lineEdit_delete_character.text()
        if len(text):
            self.ui.checkBox_delete_character.setChecked(True)
        else:
            self.ui.checkBox_delete_character.setChecked(False)

        self.emit_signal_delete_character()

    def emit_signal_delete_index(self):
        """发送信号"""
        is_enable = self.ui.checkBox_delete_index.isChecked()
        start_index = self.ui.spinBox_index.value()
        delete_count = self.ui.spinBox_delete_count.value()

        rule_class = TypeNormal.DeleteIndex(is_enable, start_index, delete_count)
        self.signal_delete_index.emit(rule_class)

    def emit_signal_delete_index_back(self):
        """发送信号"""
        is_enable = self.ui.checkBox_delete_index_back.isChecked()
        start_index = self.ui.spinBox_index_back.value()
        delete_count = self.ui.spinBox_delete_count_back.value()

        rule_class = TypeNormal.DeleteIndexBack(is_enable, start_index, delete_count)
        self.signal_delete_index_back.emit(rule_class)

    def emit_signal_delete_after(self):
        """发送信号"""
        index = self.ui.spinBox_index_del_after.value()
        is_enable = self.ui.checkBox_delete_index_after.isChecked()

        rule_class = TypeNormal.DeleteIndexAfter(is_enable, index)
        self.signal_delete_index_after.emit(rule_class)

    def emit_signal_delete_after_back(self):
        """发送信号"""
        index = self.ui.spinBox_index_del_after_back.value()
        is_enable = self.ui.checkBox_delete_index_after_back.isChecked()

        rule_class = TypeNormal.DeleteIndexAfterBack(is_enable, index)
        self.signal_delete_index_after_back.emit(rule_class)

    def delete_index_changed(self):
        """选项变动"""
        # 变动后直接勾选即可
        self.ui.checkBox_delete_index.setChecked(True)
        self.emit_signal_delete_index()

    def delete_index_back_changed(self):
        """选项变动"""
        # 变动后直接勾选即可
        self.ui.checkBox_delete_index_back.setChecked(True)
        self.emit_signal_delete_index_back()

    def delete_index_after_changed(self):
        """选项变动"""
        # 变动后直接勾选即可
        self.ui.checkBox_delete_index_after.setChecked(True)
        self.emit_signal_delete_after()

    def delete_index_after_back_changed(self):
        """选项变动"""
        # 变动后直接勾选即可
        self.ui.checkBox_delete_index_after_back.setChecked(True)
        self.emit_signal_delete_after_back()


if __name__ == '__main__':
    app = QApplication()
    app.setStyle('Fusion')  # 设置风格
    show_ui = WidgetDelete()
    show_ui.show()
    app.exec()
