# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_widget_replaceOSFkGr.ui'
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
        Form.resize(160, 77)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(3, 3, 3, 3)
        self.groupBox = QGroupBox(Form)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setFlat(False)
        self.groupBox.setCheckable(False)
        self.gridLayout_2 = QGridLayout(self.groupBox)
        self.gridLayout_2.setSpacing(3)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(3, 3, 3, 3)
        self.lineEdit_old_character = QLineEdit(self.groupBox)
        self.lineEdit_old_character.setObjectName(u"lineEdit_old_character")

        self.gridLayout_2.addWidget(self.lineEdit_old_character, 0, 1, 1, 1)

        self.checkBox_replace = QCheckBox(self.groupBox)
        self.checkBox_replace.setObjectName(u"checkBox_replace")
        self.checkBox_replace.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.checkBox_replace.setLayoutDirection(Qt.LeftToRight)

        self.gridLayout_2.addWidget(self.checkBox_replace, 0, 0, 1, 1)

        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setLayoutDirection(Qt.LeftToRight)
        self.label_2.setAutoFillBackground(False)
        self.label_2.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_2, 1, 0, 1, 1)

        self.lineEdit_new_character = QLineEdit(self.groupBox)
        self.lineEdit_new_character.setObjectName(u"lineEdit_new_character")

        self.gridLayout_2.addWidget(self.lineEdit_new_character, 1, 1, 1, 1)


        self.verticalLayout.addWidget(self.groupBox)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.groupBox.setTitle(QCoreApplication.translate("Form", u"\u66ff\u6362", None))
        self.checkBox_replace.setText(QCoreApplication.translate("Form", u"\u5c06\u6587\u4ef6\u540d\u4e2d\u7684", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"\u66ff\u6362\u6210", None))
    # retranslateUi

