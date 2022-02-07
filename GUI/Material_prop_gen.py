# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
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

class Ui_MainWindow(object):
	def setupUi(self, MainWindow):
		MainWindow.setObjectName("MainWindow")
		MainWindow.resize(900, 680)
		self.centralWidget = QtWidgets.QWidget(MainWindow)
		self.centralWidget.setObjectName("centralWidget")
		### Parent ###
		## Parameter 1 ##
		self.P = QtWidgets.QLabel(self.centralWidget)
		self.P.setGeometry(QtCore.QRect(20, 10, 74, 18))
		self.P.setObjectName("P")
		
		self.Table_P1 = QtWidgets.QTableWidget(self.centralWidget)
		self.Table_P1.setGeometry(QtCore.QRect(30, 50, 391, 190))
		self.Table_P1.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
		self.Table_P1.setAlternatingRowColors(False)
		self.Table_P1.setShowGrid(True)
		self.Table_P1.setRowCount(0)
		self.Table_P1.setColumnCount(2)
		self.Table_P1.setObjectName("Table_P1")
		item = QtWidgets.QTableWidgetItem()
		self.Table_P1.setHorizontalHeaderItem(0, item)
		self.Table_P1.setColumnWidth(0,150)
		item = QtWidgets.QTableWidgetItem()
		self.Table_P1.setHorizontalHeaderItem(1, item)
		self.Table_P1.setColumnWidth(1,200)
		self.Table_P1.horizontalHeader().setCascadingSectionResizes(True)
		self.Table_P1.horizontalHeader().setMinimumSectionSize(32)
		
		self.button_add1 = QtWidgets.QPushButton(self.centralWidget)
		self.button_add1.setGeometry(QtCore.QRect(30, 250, 89, 25))
		self.button_add1.setObjectName("Add")
		self.button_add1.clicked.connect(self.addRow1)
		
		self.button_remove1 = QtWidgets.QPushButton(self.centralWidget)
		self.button_remove1.setGeometry(QtCore.QRect(130, 250, 89, 25))
		self.button_remove1.setObjectName("Remove")
		self.button_remove1.clicked.connect(self.removeRow1)
		
		## Parameter 2 ##
		self.P2_label = QtWidgets.QLabel(self.centralWidget)
		self.P2_label.setGeometry(QtCore.QRect(30, 310, 151, 18))
		self.P2_label.setObjectName("P2_label")
		
		self.P2 = QtWidgets.QComboBox(self.centralWidget)
		self.P2.setGeometry(QtCore.QRect(30, 330, 201, 25))
		self.P2.setObjectName("P2")
		self.P2.activated.connect(self.SelectP2)
		self.P2.addItem("")
		self.P2.addItem("")
		
		self.Table_P2 = QtWidgets.QTableWidget(self.centralWidget)
		self.Table_P2.setGeometry(QtCore.QRect(30, 370, 391, 190))
		self.Table_P2.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
		self.Table_P2.setAlternatingRowColors(False)
		self.Table_P2.setShowGrid(True)
		self.Table_P2.setRowCount(0)
		self.Table_P2.setColumnCount(2)
		self.Table_P2.setObjectName("Table_P2")
		item = QtWidgets.QTableWidgetItem()
		self.Table_P2.setHorizontalHeaderItem(0, item)
		self.Table_P2.setColumnWidth(0,150)
		item = QtWidgets.QTableWidgetItem()
		self.Table_P2.setHorizontalHeaderItem(1, item)
		self.Table_P2.setColumnWidth(1,200)
		self.Table_P2.horizontalHeader().setCascadingSectionResizes(True)
		self.Table_P2.horizontalHeader().setMinimumSectionSize(32)
		
		self.button_add2 = QtWidgets.QPushButton(self.centralWidget)
		self.button_add2.setGeometry(QtCore.QRect(30, 570, 89, 25))
		self.button_add2.setObjectName("Add")
		self.button_add2.clicked.connect(self.addRow2)
		
		self.button_remove2 = QtWidgets.QPushButton(self.centralWidget)
		self.button_remove2.setGeometry(QtCore.QRect(130, 570, 89, 25))
		self.button_remove2.setObjectName("Remove")
		self.button_remove2.clicked.connect(self.removeRow2)
		
		
		
		self.split = QtWidgets.QFrame(self.centralWidget)
		self.split.setGeometry(QtCore.QRect(436, 0, 20, 651))
		self.split.setFrameShape(QtWidgets.QFrame.VLine)
		self.split.setFrameShadow(QtWidgets.QFrame.Sunken)
		self.split.setObjectName("split")
		
		
		
		### Weld ###
		## Parameter 1 ##
		self.W = QtWidgets.QLabel(self.centralWidget)
		self.W.setGeometry(QtCore.QRect(470, 10, 74, 18))
		self.W.setObjectName("W")
		
		self.Table_W1 = QtWidgets.QTableWidget(self.centralWidget)
		self.Table_W1.setGeometry(QtCore.QRect(480, 50, 391, 190))
		self.Table_W1.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
		self.Table_W1.setAlternatingRowColors(False)
		self.Table_W1.setShowGrid(True)
		self.Table_W1.setRowCount(0)
		self.Table_W1.setColumnCount(2)
		self.Table_W1.setObjectName("Table_W1")
		item = QtWidgets.QTableWidgetItem()
		self.Table_W1.setHorizontalHeaderItem(0, item)
		self.Table_W1.setColumnWidth(0,150)
		item = QtWidgets.QTableWidgetItem()
		self.Table_W1.setHorizontalHeaderItem(1, item)
		self.Table_W1.setColumnWidth(1,200)
		self.Table_W1.horizontalHeader().setCascadingSectionResizes(True)
		self.Table_W1.horizontalHeader().setMinimumSectionSize(32)
		
		self.button_add3 = QtWidgets.QPushButton(self.centralWidget)
		self.button_add3.setGeometry(QtCore.QRect(480, 250, 89, 25))
		self.button_add3.setObjectName("Add")
		self.button_add3.clicked.connect(self.addRow3)
		
		self.button_remove3 = QtWidgets.QPushButton(self.centralWidget)
		self.button_remove3.setGeometry(QtCore.QRect(580, 250, 89, 25))
		self.button_remove3.setObjectName("Remove")
		self.button_remove3.clicked.connect(self.removeRow3)
		
		## Parameter 2 ##
		self.W2_label = QtWidgets.QLabel(self.centralWidget)
		self.W2_label.setGeometry(QtCore.QRect(480, 310, 151, 18))
		self.W2_label.setObjectName("W2_label")
		
		self.W2 = QtWidgets.QComboBox(self.centralWidget)
		self.W2.setGeometry(QtCore.QRect(480, 330, 201, 25))
		self.W2.setObjectName("W2")
		self.W2.activated.connect(self.SelectW2)
		self.W2.addItem("")
		self.W2.addItem("")
		
		self.Table_W2 = QtWidgets.QTableWidget(self.centralWidget)
		self.Table_W2.setGeometry(QtCore.QRect(480, 370, 391, 190))
		self.Table_W2.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
		self.Table_W2.setAlternatingRowColors(False)
		self.Table_W2.setShowGrid(True)
		self.Table_W2.setRowCount(0)
		self.Table_W2.setColumnCount(2)
		self.Table_W2.setObjectName("Table_W2")
		item = QtWidgets.QTableWidgetItem()
		self.Table_W2.setHorizontalHeaderItem(0, item)
		self.Table_W2.setColumnWidth(0,150)
		item = QtWidgets.QTableWidgetItem()
		self.Table_W2.setHorizontalHeaderItem(1, item)
		self.Table_W2.setColumnWidth(1,200)
		self.Table_W2.horizontalHeader().setCascadingSectionResizes(True)
		self.Table_W2.horizontalHeader().setMinimumSectionSize(32)
		
		self.button_add4 = QtWidgets.QPushButton(self.centralWidget)
		self.button_add4.setGeometry(QtCore.QRect(480, 570, 89, 25))
		self.button_add4.setObjectName("Add")
		self.button_add4.clicked.connect(self.addRow4)
		
		self.button_remove4 = QtWidgets.QPushButton(self.centralWidget)
		self.button_remove4.setGeometry(QtCore.QRect(580, 570, 89, 25))
		self.button_remove4.setObjectName("Remove")
		self.button_remove4.clicked.connect(self.removeRow4)
		
		
		
		self.finish = QtWidgets.QPushButton(self.centralWidget)
		self.finish.setGeometry(QtCore.QRect(750, 610, 95, 26))
		self.finish.setObjectName("finish")
		self.finish.clicked.connect(self.clicked)



		MainWindow.setCentralWidget(self.centralWidget)
		self.menuBar = QtWidgets.QMenuBar(MainWindow)
		self.menuBar.setGeometry(QtCore.QRect(0, 0, 678, 23))
		self.menuBar.setObjectName("menuBar")
		MainWindow.setMenuBar(self.menuBar)
		self.mainToolBar = QtWidgets.QToolBar(MainWindow)
		self.mainToolBar.setObjectName("mainToolBar")
		MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
		self.statusBar = QtWidgets.QStatusBar(MainWindow)
		self.statusBar.setObjectName("statusBar")
		MainWindow.setStatusBar(self.statusBar)

		self.retranslateUi(MainWindow)
		QtCore.QMetaObject.connectSlotsByName(MainWindow)



	def addRow1(self):
		rowCount1 = self.Table_P1.rowCount()
		self.Table_P1.insertRow(rowCount1)
		
	def removeRow1(self):
		if self.Table_P1.rowCount() > 0:
			self.Table_P1.removeRow(self.Table_P1.rowCount()-1)
			
	def addRow2(self):
		rowCount2 = self.Table_P2.rowCount()
		self.Table_P2.insertRow(rowCount2)
		_translate = QtCore.QCoreApplication.translate
		item = self.Table_P2.horizontalHeaderItem(1)
		if int(self.P2.currentIndex()) == 0:
			item.setText(_translate("MainWindow", "Thermal Diffusivity"))
		else:
			item.setText(_translate("MainWindow", "Enthalpy"))
		
	def removeRow2(self):
		if self.Table_P2.rowCount() > 0:
			self.Table_P2.removeRow(self.Table_P2.rowCount()-1)

	def SelectP2(self):
		_translate = QtCore.QCoreApplication.translate
		item = self.Table_P2.horizontalHeaderItem(1)
		if int(self.P2.currentIndex()) == 0:
			item.setText(_translate("MainWindow", "Thermal Diffusivity"))
		else:
			item.setText(_translate("MainWindow", "Enthalpy"))
		
	def addRow3(self):
		rowCount3 = self.Table_W1.rowCount()
		self.Table_W1.insertRow(rowCount3)
		
	def removeRow3(self):
		if self.Table_W1.rowCount() > 0:
			self.Table_W1.removeRow(self.Table_W1.rowCount()-1)
			
	def addRow4(self):
		rowCount4 = self.Table_W2.rowCount()
		self.Table_W2.insertRow(rowCount4)
		_translate = QtCore.QCoreApplication.translate
		item = self.Table_W2.horizontalHeaderItem(1)
		if int(self.W2.currentIndex()) == 0:
			item.setText(_translate("MainWindow", "Thermal Diffusivity"))
		else:
			item.setText(_translate("MainWindow", "Enthalpy"))
		
	def removeRow4(self):
		if self.Table_W2.rowCount() > 0:
			self.Table_W2.removeRow(self.Table_W2.rowCount()-1)

	def SelectW2(self):
		_translate = QtCore.QCoreApplication.translate
		item = self.Table_W2.horizontalHeaderItem(1)
		if int(self.W2.currentIndex()) == 0:
			item.setText(_translate("MainWindow", "Thermal Diffusivity"))
		else:
			item.setText(_translate("MainWindow", "Enthalpy"))
			
	def clicked(self):
		Parent_cond = []
		Parent_2 = []
		Weld_cond = []
		Weld_2 = []
		rowCount1 = self.Table_P1.rowCount()
		rowCount2 = self.Table_P2.rowCount()
		rowCount3 = self.Table_W1.rowCount()
		rowCount4 = self.Table_W2.rowCount()
		columnCount = 2
		for i in range(rowCount1):
			for j in range(columnCount):
				Parent_cond.append(float(self.Table_P1.item(i,j).text()))
				
		for i in range(rowCount2):
			for j in range(columnCount):
				Parent_2.append(float(self.Table_P2.item(i,j).text()))
		
		for i in range(rowCount3):
			for j in range(columnCount):
				Weld_cond.append(float(self.Table_W1.item(i,j).text()))
		
		for i in range(rowCount4):
			for j in range(columnCount):
				Weld_2.append(float(self.Table_W2.item(i,j).text()))
				
		Lines = []
		Lines.append('parent_lsa_from_GUI=' + str(Parent_cond))
		Lines.append('\n')
		if int(self.P2.currentIndex()) == 0:
			Lines.append('user_choice_parent_def=1 #diffusivity')
			Lines.append('parent_lrhocpsa_from_GUI=' + str(Parent_2))
			Lines.append('\n')
			Lines.append('\n')
		else:
			Lines.append('user_choice_parent_def=2 #enthalpy')
			Lines.append('parent_enthalpy_from_GUI=' + str(Parent_2))
			Lines.append('\n')
			Lines.append('\n')
			
		Lines.append('weld_lsa_from_GUI= ' + str(Weld_cond))
		Lines.append('\n')
		if int(self.W2.currentIndex()) == 0:
			Lines.append('user_choice_weld_def=1 #diffusivity')
			Lines.append('weld_rhocpsa_from_GUI=' + str(Weld_2))
			Lines.append('\n')
		else:
			Lines.append('user_choice_weld_def=2 #enthalpy')
			Lines.append('weld_enthalpy_from_GUI=' + str(Weld_2))
			Lines.append('\n')
		
		with open('outputs.txt', 'w') as f:
			#f.writelines(Lines)
			f.write('\n'.join(Lines))
		

	def retranslateUi(self, MainWindow):
		_translate = QtCore.QCoreApplication.translate
		MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
		
		self.P.setText(_translate("MainWindow", "Parent:"))
		item = self.Table_P1.horizontalHeaderItem(0)
		item.setText(_translate("MainWindow", "Temperature (C)"))
		item = self.Table_P1.horizontalHeaderItem(1)
		item.setText(_translate("MainWindow", "Thermal Conductivity"))
		self.button_add1.setText(_translate("MainWindow", "Add"))
		self.button_remove1.setText(_translate("MainWindow", "Remove"))
		self.P2_label.setText(_translate("MainWindow", "Second Parameter:"))
		self.P2.setItemText(0, _translate("MainWindow", "Thermal Diffusivity"))
		self.P2.setItemText(1, _translate("MainWindow", "Enthalpy"))
		item = self.Table_P2.horizontalHeaderItem(0)
		item.setText(_translate("MainWindow", "Temperature (C)"))
		item = self.Table_P2.horizontalHeaderItem(1)
		item.setText(_translate("MainWindow", "Second Parameter"))
		self.button_add2.setText(_translate("MainWindow", "Add"))
		self.button_remove2.setText(_translate("MainWindow", "Remove"))
		
		self.W.setText(_translate("MainWindow", "Weld:"))
		item = self.Table_W1.horizontalHeaderItem(0)
		item.setText(_translate("MainWindow", "Temperature (C)"))
		item = self.Table_W1.horizontalHeaderItem(1)
		item.setText(_translate("MainWindow", "Thermal Conductivity"))
		self.button_add3.setText(_translate("MainWindow", "Add"))
		self.button_remove3.setText(_translate("MainWindow", "Remove"))
		self.W2_label.setText(_translate("MainWindow", "Second Parameter:"))
		self.W2.setItemText(0, _translate("MainWindow", "Thermal Diffusivity"))
		self.W2.setItemText(1, _translate("MainWindow", "Enthalpy"))
		item = self.Table_W2.horizontalHeaderItem(0)
		item.setText(_translate("MainWindow", "Temperature (C)"))
		item = self.Table_W2.horizontalHeaderItem(1)
		item.setText(_translate("MainWindow", "Second Parameter"))
		self.button_add4.setText(_translate("MainWindow", "Add"))
		self.button_remove4.setText(_translate("MainWindow", "Remove"))
		
		self.finish.setText(_translate("MainWindow", "Submit"))


if __name__ == "__main__":
	import sys
	app = QtWidgets.QApplication(sys.argv)
	MainWindow = QtWidgets.QMainWindow()
	ui = Ui_MainWindow()
	ui.setupUi(MainWindow)
	MainWindow.show()
	sys.exit(app.exec_())

