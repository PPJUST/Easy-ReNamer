# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_widget_file_extensionUcVwoo.ui'
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
        Form.resize(174, 123)
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
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.checkBox_change_to = QCheckBox(self.groupBox)
        self.checkBox_change_to.setObjectName(u"checkBox_change_to")

        self.horizontalLayout.addWidget(self.checkBox_change_to)

        self.lineEdit_file_extension = QLineEdit(self.groupBox)
        self.lineEdit_file_extension.setObjectName(u"lineEdit_file_extension")

        self.horizontalLayout.addWidget(self.lineEdit_file_extension)

        self.horizontalLayout.setStretch(1, 1)

        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.checkBox_real_type = QCheckBox(self.groupBox)
        self.checkBox_real_type.setObjectName(u"checkBox_real_type")

        self.verticalLayout_2.addWidget(self.checkBox_real_type)

        self.checkBox_lowercase = QCheckBox(self.groupBox)
        self.checkBox_lowercase.setObjectName(u"checkBox_lowercase")

        self.verticalLayout_2.addWidget(self.checkBox_lowercase)

        self.checkBox_capital = QCheckBox(self.groupBox)
        self.checkBox_capital.setObjectName(u"checkBox_capital")

        self.verticalLayout_2.addWidget(self.checkBox_capital)


        self.verticalLayout.addWidget(self.groupBox)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.groupBox.setTitle(QCoreApplication.translate("Form", u"\u6587\u4ef6\u6269\u5c55\u540d", None))
        self.checkBox_change_to.setText(QCoreApplication.translate("Form", u"\u6269\u5c55\u540d\u6539\u4e3a", None))
        self.checkBox_real_type.setText(QCoreApplication.translate("Form", u"\u6269\u5c55\u540d\u6539\u4e3a\u771f\u5b9e\u6587\u4ef6\u7c7b\u578b*", None))
        self.checkBox_lowercase.setText(QCoreApplication.translate("Form", u"\u6269\u5c55\u540d\u6539\u4e3a\u5c0f\u5199", None))
        self.checkBox_capital.setText(QCoreApplication.translate("Form", u"\u6269\u5c55\u540d\u6539\u4e3a\u5927\u5199", None))
    # retranslateUi

