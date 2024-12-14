# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_widget_filename_patternBwQWsY.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractSpinBox, QApplication, QCheckBox, QFrame,
    QGridLayout, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QSpacerItem, QSpinBox,
    QToolButton, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(483, 426)
        self.verticalLayout_8 = QVBoxLayout(Form)
        self.verticalLayout_8.setSpacing(3)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(3, 3, 3, 3)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.checkBox_pattern = QCheckBox(Form)
        self.checkBox_pattern.setObjectName(u"checkBox_pattern")

        self.horizontalLayout_2.addWidget(self.checkBox_pattern)

        self.toolButton_choose_pattern = QToolButton(Form)
        self.toolButton_choose_pattern.setObjectName(u"toolButton_choose_pattern")

        self.horizontalLayout_2.addWidget(self.toolButton_choose_pattern)

        self.lineEdit_pattern = QLineEdit(Form)
        self.lineEdit_pattern.setObjectName(u"lineEdit_pattern")

        self.horizontalLayout_2.addWidget(self.lineEdit_pattern)


        self.verticalLayout_8.addLayout(self.horizontalLayout_2)

        self.widget_preset_pattern = QWidget(Form)
        self.widget_preset_pattern.setObjectName(u"widget_preset_pattern")
        self.verticalLayout_4 = QVBoxLayout(self.widget_preset_pattern)
        self.verticalLayout_4.setSpacing(3)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(3, 3, 3, 3)
        self.pushButton_preset_1 = QPushButton(self.widget_preset_pattern)
        self.pushButton_preset_1.setObjectName(u"pushButton_preset_1")

        self.verticalLayout_4.addWidget(self.pushButton_preset_1)

        self.pushButton_preset_2 = QPushButton(self.widget_preset_pattern)
        self.pushButton_preset_2.setObjectName(u"pushButton_preset_2")

        self.verticalLayout_4.addWidget(self.pushButton_preset_2)

        self.pushButton_preset_3 = QPushButton(self.widget_preset_pattern)
        self.pushButton_preset_3.setObjectName(u"pushButton_preset_3")

        self.verticalLayout_4.addWidget(self.pushButton_preset_3)


        self.verticalLayout_8.addWidget(self.widget_preset_pattern)

        self.line_9 = QFrame(Form)
        self.line_9.setObjectName(u"line_9")
        self.line_9.setFrameShape(QFrame.Shape.HLine)
        self.line_9.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_8.addWidget(self.line_9)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setSpacing(3)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setSpacing(3)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_10 = QLabel(Form)
        self.label_10.setObjectName(u"label_10")

        self.verticalLayout_7.addWidget(self.label_10)

        self.line_4 = QFrame(Form)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFrameShape(QFrame.Shape.HLine)
        self.line_4.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_7.addWidget(self.line_4)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.horizontalLayout_7.addItem(self.verticalSpacer)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setSpacing(3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_3.addWidget(self.label_2)

        self.line = QFrame(Form)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_3.addWidget(self.line)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setSpacing(3)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_5 = QLabel(Form)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_6.addWidget(self.label_5)

        self.widget_digit = QWidget(Form)
        self.widget_digit.setObjectName(u"widget_digit")
        self.horizontalLayout_5 = QHBoxLayout(self.widget_digit)
        self.horizontalLayout_5.setSpacing(3)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.line_6 = QFrame(self.widget_digit)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setFrameShape(QFrame.Shape.VLine)
        self.line_6.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_5.addWidget(self.line_6)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(3)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(0)
        self.gridLayout.setVerticalSpacing(3)
        self.spinBox_digit_start = QSpinBox(self.widget_digit)
        self.spinBox_digit_start.setObjectName(u"spinBox_digit_start")
        self.spinBox_digit_start.setMinimum(-9999)
        self.spinBox_digit_start.setMaximum(9999)
        self.spinBox_digit_start.setValue(1)

        self.gridLayout.addWidget(self.spinBox_digit_start, 0, 1, 1, 1)

        self.label_8 = QLabel(self.widget_digit)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout.addWidget(self.label_8, 2, 0, 1, 1)

        self.label_6 = QLabel(self.widget_digit)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout.addWidget(self.label_6, 0, 0, 1, 1)

        self.spinBox_digit_length = QSpinBox(self.widget_digit)
        self.spinBox_digit_length.setObjectName(u"spinBox_digit_length")
        self.spinBox_digit_length.setMinimum(1)
        self.spinBox_digit_length.setMaximum(255)

        self.gridLayout.addWidget(self.spinBox_digit_length, 2, 1, 1, 1)

        self.spinBox_digit_step = QSpinBox(self.widget_digit)
        self.spinBox_digit_step.setObjectName(u"spinBox_digit_step")
        self.spinBox_digit_step.setMinimum(-9999)
        self.spinBox_digit_step.setMaximum(9999)
        self.spinBox_digit_step.setStepType(QAbstractSpinBox.StepType.DefaultStepType)
        self.spinBox_digit_step.setValue(1)

        self.gridLayout.addWidget(self.spinBox_digit_step, 1, 1, 1, 1)

        self.label_7 = QLabel(self.widget_digit)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout.addWidget(self.label_7, 1, 0, 1, 1)


        self.verticalLayout_2.addLayout(self.gridLayout)

        self.checkBox_auto_fill_digit_length = QCheckBox(self.widget_digit)
        self.checkBox_auto_fill_digit_length.setObjectName(u"checkBox_auto_fill_digit_length")

        self.verticalLayout_2.addWidget(self.checkBox_auto_fill_digit_length)


        self.horizontalLayout_5.addLayout(self.verticalLayout_2)

        self.horizontalLayout_5.setStretch(1, 1)

        self.horizontalLayout_6.addWidget(self.widget_digit)


        self.verticalLayout_3.addLayout(self.horizontalLayout_6)

        self.line_2 = QFrame(Form)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_3.addWidget(self.line_2)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setSpacing(3)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_4 = QLabel(Form)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_4.addWidget(self.label_4)

        self.widget_char = QWidget(Form)
        self.widget_char.setObjectName(u"widget_char")
        self.horizontalLayout_3 = QHBoxLayout(self.widget_char)
        self.horizontalLayout_3.setSpacing(3)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.line_5 = QFrame(self.widget_char)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setFrameShape(QFrame.Shape.VLine)
        self.line_5.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_3.addWidget(self.line_5)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(3)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.checkBox_random_digit = QCheckBox(self.widget_char)
        self.checkBox_random_digit.setObjectName(u"checkBox_random_digit")

        self.verticalLayout.addWidget(self.checkBox_random_digit)

        self.checkBox_random_lowercase = QCheckBox(self.widget_char)
        self.checkBox_random_lowercase.setObjectName(u"checkBox_random_lowercase")

        self.verticalLayout.addWidget(self.checkBox_random_lowercase)

        self.checkBox_random_capital = QCheckBox(self.widget_char)
        self.checkBox_random_capital.setObjectName(u"checkBox_random_capital")

        self.verticalLayout.addWidget(self.checkBox_random_capital)

        self.checkBox_random_punctuation = QCheckBox(self.widget_char)
        self.checkBox_random_punctuation.setObjectName(u"checkBox_random_punctuation")

        self.verticalLayout.addWidget(self.checkBox_random_punctuation)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(3)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_9 = QLabel(self.widget_char)
        self.label_9.setObjectName(u"label_9")

        self.horizontalLayout.addWidget(self.label_9)

        self.spinBox_char_length = QSpinBox(self.widget_char)
        self.spinBox_char_length.setObjectName(u"spinBox_char_length")
        self.spinBox_char_length.setMinimum(1)
        self.spinBox_char_length.setMaximum(255)

        self.horizontalLayout.addWidget(self.spinBox_char_length)

        self.horizontalLayout.setStretch(1, 1)

        self.verticalLayout.addLayout(self.horizontalLayout)


        self.horizontalLayout_3.addLayout(self.verticalLayout)

        self.horizontalLayout_3.setStretch(1, 1)

        self.horizontalLayout_4.addWidget(self.widget_char)


        self.verticalLayout_3.addLayout(self.horizontalLayout_4)

        self.line_3 = QFrame(Form)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.Shape.HLine)
        self.line_3.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_3.addWidget(self.line_3)

        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_3.addWidget(self.label_3)


        self.horizontalLayout_7.addLayout(self.verticalLayout_3)


        self.verticalLayout_7.addLayout(self.horizontalLayout_7)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_7.addItem(self.verticalSpacer_2)


        self.horizontalLayout_8.addLayout(self.verticalLayout_7)

        self.line_7 = QFrame(Form)
        self.line_7.setObjectName(u"line_7")
        self.line_7.setFrameShape(QFrame.Shape.VLine)
        self.line_7.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_8.addWidget(self.line_7)

        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        self.verticalLayout_6 = QVBoxLayout(self.widget)
        self.verticalLayout_6.setSpacing(3)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(3, 3, 3, 3)
        self.verticalLayout_standard = QVBoxLayout()
        self.verticalLayout_standard.setSpacing(3)
        self.verticalLayout_standard.setObjectName(u"verticalLayout_standard")

        self.verticalLayout_6.addLayout(self.verticalLayout_standard)

        self.line_8 = QFrame(self.widget)
        self.line_8.setObjectName(u"line_8")
        self.line_8.setFrameShape(QFrame.Shape.HLine)
        self.line_8.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_6.addWidget(self.line_8)

        self.verticalLayout_file_extension = QVBoxLayout()
        self.verticalLayout_file_extension.setSpacing(3)
        self.verticalLayout_file_extension.setObjectName(u"verticalLayout_file_extension")

        self.verticalLayout_6.addLayout(self.verticalLayout_file_extension)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer_3)


        self.horizontalLayout_8.addWidget(self.widget)

        self.horizontalLayout_8.setStretch(2, 1)

        self.verticalLayout_8.addLayout(self.horizontalLayout_8)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.checkBox_pattern.setText(QCoreApplication.translate("Form", u"\u547d\u540d\u6a21\u677f\uff1a", None))
        self.toolButton_choose_pattern.setText(QCoreApplication.translate("Form", u"...", None))
        self.lineEdit_pattern.setPlaceholderText(QCoreApplication.translate("Form", u"\u4f8b: *_## \u4e3a<\u539f\u6587\u4ef6\u540d>_<\u6570\u5b57\u7f16\u53f7>", None))
        self.pushButton_preset_1.setText(QCoreApplication.translate("Form", u"<\u7236\u6587\u4ef6\u5939\u540d> <\u539f\u6587\u4ef6\u540d> | / *", None))
        self.pushButton_preset_2.setText(QCoreApplication.translate("Form", u"<\u539f\u6587\u4ef6\u540d> #<\u6570\u5b57\u7f16\u53f7> | * ###", None))
        self.pushButton_preset_3.setText(QCoreApplication.translate("Form", u"<\u539f\u6587\u4ef6\u540d>_<\u968f\u673a\u5b57\u7b26> | *_?", None))
        self.label_10.setText(QCoreApplication.translate("Form", u"\u7b26\u53f7\u8bf4\u660e\uff1a", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"* \u63d2\u5165\u539f\u6587\u4ef6\u540d", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"##\u6216\"\n"
"\u63d2\u5165\u6570\u5b57\u7f16\u53f7", None))
        self.label_8.setText(QCoreApplication.translate("Form", u"\u4f4d\u6570", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"\u8d77\u59cb", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"\u6b65\u957f", None))
        self.checkBox_auto_fill_digit_length.setText(QCoreApplication.translate("Form", u"\u81ea\u52a8\u8865\u9f50\u4f4d\u6570", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"?\n"
"\u63d2\u5165\u968f\u673a\u5b57\u7b26", None))
        self.checkBox_random_digit.setText(QCoreApplication.translate("Form", u"\u6570\u5b57", None))
        self.checkBox_random_lowercase.setText(QCoreApplication.translate("Form", u"\u5c0f\u5199\u5b57\u6bcd", None))
        self.checkBox_random_capital.setText(QCoreApplication.translate("Form", u"\u5927\u5199\u5b57\u6bcd", None))
        self.checkBox_random_punctuation.setText(QCoreApplication.translate("Form", u"\u7b26\u53f7", None))
        self.label_9.setText(QCoreApplication.translate("Form", u"\u4f4d\u6570", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"/ \u63d2\u5165\u7236\u76ee\u5f55\u540d", None))
    # retranslateUi

