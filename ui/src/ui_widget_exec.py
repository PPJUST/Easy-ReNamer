# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_widget_execyuUrNb.ui'
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
        Form.resize(257, 55)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setSpacing(3)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(3, 3, 3, 3)
        self.checkBox_auto_deal_dup = QCheckBox(Form)
        self.checkBox_auto_deal_dup.setObjectName(u"checkBox_auto_deal_dup")

        self.verticalLayout.addWidget(self.checkBox_auto_deal_dup)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(12)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButton_rename = QPushButton(Form)
        self.pushButton_rename.setObjectName(u"pushButton_rename")

        self.horizontalLayout.addWidget(self.pushButton_rename)

        self.pushButton_cancel = QPushButton(Form)
        self.pushButton_cancel.setObjectName(u"pushButton_cancel")

        self.horizontalLayout.addWidget(self.pushButton_cancel)

        self.pushButton_quit = QPushButton(Form)
        self.pushButton_quit.setObjectName(u"pushButton_quit")

        self.horizontalLayout.addWidget(self.pushButton_quit)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.checkBox_auto_deal_dup.setText(QCoreApplication.translate("Form", u"\u81ea\u52a8\u5904\u7406\u547d\u540d\u51b2\u7a81", None))
        self.pushButton_rename.setText(QCoreApplication.translate("Form", u"\u91cd\u547d\u540d", None))
        self.pushButton_cancel.setText(QCoreApplication.translate("Form", u"\u64a4\u9500", None))
        self.pushButton_quit.setText(QCoreApplication.translate("Form", u"\u9000\u51fa", None))
    # retranslateUi

