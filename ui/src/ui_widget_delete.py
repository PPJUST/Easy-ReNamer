# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_widget_deleteVJTELg.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
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
    QLabel, QLineEdit, QSizePolicy, QSpacerItem,
    QSpinBox, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(320, 150)
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
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(3)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.checkBox_delete_character = QCheckBox(self.groupBox)
        self.checkBox_delete_character.setObjectName(u"checkBox_delete_character")

        self.horizontalLayout_2.addWidget(self.checkBox_delete_character)

        self.lineEdit_delete_character = QLineEdit(self.groupBox)
        self.lineEdit_delete_character.setObjectName(u"lineEdit_delete_character")

        self.horizontalLayout_2.addWidget(self.lineEdit_delete_character)

        self.horizontalLayout_2.setStretch(1, 1)

        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(3)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.checkBox_delete_index = QCheckBox(self.groupBox)
        self.checkBox_delete_index.setObjectName(u"checkBox_delete_index")

        self.horizontalLayout.addWidget(self.checkBox_delete_index)

        self.spinBox_index = QSpinBox(self.groupBox)
        self.spinBox_index.setObjectName(u"spinBox_index")
        self.spinBox_index.setMinimum(1)
        self.spinBox_index.setMaximum(999)

        self.horizontalLayout.addWidget(self.spinBox_index)

        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.spinBox_delete_count = QSpinBox(self.groupBox)
        self.spinBox_delete_count.setObjectName(u"spinBox_delete_count")
        self.spinBox_delete_count.setMinimum(1)
        self.spinBox_delete_count.setMaximum(999)

        self.horizontalLayout.addWidget(self.spinBox_delete_count)

        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout.addWidget(self.label_2)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setSpacing(3)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.checkBox_delete_index_back = QCheckBox(self.groupBox)
        self.checkBox_delete_index_back.setObjectName(u"checkBox_delete_index_back")

        self.horizontalLayout_6.addWidget(self.checkBox_delete_index_back)

        self.spinBox_index_back = QSpinBox(self.groupBox)
        self.spinBox_index_back.setObjectName(u"spinBox_index_back")
        self.spinBox_index_back.setMinimum(1)
        self.spinBox_index_back.setMaximum(999)

        self.horizontalLayout_6.addWidget(self.spinBox_index_back)

        self.label_6 = QLabel(self.groupBox)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_6.addWidget(self.label_6)

        self.spinBox_delete_count_back = QSpinBox(self.groupBox)
        self.spinBox_delete_count_back.setObjectName(u"spinBox_delete_count_back")
        self.spinBox_delete_count_back.setMinimum(1)
        self.spinBox_delete_count_back.setMaximum(999)

        self.horizontalLayout_6.addWidget(self.spinBox_delete_count_back)

        self.label_7 = QLabel(self.groupBox)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_6.addWidget(self.label_7)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_2)


        self.verticalLayout_2.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(3)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.checkBox_delete_index_after = QCheckBox(self.groupBox)
        self.checkBox_delete_index_after.setObjectName(u"checkBox_delete_index_after")

        self.horizontalLayout_3.addWidget(self.checkBox_delete_index_after)

        self.spinBox_index_del_after = QSpinBox(self.groupBox)
        self.spinBox_index_del_after.setObjectName(u"spinBox_index_del_after")
        self.spinBox_index_del_after.setMinimum(0)
        self.spinBox_index_del_after.setMaximum(999)

        self.horizontalLayout_3.addWidget(self.spinBox_index_del_after)

        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_3.addWidget(self.label_3)

        self.horizontalLayout_3.setStretch(2, 1)

        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setSpacing(3)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.checkBox_delete_index_after_back = QCheckBox(self.groupBox)
        self.checkBox_delete_index_after_back.setObjectName(u"checkBox_delete_index_after_back")

        self.horizontalLayout_5.addWidget(self.checkBox_delete_index_after_back)

        self.spinBox_index_del_after_back = QSpinBox(self.groupBox)
        self.spinBox_index_del_after_back.setObjectName(u"spinBox_index_del_after_back")
        self.spinBox_index_del_after_back.setMinimum(1)
        self.spinBox_index_del_after_back.setMaximum(999)

        self.horizontalLayout_5.addWidget(self.spinBox_index_del_after_back)

        self.label_5 = QLabel(self.groupBox)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_5.addWidget(self.label_5)

        self.horizontalLayout_5.setStretch(2, 1)

        self.verticalLayout_2.addLayout(self.horizontalLayout_5)


        self.verticalLayout.addWidget(self.groupBox)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.groupBox.setTitle(QCoreApplication.translate("Form", u"\u5220\u9664", None))
        self.checkBox_delete_character.setText(QCoreApplication.translate("Form", u"\u5220\u9664\u6587\u4ef6\u540d\u4e2d\u7684", None))
        self.checkBox_delete_index.setText(QCoreApplication.translate("Form", u"\u4ece\u7b2c", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u4e2a\u5b57\u7b26\u5f00\u59cb\uff0c\u5220\u9664", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"\u4e2a\u5b57\u7b26", None))
        self.checkBox_delete_index_back.setText(QCoreApplication.translate("Form", u"\u4ece\u5012\u6570\u7b2c", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"\u4e2a\u5b57\u7b26\u5f00\u59cb\uff0c\u5220\u9664", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"\u4e2a\u5b57\u7b26", None))
        self.checkBox_delete_index_after.setText(QCoreApplication.translate("Form", u"\u5220\u9664\u7b2c", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"\u4e2a\u5b57\u7b26\u540e\u7684\u5168\u90e8\u5b57\u7b26", None))
        self.checkBox_delete_index_after_back.setText(QCoreApplication.translate("Form", u"\u5220\u9664\u5012\u6570\u7b2c", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"\u4e2a\u5b57\u7b26\u540e\u7684\u5168\u90e8\u5b57\u7b26", None))
    # retranslateUi

