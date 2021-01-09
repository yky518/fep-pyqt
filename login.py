# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MyLogin(object):
    def setupUi(self, MyLogin):
        MyLogin.setObjectName("MyLogin")
        MyLogin.resize(1053, 690)
        self.horizontalLayout = QtWidgets.QHBoxLayout(MyLogin)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.widget = QtWidgets.QWidget(MyLogin)
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.usernameLabel = QtWidgets.QLabel(self.widget)
        self.usernameLabel.setObjectName("usernameLabel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.usernameLabel)
        self.usernameLineEdit = QtWidgets.QLineEdit(self.widget)
        self.usernameLineEdit.setObjectName("usernameLineEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.usernameLineEdit)
        self.configFileLabel = QtWidgets.QLabel(self.widget)
        self.configFileLabel.setObjectName("configFileLabel")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.configFileLabel)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.lineEdit = QtWidgets.QLineEdit(self.widget)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_2.addWidget(self.lineEdit)
        self.pushButton_2 = QtWidgets.QPushButton(self.widget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_2.addWidget(self.pushButton_2)
        self.formLayout.setLayout(1, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_2)
        self.verticalLayout.addLayout(self.formLayout)
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.textBrowser = QtWidgets.QTextBrowser(self.widget)
        self.textBrowser.setObjectName("textBrowser")
        self.verticalLayout.addWidget(self.textBrowser)
        self.horizontalLayout.addWidget(self.widget)
        self.tableWidget_job = QtWidgets.QTableWidget(MyLogin)
        self.tableWidget_job.setObjectName("tableWidget_job")
        self.tableWidget_job.setColumnCount(7)
        self.tableWidget_job.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_job.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_job.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_job.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_job.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_job.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_job.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_job.setHorizontalHeaderItem(6, item)
        self.tableWidget_job.horizontalHeader().setCascadingSectionResizes(True)
        self.horizontalLayout.addWidget(self.tableWidget_job)

        self.retranslateUi(MyLogin)
        QtCore.QMetaObject.connectSlotsByName(MyLogin)

    def retranslateUi(self, MyLogin):
        _translate = QtCore.QCoreApplication.translate
        MyLogin.setWindowTitle(_translate("MyLogin", "Form"))
        self.usernameLabel.setText(_translate("MyLogin", "Username"))
        self.configFileLabel.setText(_translate("MyLogin", "Config File"))
        self.pushButton_2.setText(_translate("MyLogin", "Browse"))
        self.pushButton.setText(_translate("MyLogin", "Login"))
        self.textBrowser.setHtml(_translate("MyLogin", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Config file info</p></body></html>"))
        item = self.tableWidget_job.horizontalHeaderItem(0)
        item.setText(_translate("MyLogin", "JobID"))
        item = self.tableWidget_job.horizontalHeaderItem(1)
        item.setText(_translate("MyLogin", "JobName"))
        item = self.tableWidget_job.horizontalHeaderItem(2)
        item.setText(_translate("MyLogin", "Process"))
        item = self.tableWidget_job.horizontalHeaderItem(3)
        item.setText(_translate("MyLogin", "Running Time"))
        item = self.tableWidget_job.horizontalHeaderItem(4)
        item.setText(_translate("MyLogin", "Cost"))
        item = self.tableWidget_job.horizontalHeaderItem(5)
        item.setText(_translate("MyLogin", "Status"))
        item = self.tableWidget_job.horizontalHeaderItem(6)
        item.setText(_translate("MyLogin", "Ops"))

