# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'preparation.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_preparation(object):
    def setupUi(self, preparation):
        preparation.setObjectName("preparation")
        preparation.setEnabled(True)
        preparation.resize(873, 611)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(preparation)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.widget = QtWidgets.QWidget(preparation)
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(self.widget)
        self.frame.setFrameShape(QtWidgets.QFrame.Box)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_5 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setItalic(True)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_2.addWidget(self.label_5)
        self.radioButton = QtWidgets.QRadioButton(self.frame)
        self.radioButton.setObjectName("radioButton")
        self.verticalLayout_2.addWidget(self.radioButton)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.project_line = QtWidgets.QLineEdit(self.frame)
        self.project_line.setObjectName("project_line")
        self.horizontalLayout_2.addWidget(self.project_line)
        self.peoject_button = QtWidgets.QPushButton(self.frame)
        self.peoject_button.setObjectName("peoject_button")
        self.horizontalLayout_2.addWidget(self.peoject_button)
        self.horizontalLayout_2.setStretch(0, 1)
        self.horizontalLayout_2.setStretch(1, 2)
        self.horizontalLayout_2.setStretch(2, 1)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.radioButton_2 = QtWidgets.QRadioButton(self.frame)
        self.radioButton_2.setObjectName("radioButton_2")
        self.verticalLayout_2.addWidget(self.radioButton_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_3.addWidget(self.label_2)
        self.job_line = QtWidgets.QLineEdit(self.frame)
        self.job_line.setObjectName("job_line")
        self.horizontalLayout_3.addWidget(self.job_line)
        self.job_button = QtWidgets.QPushButton(self.frame)
        self.job_button.setObjectName("job_button")
        self.horizontalLayout_3.addWidget(self.job_button)
        self.horizontalLayout_3.setStretch(0, 1)
        self.horizontalLayout_3.setStretch(1, 2)
        self.horizontalLayout_3.setStretch(2, 1)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.verticalLayout.addWidget(self.frame)
        self.frame_3 = QtWidgets.QFrame(self.widget)
        self.frame_3.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_6 = QtWidgets.QLabel(self.frame_3)
        font = QtGui.QFont()
        font.setItalic(True)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_3.addWidget(self.label_6)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_3 = QtWidgets.QLabel(self.frame_3)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_4.addWidget(self.label_3)
        self.protein_file = QtWidgets.QLineEdit(self.frame_3)
        self.protein_file.setObjectName("protein_file")
        self.horizontalLayout_4.addWidget(self.protein_file)
        self.protein_button = QtWidgets.QPushButton(self.frame_3)
        self.protein_button.setObjectName("protein_button")
        self.horizontalLayout_4.addWidget(self.protein_button)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_4 = QtWidgets.QLabel(self.frame_3)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_5.addWidget(self.label_4)
        self.unprepare_button = QtWidgets.QPushButton(self.frame_3)
        self.unprepare_button.setObjectName("unprepare_button")
        self.horizontalLayout_5.addWidget(self.unprepare_button)
        self.verticalLayout_3.addLayout(self.horizontalLayout_5)
        self.verticalLayout.addWidget(self.frame_3)
        self.frame_4 = QtWidgets.QFrame(self.widget)
        self.frame_4.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_4)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_7 = QtWidgets.QLabel(self.frame_4)
        font = QtGui.QFont()
        font.setItalic(True)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_4.addWidget(self.label_7)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_8 = QtWidgets.QLabel(self.frame_4)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_6.addWidget(self.label_8)
        self.ligand_button = QtWidgets.QPushButton(self.frame_4)
        self.ligand_button.setObjectName("ligand_button")
        self.horizontalLayout_6.addWidget(self.ligand_button)
        self.horizontalLayout_6.setStretch(0, 1)
        self.horizontalLayout_6.setStretch(1, 1)
        self.verticalLayout_4.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_10 = QtWidgets.QLabel(self.frame_4)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_8.addWidget(self.label_10)
        self.affinity_line = QtWidgets.QLineEdit(self.frame_4)
        self.affinity_line.setObjectName("affinity_line")
        self.horizontalLayout_8.addWidget(self.affinity_line)
        self.button_dGImport = QtWidgets.QPushButton(self.frame_4)
        self.button_dGImport.setObjectName("button_dGImport")
        self.horizontalLayout_8.addWidget(self.button_dGImport)
        self.horizontalLayout_8.setStretch(0, 1)
        self.horizontalLayout_8.setStretch(1, 2)
        self.horizontalLayout_8.setStretch(2, 1)
        self.verticalLayout_4.addLayout(self.horizontalLayout_8)
        self.verticalLayout.addWidget(self.frame_4)
        self.frame_5 = QtWidgets.QFrame(self.widget)
        self.frame_5.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame_5)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_9 = QtWidgets.QLabel(self.frame_5)
        font = QtGui.QFont()
        font.setItalic(True)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_5.addWidget(self.label_9)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_11 = QtWidgets.QLabel(self.frame_5)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_9.addWidget(self.label_11)
        self.label_13 = QtWidgets.QLabel(self.frame_5)
        self.label_13.setObjectName("label_13")
        self.horizontalLayout_9.addWidget(self.label_13)
        self.horizontalLayout_9.setStretch(0, 1)
        self.verticalLayout_5.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_12 = QtWidgets.QLabel(self.frame_5)
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_10.addWidget(self.label_12)
        self.align_box = QtWidgets.QComboBox(self.frame_5)
        self.align_box.setObjectName("align_box")
        self.align_box.addItem("")
        self.align_box.addItem("")
        self.horizontalLayout_10.addWidget(self.align_box)
        self.horizontalLayout_10.setStretch(0, 1)
        self.horizontalLayout_10.setStretch(1, 1)
        self.verticalLayout_5.addLayout(self.horizontalLayout_10)
        self.hermite_button = QtWidgets.QPushButton(self.frame_5)
        self.hermite_button.setObjectName("hermite_button")
        self.verticalLayout_5.addWidget(self.hermite_button)
        self.label_14 = QtWidgets.QLabel(self.frame_5)
        self.label_14.setAlignment(QtCore.Qt.AlignCenter)
        self.label_14.setObjectName("label_14")
        self.verticalLayout_5.addWidget(self.label_14)
        self.verticalLayout.addWidget(self.frame_5)
        self.horizontalLayout_11.addWidget(self.widget)
        self.right_panel = QtWidgets.QWidget(preparation)
        self.right_panel.setObjectName("right_panel")
        self.table_layout = QtWidgets.QVBoxLayout(self.right_panel)
        self.table_layout.setObjectName("table_layout")
        self.horizontalLayout_11.addWidget(self.right_panel)
        self.horizontalLayout_11.setStretch(0, 1)
        self.horizontalLayout_11.setStretch(1, 1)
        self.verticalLayout_6.addLayout(self.horizontalLayout_11)
        self.button_next_prep = QtWidgets.QPushButton(preparation)
        self.button_next_prep.setObjectName("button_next_prep")
        self.verticalLayout_6.addWidget(self.button_next_prep)

        self.retranslateUi(preparation)
        QtCore.QMetaObject.connectSlotsByName(preparation)

    def retranslateUi(self, preparation):
        _translate = QtCore.QCoreApplication.translate
        preparation.setWindowTitle(_translate("preparation", "Form"))
        self.label_5.setText(_translate("preparation", "Load Project"))
        self.radioButton.setText(_translate("preparation", "Load Project"))
        self.label.setText(_translate("preparation", "Project Dir"))
        self.peoject_button.setText(_translate("preparation", "Browse"))
        self.radioButton_2.setText(_translate("preparation", "Create a New Project"))
        self.label_2.setText(_translate("preparation", "Job Dir"))
        self.job_button.setText(_translate("preparation", "Browse"))
        self.label_6.setText(_translate("preparation", "Load Protein"))
        self.label_3.setText(_translate("preparation", "Portein File"))
        self.protein_button.setText(_translate("preparation", "Browse"))
        self.label_4.setText(_translate("preparation", "If the protein is upprepared, you can do:"))
        self.unprepare_button.setText(_translate("preparation", "Protein Preparation"))
        self.label_7.setText(_translate("preparation", "Load Ligands"))
        self.label_8.setText(_translate("preparation", "Lignad Files"))
        self.ligand_button.setText(_translate("preparation", "Browse"))
        self.label_10.setText(_translate("preparation", "Affinity Data"))
        self.button_dGImport.setText(_translate("preparation", "Browse"))
        self.label_9.setText(_translate("preparation", "Alignment"))
        self.label_11.setText(_translate("preparation", "Identify Crystal Structures"))
        self.label_13.setText(_translate("preparation", "Please identify on the right"))
        self.label_12.setText(_translate("preparation", "Ligand Alignment"))
        self.align_box.setItemText(0, _translate("preparation", "Constrained Docking"))
        self.align_box.setItemText(1, _translate("preparation", "None"))
        self.hermite_button.setText(_translate("preparation", "Align and Show on Hermite"))
        self.label_14.setText(_translate("preparation", "If you are not satisfied with the result, \n"
"you can do overlay one more time."))
        self.button_next_prep.setText(_translate("preparation", "Next->"))

