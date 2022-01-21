# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CCTgenerator/CCTgenerator.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!
import sys
import os
import subprocess
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QFileDialog, QDialog, QPlainTextEdit
from PyQt5.QtWidgets import QMainWindow
import inspect

class Ui_moduleMeta(object):
	def setupUi(self, moduleMeta):
		moduleMeta.setObjectName("moduleMeta")
		moduleMeta.resize(639, 701)
		self.centralWidget = QtWidgets.QWidget(moduleMeta)
		self.centralWidget.setObjectName("centralWidget")
		self.Inputs_label = QtWidgets.QLabel(self.centralWidget)
		self.Inputs_label.setGeometry(QtCore.QRect(10, 10, 81, 21))
		font = QtGui.QFont()
		font.setPointSize(14)
		self.Inputs_label.setFont(font)
		self.Inputs_label.setObjectName("Inputs_label")
		self.T_Aust = QtWidgets.QTextEdit(self.centralWidget)
		self.T_Aust.setGeometry(QtCore.QRect(280, 40, 51, 31))
		self.T_Aust.setObjectName("T_Aust")
		self.T_End = QtWidgets.QTextEdit(self.centralWidget)
		self.T_End.setGeometry(QtCore.QRect(280, 80, 51, 31))
		self.T_End.setObjectName("T_End")
		self.GS = QtWidgets.QTextEdit(self.centralWidget)
		self.GS.setGeometry(QtCore.QRect(280, 120, 51, 31))
		self.GS.setObjectName("GS")
		self.AustT_label = QtWidgets.QLabel(self.centralWidget)
		self.AustT_label.setGeometry(QtCore.QRect(20, 50, 281, 17))
		self.AustT_label.setObjectName("AustT_label")
		self.EndT_label = QtWidgets.QLabel(self.centralWidget)
		self.EndT_label.setGeometry(QtCore.QRect(20, 90, 191, 17))
		self.EndT_label.setObjectName("EndT_label")
		self.GS_label = QtWidgets.QLabel(self.centralWidget)
		self.GS_label.setGeometry(QtCore.QRect(20, 130, 121, 17))
		self.GS_label.setObjectName("GS_label")
		self.CR_label = QtWidgets.QLabel(self.centralWidget)
		self.CR_label.setGeometry(QtCore.QRect(20, 170, 211, 17))
		self.CR_label.setObjectName("CR_label")
		self.CR = QtWidgets.QTextEdit(self.centralWidget)
		self.CR.setGeometry(QtCore.QRect(280, 170, 331, 41))
		self.CR.setObjectName("CR")
		self.GGM_label = QtWidgets.QLabel(self.centralWidget)
		self.GGM_label.setGeometry(QtCore.QRect(20, 240, 151, 17))
		self.GGM_label.setObjectName("GGM_label")
		self.GGM = QtWidgets.QComboBox(self.centralWidget)
		self.GGM.setGeometry(QtCore.QRect(280, 230, 121, 25))
		self.GGM.setObjectName("GGM")
		self.GGM.addItem("")
		self.GGM.addItem("")
		self.GGM.addItem("")
		self.Material_label = QtWidgets.QLabel(self.centralWidget)
		self.Material_label.setGeometry(QtCore.QRect(20, 280, 71, 17))
		self.Material_label.setObjectName("Material_label")
		self.Material = QtWidgets.QComboBox(self.centralWidget)
		self.Material.setGeometry(QtCore.QRect(280, 270, 121, 25))
		self.Material.setObjectName("Material")
		self.Material.addItem("")
		self.Material.addItem("")
		self.Material.addItem("")
		self.Material.addItem("")
		self.AE13 = QtWidgets.QComboBox(self.centralWidget)
		self.AE13.setGeometry(QtCore.QRect(280, 450, 121, 25))
		self.AE13.setObjectName("AE13")
		self.AE13.addItem("")
		self.AE13.addItem("")
		self.AE13.addItem("")
		self.AE13_label = QtWidgets.QLabel(self.centralWidget)
		self.AE13_label.setGeometry(QtCore.QRect(20, 460, 101, 17))
		self.AE13_label.setObjectName("AE13_label")
		
		self.Finish = QtWidgets.QPushButton(self.centralWidget)
		self.Finish.setGeometry(QtCore.QRect(540, 600, 89, 25))
		self.Finish.setObjectName("Finish")
		#self.Finish.clicked.connect(self.clicked)
		
		self.CCT = QtWidgets.QCheckBox(self.centralWidget)
		self.CCT.setGeometry(QtCore.QRect(80, 560, 92, 23))
		self.CCT.setObjectName("CCT")
		
		self.TTT = QtWidgets.QCheckBox(self.centralWidget)
		self.TTT.setGeometry(QtCore.QRect(310, 560, 92, 23))
		self.TTT.setObjectName("TTT")
		
		self.Plots_label = QtWidgets.QLabel(self.centralWidget)
		self.Plots_label.setGeometry(QtCore.QRect(20, 500, 81, 21))
		font = QtGui.QFont()
		font.setPointSize(14)
		self.Plots_label.setFont(font)
		self.Plots_label.setObjectName("Plots_label")
		self.Plots_explanation = QtWidgets.QLabel(self.centralWidget)
		self.Plots_explanation.setGeometry(QtCore.QRect(20, 530, 361, 17))
		self.Plots_explanation.setObjectName("Plots_explanation")
		
		self.Material_label_2 = QtWidgets.QLabel(self.centralWidget)
		self.Material_label_2.setGeometry(QtCore.QRect(90, 310, 381, 71))
		self.Material_label_2.setObjectName("Material_label_2")
		self.USR = QtWidgets.QTextEdit(self.centralWidget)
		self.USR.setGeometry(QtCore.QRect(280, 390, 331, 41))
		self.USR.setObjectName("USR")
		self.Material_label_3 = QtWidgets.QLabel(self.centralWidget)
		self.Material_label_3.setGeometry(QtCore.QRect(90, 400, 161, 16))
		self.Material_label_3.setObjectName("Material_label_3")
		
		moduleMeta.setCentralWidget(self.centralWidget)
		self.menuBar = QtWidgets.QMenuBar(moduleMeta)
		self.menuBar.setGeometry(QtCore.QRect(0, 0, 639, 22))
		self.menuBar.setObjectName("menuBar")
		moduleMeta.setMenuBar(self.menuBar)
		self.mainToolBar = QtWidgets.QToolBar(moduleMeta)
		self.mainToolBar.setObjectName("mainToolBar")
		moduleMeta.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
		self.statusBar = QtWidgets.QStatusBar(moduleMeta)
		self.statusBar.setObjectName("statusBar")
		moduleMeta.setStatusBar(self.statusBar)

		self.retranslateUi(moduleMeta)
		QtCore.QMetaObject.connectSlotsByName(moduleMeta)
		
	

	def retranslateUi(self, moduleMeta):
		_translate = QtCore.QCoreApplication.translate
		moduleMeta.setWindowTitle(_translate("moduleMeta", "CCT Generator"))
		self.Inputs_label.setText(_translate("moduleMeta", "Inputs:"))
		self.AustT_label.setText(_translate("moduleMeta", "Austenisation temperature (Celsius):"))
		self.EndT_label.setText(_translate("moduleMeta", "End temperature (Celsius):"))
		self.GS_label.setText(_translate("moduleMeta", "Grain size (mm):"))
		self.CR_label.setText(_translate("moduleMeta", "Cooling rates  (0.1, 0.2, 0.3, etc):"))
		self.GGM_label.setText(_translate("moduleMeta", "Grain growth method:"))
		self.GGM.setItemText(0, _translate("moduleMeta", "IKAWA"))
		self.GGM.setItemText(1, _translate("moduleMeta", "CONSTANT"))
		self.GGM.setItemText(2, _translate("moduleMeta", "TWORATE"))
		self.Material_label.setText(_translate("moduleMeta", "Material:"))
		self.Material.setItemText(0, _translate("moduleMeta", "SA508"))
		self.Material.setItemText(1, _translate("moduleMeta", "4140"))
		self.Material.setItemText(2, _translate("moduleMeta", "16MND5"))
		self.Material.setItemText(3, _translate("moduleMeta", "USER"))
		self.AE13.setItemText(0, _translate("moduleMeta", "Grange"))
		self.AE13.setItemText(1, _translate("moduleMeta", "Andrews"))
		self.AE13.setItemText(2, _translate("moduleMeta", "Eldis"))
		self.AE13_label.setText(_translate("moduleMeta", "AE13 method:"))
		self.Finish.setText(_translate("moduleMeta", "Submit"))
		self.CCT.setText(_translate("moduleMeta", "CCT"))
		self.TTT.setText(_translate("moduleMeta", "TTT"))
		self.Plots_label.setText(_translate("moduleMeta", "Plots:"))
		self.Plots_explanation.setText(_translate("moduleMeta", "Selected which plots you would like to be produced"))
		self.Material_label_2.setText(_translate("moduleMeta", "<html><head/><body><p>User-defined Material:<br/>(Your composition must be inputted in this format and<br/>contain these chemical elements in the following order: <br/>[C, Mn, Si, Ni, Cr, Mo, V, W, Cu, P, Al, As, Ti, Co])</p></body></html>"))
		self.Material_label_3.setText(_translate("moduleMeta", "User-defined Material:"))		
			


if __name__ == "__main__":
	import sys
	app = QtWidgets.QApplication(sys.argv)
	moduleMeta = QtWidgets.QMainWindow()
	ui = Ui_moduleMeta()
	ui.setupUi(moduleMeta)
	moduleMeta.show()
	sys.exit(app.exec_())


