# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_widget_insertyhKFeU.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QGroupBox, QHBoxLayout,
    QLabel, QLineEdit, QSizePolicy, QSpinBox,
    QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(274, 130)
        self.verticalLayout_2 = QVBoxLayout(Form)
        self.verticalLayout_2.setSpacing(3)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(3, 3, 3, 3)
        self.groupBox = QGroupBox(Form)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout = QVBoxLayout(self.groupBox)
        self.verticalLayout.setSpacing(3)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(3, 3, 3, 3)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.checkBox_add_prefix = QCheckBox(self.groupBox)
        self.checkBox_add_prefix.setObjectName(u"checkBox_add_prefix")

        self.horizontalLayout.addWidget(self.checkBox_add_prefix)

        self.lineEdit_add_prefix = QLineEdit(self.groupBox)
        self.lineEdit_add_prefix.setObjectName(u"lineEdit_add_prefix")

        self.horizontalLayout.addWidget(self.lineEdit_add_prefix)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.checkBox_add_suffix = QCheckBox(self.groupBox)
        self.checkBox_add_suffix.setObjectName(u"checkBox_add_suffix")

        self.horizontalLayout_3.addWidget(self.checkBox_add_suffix)

        self.lineEdit_add_suffix = QLineEdit(self.groupBox)
        self.lineEdit_add_suffix.setObjectName(u"lineEdit_add_suffix")

        self.horizontalLayout_3.addWidget(self.lineEdit_add_suffix)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.checkBox_insert_index = QCheckBox(self.groupBox)
        self.checkBox_insert_index.setObjectName(u"checkBox_insert_index")

        self.horizontalLayout_4.addWidget(self.checkBox_insert_index)

        self.spinBox_index = QSpinBox(self.groupBox)
        self.spinBox_index.setObjectName(u"spinBox_index")
        self.spinBox_index.setMinimum(1)
        self.spinBox_index.setMaximum(999)

        self.horizontalLayout_4.addWidget(self.spinBox_index)

        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")

        self.horizontalLayout_4.addWidget(self.label)

        self.lineEdit_insert_character = QLineEdit(self.groupBox)
        self.lineEdit_insert_character.setObjectName(u"lineEdit_insert_character")

        self.horizontalLayout_4.addWidget(self.lineEdit_insert_character)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.checkBox_insert_index_back = QCheckBox(self.groupBox)
        self.checkBox_insert_index_back.setObjectName(u"checkBox_insert_index_back")

        self.horizontalLayout_5.addWidget(self.checkBox_insert_index_back)

        self.spinBox_index_back = QSpinBox(self.groupBox)
        self.spinBox_index_back.setObjectName(u"spinBox_index_back")
        self.spinBox_index_back.setMinimum(1)
        self.spinBox_index_back.setMaximum(999)

        self.horizontalLayout_5.addWidget(self.spinBox_index_back)

        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_5.addWidget(self.label_2)

        self.lineEdit_insert_character_back = QLineEdit(self.groupBox)
        self.lineEdit_insert_character_back.setObjectName(u"lineEdit_insert_character_back")

        self.horizontalLayout_5.addWidget(self.lineEdit_insert_character_back)


        self.verticalLayout.addLayout(self.horizontalLayout_5)


        self.verticalLayout_2.addWidget(self.groupBox)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.groupBox.setTitle(QCoreApplication.translate("Form", u"\u6dfb\u52a0", None))
        self.checkBox_add_prefix.setText(QCoreApplication.translate("Form", u"\u6587\u4ef6\u540d\u524d\u63d2\u5165", None))
        self.lineEdit_add_prefix.setPlaceholderText(QCoreApplication.translate("Form", u"\u9700\u8981\u63d2\u5165\u7684\u5b57\u7b26", None))
        self.checkBox_add_suffix.setText(QCoreApplication.translate("Form", u"\u6587\u4ef6\u540d\u540e\u6dfb\u52a0", None))
        self.lineEdit_add_suffix.setPlaceholderText(QCoreApplication.translate("Form", u"\u9700\u8981\u63d2\u5165\u7684\u5b57\u7b26", None))
        self.checkBox_insert_index.setText(QCoreApplication.translate("Form", u"\u5728\u7b2c", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u4e2a\u5b57\u7b26\u540e\u63d2\u5165", None))
        self.lineEdit_insert_character.setPlaceholderText(QCoreApplication.translate("Form", u"\u9700\u8981\u63d2\u5165\u7684\u5b57\u7b26", None))
        self.checkBox_insert_index_back.setText(QCoreApplication.translate("Form", u"\u5728\u5012\u6570\u7b2c", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"\u4e2a\u5b57\u7b26\u540e\u63d2\u5165", None))
        self.lineEdit_insert_character_back.setPlaceholderText(QCoreApplication.translate("Form", u"\u9700\u8981\u63d2\u5165\u7684\u5b57\u7b26", None))
    # retranslateUi

