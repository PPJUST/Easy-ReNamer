# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_mainzfkvkX.ui'
##
## Created by: Qt User Interface Compiler version 6.1.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 530)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout_3 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_3.setSpacing(3)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(3, 3, 3, 3)
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab_pattern = QWidget()
        self.tab_pattern.setObjectName(u"tab_pattern")
        self.verticalLayout_2 = QVBoxLayout(self.tab_pattern)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.tabWidget.addTab(self.tab_pattern, "")
        self.tab_other = QWidget()
        self.tab_other.setObjectName(u"tab_other")
        self.verticalLayout_3 = QVBoxLayout(self.tab_other)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_place = QVBoxLayout()
        self.verticalLayout_place.setSpacing(3)
        self.verticalLayout_place.setObjectName(u"verticalLayout_place")

        self.verticalLayout_3.addLayout(self.verticalLayout_place)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.tabWidget.addTab(self.tab_other, "")

        self.horizontalLayout_3.addWidget(self.tabWidget)

        self.line_2 = QFrame(self.centralwidget)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.VLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_3.addWidget(self.line_2)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(3)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.widget_file_list = QWidget(self.centralwidget)
        self.widget_file_list.setObjectName(u"widget_file_list")
        self.horizontalLayout = QHBoxLayout(self.widget_file_list)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout.addWidget(self.widget_file_list)

        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.line)

        self.widget_exec = QWidget(self.centralwidget)
        self.widget_exec.setObjectName(u"widget_exec")
        self.horizontalLayout_2 = QHBoxLayout(self.widget_exec)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout.addWidget(self.widget_exec)

        self.verticalLayout.setStretch(0, 1)

        self.horizontalLayout_3.addLayout(self.verticalLayout)

        self.horizontalLayout_3.setStretch(0, 2)
        self.horizontalLayout_3.setStretch(2, 3)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Easy ReNamer", None))
#if QT_CONFIG(accessibility)
        self.tab_pattern.setAccessibleName("")
#endif // QT_CONFIG(accessibility)
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_pattern), QCoreApplication.translate("MainWindow", u"\u901a\u7528", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_other), QCoreApplication.translate("MainWindow", u"\u589e\u5220\u67e5\u6539", None))
    # retranslateUi

