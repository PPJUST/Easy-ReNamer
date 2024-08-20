# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_widget_file_listTqyBOE.ui'
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
        Form.resize(368, 309)
        self.verticalLayout_2 = QVBoxLayout(Form)
        self.verticalLayout_2.setSpacing(3)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(3, 3, 3, 3)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(3)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout__place = QVBoxLayout()
        self.verticalLayout__place.setSpacing(0)
        self.verticalLayout__place.setObjectName(u"verticalLayout__place")

        self.horizontalLayout_2.addLayout(self.verticalLayout__place)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(16)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.toolButton_move_top = QToolButton(Form)
        self.toolButton_move_top.setObjectName(u"toolButton_move_top")

        self.verticalLayout.addWidget(self.toolButton_move_top)

        self.toolButton_move_up = QToolButton(Form)
        self.toolButton_move_up.setObjectName(u"toolButton_move_up")

        self.verticalLayout.addWidget(self.toolButton_move_up)

        self.toolButton_move_down = QToolButton(Form)
        self.toolButton_move_down.setObjectName(u"toolButton_move_down")

        self.verticalLayout.addWidget(self.toolButton_move_down)

        self.toolButton_move_bottom = QToolButton(Form)
        self.toolButton_move_bottom.setObjectName(u"toolButton_move_bottom")

        self.verticalLayout.addWidget(self.toolButton_move_bottom)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)


        self.horizontalLayout_2.addLayout(self.verticalLayout)

        self.horizontalLayout_2.setStretch(0, 1)

        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(12)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.pushButton_add_file = QPushButton(Form)
        self.pushButton_add_file.setObjectName(u"pushButton_add_file")

        self.horizontalLayout.addWidget(self.pushButton_add_file)

        self.pushButton_add_folder = QPushButton(Form)
        self.pushButton_add_folder.setObjectName(u"pushButton_add_folder")

        self.horizontalLayout.addWidget(self.pushButton_add_folder)

        self.pushButton_remove = QPushButton(Form)
        self.pushButton_remove.setObjectName(u"pushButton_remove")

        self.horizontalLayout.addWidget(self.pushButton_remove)

        self.pushButton_clear = QPushButton(Form)
        self.pushButton_clear.setObjectName(u"pushButton_clear")

        self.horizontalLayout.addWidget(self.pushButton_clear)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.verticalLayout_2.addLayout(self.horizontalLayout)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.toolButton_move_top.setText(QCoreApplication.translate("Form", u"...", None))
        self.toolButton_move_up.setText(QCoreApplication.translate("Form", u"...", None))
        self.toolButton_move_down.setText(QCoreApplication.translate("Form", u"...", None))
        self.toolButton_move_bottom.setText(QCoreApplication.translate("Form", u"...", None))
        self.pushButton_add_file.setText(QCoreApplication.translate("Form", u"\u6dfb\u52a0\u6587\u4ef6", None))
        self.pushButton_add_folder.setText(QCoreApplication.translate("Form", u"\u6dfb\u52a0\u6587\u4ef6\u5939", None))
        self.pushButton_remove.setText(QCoreApplication.translate("Form", u"\u79fb\u9664", None))
        self.pushButton_clear.setText(QCoreApplication.translate("Form", u"\u6e05\u7a7a", None))
    # retranslateUi

