# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_login_dialog(object):
    def setupUi(self, login_dialog):
        login_dialog.setObjectName("login_dialog")
        login_dialog.resize(400, 300)
        self.verticalLayout = QtWidgets.QVBoxLayout(login_dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.title = QtWidgets.QLabel(login_dialog)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.title.setFont(font)
        self.title.setAlignment(QtCore.Qt.AlignCenter)
        self.title.setObjectName("title")
        self.verticalLayout.addWidget(self.title)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.usernameLabel = QtWidgets.QLabel(login_dialog)
        self.usernameLabel.setObjectName("usernameLabel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.usernameLabel)
        self.usernameLineEdit = QtWidgets.QLineEdit(login_dialog)
        self.usernameLineEdit.setObjectName("usernameLineEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.usernameLineEdit)
        self.passwordLabel = QtWidgets.QLabel(login_dialog)
        self.passwordLabel.setObjectName("passwordLabel")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.passwordLabel)
        self.passwordLineEdit = QtWidgets.QLineEdit(login_dialog)
        self.passwordLineEdit.setObjectName("passwordLineEdit")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.passwordLineEdit)
        self.configFileLabel = QtWidgets.QLabel(login_dialog)
        self.configFileLabel.setObjectName("configFileLabel")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.configFileLabel)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.config_edit = QtWidgets.QLineEdit(login_dialog)
        self.config_edit.setObjectName("config_edit")
        self.horizontalLayout.addWidget(self.config_edit)
        self.config_button = QtWidgets.QPushButton(login_dialog)
        self.config_button.setObjectName("config_button")
        self.horizontalLayout.addWidget(self.config_button)
        self.formLayout.setLayout(2, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout)
        self.verticalLayout.addLayout(self.formLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.cancel_button = QtWidgets.QPushButton(login_dialog)
        self.cancel_button.setObjectName("cancel_button")
        self.horizontalLayout_2.addWidget(self.cancel_button)
        self.login_button = QtWidgets.QPushButton(login_dialog)
        self.login_button.setObjectName("login_button")
        self.horizontalLayout_2.addWidget(self.login_button)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.configTextBrowser = QtWidgets.QTextBrowser(login_dialog)
        self.configTextBrowser.setObjectName("configTextBrowser")
        self.verticalLayout.addWidget(self.configTextBrowser)

        self.retranslateUi(login_dialog)
        QtCore.QMetaObject.connectSlotsByName(login_dialog)

    def retranslateUi(self, login_dialog):
        _translate = QtCore.QCoreApplication.translate
        login_dialog.setWindowTitle(_translate("login_dialog", "Dialog"))
        self.title.setText(_translate("login_dialog", "Log In"))
        self.usernameLabel.setText(_translate("login_dialog", "Username"))
        self.passwordLabel.setText(_translate("login_dialog", "Password"))
        self.configFileLabel.setText(_translate("login_dialog", "Config File"))
        self.config_button.setText(_translate("login_dialog", "Browse"))
        self.cancel_button.setText(_translate("login_dialog", "Reset"))
        self.login_button.setText(_translate("login_dialog", "Login"))
        self.configTextBrowser.setHtml(_translate("login_dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Config file info</p></body></html>"))

