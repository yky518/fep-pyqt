# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(577, 300)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabWidget_side = QtWidgets.QTabWidget(Dialog)
        self.tabWidget_side.setTabPosition(QtWidgets.QTabWidget.West)
        self.tabWidget_side.setObjectName("tabWidget_side")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.tab)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.tabWidget_result = QtWidgets.QTabWidget(self.tab)
        self.tabWidget_result.setObjectName("tabWidget_result")
        self.verticalLayout_2.addWidget(self.tabWidget_result)
        self.tabWidget_side.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setStyleSheet("margin: 0;")
        self.tab_2.setObjectName("tab_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.tab_2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.tabWidget_project = QtWidgets.QTabWidget(self.tab_2)
        self.tabWidget_project.setObjectName("tabWidget_project")
        self.verticalLayout_3.addWidget(self.tabWidget_project)
        self.tabWidget_side.addTab(self.tab_2, "")
        self.verticalLayout.addWidget(self.tabWidget_side)

        self.retranslateUi(Dialog)
        self.tabWidget_side.setCurrentIndex(1)
        self.tabWidget_result.setCurrentIndex(-1)
        self.tabWidget_project.setCurrentIndex(-1)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.tabWidget_side.setTabText(self.tabWidget_side.indexOf(self.tab), _translate("Dialog", "Result"))
        self.tabWidget_side.setTabText(self.tabWidget_side.indexOf(self.tab_2), _translate("Dialog", "Add Project"))

