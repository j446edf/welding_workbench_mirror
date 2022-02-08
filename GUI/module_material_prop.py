# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'moduleMatProp.ui'
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

class Ui_moduleMatProp(object):
	def setupUi(self, moduleMatProp):
		moduleMatProp.setObjectName("moduleMatProp")
		moduleMatProp.resize(900, 680)
		self.centralWidget = QtWidgets.QWidget(moduleMatProp)
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
		#self.button_add1.clicked.connect(self.addRow1)
		
		self.button_remove1 = QtWidgets.QPushButton(self.centralWidget)
		self.button_remove1.setGeometry(QtCore.QRect(130, 250, 89, 25))
		self.button_remove1.setObjectName("Remove")
		#self.button_remove1.clicked.connect(self.removeRow1)
		
		## Parameter 2 ##
		self.P2_label = QtWidgets.QLabel(self.centralWidget)
		self.P2_label.setGeometry(QtCore.QRect(30, 310, 151, 18))
		self.P2_label.setObjectName("P2_label")
		
		self.P2 = QtWidgets.QComboBox(self.centralWidget)
		self.P2.setGeometry(QtCore.QRect(30, 330, 201, 25))
		self.P2.setObjectName("P2")
		#self.P2.activated.connect(self.SelectP2)
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
		#self.button_add2.clicked.connect(self.addRow2)
		
		self.button_remove2 = QtWidgets.QPushButton(self.centralWidget)
		self.button_remove2.setGeometry(QtCore.QRect(130, 570, 89, 25))
		self.button_remove2.setObjectName("Remove")
		#self.button_remove2.clicked.connect(self.removeRow2)
		
		
		
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
		#self.button_add3.clicked.connect(self.addRow3)
		
		self.button_remove3 = QtWidgets.QPushButton(self.centralWidget)
		self.button_remove3.setGeometry(QtCore.QRect(580, 250, 89, 25))
		self.button_remove3.setObjectName("Remove")
		#self.button_remove3.clicked.connect(self.removeRow3)
		
		## Parameter 2 ##
		self.W2_label = QtWidgets.QLabel(self.centralWidget)
		self.W2_label.setGeometry(QtCore.QRect(480, 310, 151, 18))
		self.W2_label.setObjectName("W2_label")
		
		self.W2 = QtWidgets.QComboBox(self.centralWidget)
		self.W2.setGeometry(QtCore.QRect(480, 330, 201, 25))
		self.W2.setObjectName("W2")
		#self.W2.activated.connect(self.SelectW2)
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
		#self.button_add4.clicked.connect(self.addRow4)
		
		self.button_remove4 = QtWidgets.QPushButton(self.centralWidget)
		self.button_remove4.setGeometry(QtCore.QRect(580, 570, 89, 25))
		self.button_remove4.setObjectName("Remove")
		#self.button_remove4.clicked.connect(self.removeRow4)
		
		
		
		self.finish = QtWidgets.QPushButton(self.centralWidget)
		self.finish.setGeometry(QtCore.QRect(750, 610, 95, 26))
		self.finish.setObjectName("finish")
		#self.finish.clicked.connect(self.clicked)



		moduleMatProp.setCentralWidget(self.centralWidget)
		self.menuBar = QtWidgets.QMenuBar(moduleMatProp)
		self.menuBar.setGeometry(QtCore.QRect(0, 0, 678, 23))
		self.menuBar.setObjectName("menuBar")
		moduleMatProp.setMenuBar(self.menuBar)
		self.mainToolBar = QtWidgets.QToolBar(moduleMatProp)
		self.mainToolBar.setObjectName("mainToolBar")
		moduleMatProp.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
		self.statusBar = QtWidgets.QStatusBar(moduleMatProp)
		self.statusBar.setObjectName("statusBar")
		moduleMatProp.setStatusBar(self.statusBar)

		self.retranslateUi(moduleMatProp)
		QtCore.QMetaObject.connectSlotsByName(moduleMatProp)

	def retranslateUi(self, moduleMatProp):
		_translate = QtCore.QCoreApplication.translate
		moduleMatProp.setWindowTitle(_translate("moduleMatProp", "moduleMatProp"))
		
		self.P.setText(_translate("moduleMatProp", "Parent:"))
		item = self.Table_P1.horizontalHeaderItem(0)
		item.setText(_translate("moduleMatProp", "Temperature (C)"))
		item = self.Table_P1.horizontalHeaderItem(1)
		item.setText(_translate("moduleMatProp", "Thermal Conductivity"))
		self.button_add1.setText(_translate("moduleMatProp", "Add"))
		self.button_remove1.setText(_translate("moduleMatProp", "Remove"))
		self.P2_label.setText(_translate("moduleMatProp", "Second Parameter:"))
		self.P2.setItemText(0, _translate("moduleMatProp", "Thermal Diffusivity"))
		self.P2.setItemText(1, _translate("moduleMatProp", "Enthalpy"))
		item = self.Table_P2.horizontalHeaderItem(0)
		item.setText(_translate("moduleMatProp", "Temperature (C)"))
		item = self.Table_P2.horizontalHeaderItem(1)
		item.setText(_translate("moduleMatProp", "Second Parameter"))
		self.button_add2.setText(_translate("moduleMatProp", "Add"))
		self.button_remove2.setText(_translate("moduleMatProp", "Remove"))
		
		self.W.setText(_translate("moduleMatProp", "Weld:"))
		item = self.Table_W1.horizontalHeaderItem(0)
		item.setText(_translate("moduleMatProp", "Temperature (C)"))
		item = self.Table_W1.horizontalHeaderItem(1)
		item.setText(_translate("moduleMatProp", "Thermal Conductivity"))
		self.button_add3.setText(_translate("moduleMatProp", "Add"))
		self.button_remove3.setText(_translate("moduleMatProp", "Remove"))
		self.W2_label.setText(_translate("moduleMatProp", "Second Parameter:"))
		self.W2.setItemText(0, _translate("moduleMatProp", "Thermal Diffusivity"))
		self.W2.setItemText(1, _translate("moduleMatProp", "Enthalpy"))
		item = self.Table_W2.horizontalHeaderItem(0)
		item.setText(_translate("moduleMatProp", "Temperature (C)"))
		item = self.Table_W2.horizontalHeaderItem(1)
		item.setText(_translate("moduleMatProp", "Second Parameter"))
		self.button_add4.setText(_translate("moduleMatProp", "Add"))
		self.button_remove4.setText(_translate("moduleMatProp", "Remove"))
		
		self.finish.setText(_translate("moduleMatProp", "Submit"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    moduleMatProp = QtWidgets.QMainWindow()
    ui = Ui_moduleMatProp()
    ui.setupUi(moduleMatProp)
    moduleMatProp.show()
    sys.exit(app.exec_())

