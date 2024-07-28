# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_widget_filename_standardFqJLqI.ui'
##
## Created by: Qt User Interface Compiler version 6.1.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(141, 131)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setSpacing(3)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(3, 3, 3, 3)
        self.groupBox = QGroupBox(Form)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout_2 = QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setSpacing(3)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(3, 3, 3, 3)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(3)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.checkBox_letter = QCheckBox(self.groupBox)
        self.checkBox_letter.setObjectName(u"checkBox_letter")

        self.horizontalLayout.addWidget(self.checkBox_letter)

        self.comboBox_letter = QComboBox(self.groupBox)
        self.comboBox_letter.addItem("")
        self.comboBox_letter.addItem("")
        self.comboBox_letter.setObjectName(u"comboBox_letter")

        self.horizontalLayout.addWidget(self.comboBox_letter)

        self.horizontalLayout.setStretch(1, 1)

        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(3)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.checkBox_chinese = QCheckBox(self.groupBox)
        self.checkBox_chinese.setObjectName(u"checkBox_chinese")

        self.horizontalLayout_2.addWidget(self.checkBox_chinese)

        self.comboBox_chinese = QComboBox(self.groupBox)
        self.comboBox_chinese.addItem("")
        self.comboBox_chinese.addItem("")
        self.comboBox_chinese.setObjectName(u"comboBox_chinese")

        self.horizontalLayout_2.addWidget(self.comboBox_chinese)

        self.horizontalLayout_2.setStretch(1, 1)

        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(3)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.checkBox_character = QCheckBox(self.groupBox)
        self.checkBox_character.setObjectName(u"checkBox_character")

        self.horizontalLayout_3.addWidget(self.checkBox_character)

        self.comboBox_character = QComboBox(self.groupBox)
        self.comboBox_character.addItem("")
        self.comboBox_character.addItem("")
        self.comboBox_character.setObjectName(u"comboBox_character")

        self.horizontalLayout_3.addWidget(self.comboBox_character)

        self.horizontalLayout_3.setStretch(1, 1)

        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.checkBox_excess_spaces = QCheckBox(self.groupBox)
        self.checkBox_excess_spaces.setObjectName(u"checkBox_excess_spaces")

        self.verticalLayout_2.addWidget(self.checkBox_excess_spaces)


        self.verticalLayout.addWidget(self.groupBox)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.groupBox.setTitle(QCoreApplication.translate("Form", u"\u6807\u51c6\u5316", None))
        self.checkBox_letter.setText(QCoreApplication.translate("Form", u"\u5b57\u6bcd\u6539\u4e3a", None))
        self.comboBox_letter.setItemText(0, QCoreApplication.translate("Form", u"\u5c0f\u5199", None))
        self.comboBox_letter.setItemText(1, QCoreApplication.translate("Form", u"\u5927\u5199", None))

        self.checkBox_chinese.setText(QCoreApplication.translate("Form", u"\u6c49\u5b57\u6539\u4e3a", None))
        self.comboBox_chinese.setItemText(0, QCoreApplication.translate("Form", u"\u7b80\u4f53", None))
        self.comboBox_chinese.setItemText(1, QCoreApplication.translate("Form", u"\u7e41\u4f53", None))

        self.checkBox_character.setText(QCoreApplication.translate("Form", u"\u5b57\u7b26\u6539\u4e3a", None))
        self.comboBox_character.setItemText(0, QCoreApplication.translate("Form", u"\u534a\u89d2", None))
        self.comboBox_character.setItemText(1, QCoreApplication.translate("Form", u"\u5168\u89d2", None))

        self.checkBox_excess_spaces.setText(QCoreApplication.translate("Form", u"\u6e05\u9664\u591a\u4f59\u7a7a\u683c", None))
    # retranslateUi

