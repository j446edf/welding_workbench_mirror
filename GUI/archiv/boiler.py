import sys
import os
import subprocess
from PyQt5.QtWidgets import QApplication, QFileDialog, QDialog, QPlainTextEdit
from PyQt5.QtWidgets import QMainWindow
from PyQt5 import QtCore 
import inspect

from mainWB import Ui_MainWindow
#from boilerModule1Meta import ModuleMetaMainWindow
from boilerModule1 import Module1MainWindow
from boilerModule2 import Module2MainWindow

class MainWindow:
	
	def __init__(self):
		self.settings = QtCore.QSettings('wbSettings','app1')
		print(self.settings.fileName())
		self.MainWindow = QMainWindow()
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self.MainWindow)
		
		#Non standard template
		# Events from Stage 1
		self.ui.pushButton.clicked.connect(self.clickpushButton)
		self.ui.pushButton_2.clicked.connect(self.clickpushButton_2)
	

	# def clickpushButton(self):
		# print("pushed button 1")
		# self.window = QMainWindow()
		# self.window = ModuleMetaMainWindow()
		# self.window.show()

	def clickpushButton(self):
		print("pushed button 1")
		self.window1 = QMainWindow()
		self.window1 = Module1MainWindow()
		self.window1.show()

	def clickpushButton_2(self):
		print("pushed button 2")
		self.window2 = QMainWindow()
		self.window2 = Module2MainWindow()
		self.window2.show()



	def show(self):
		self.MainWindow.show()




if __name__ == '__main__':
	app = QApplication(sys.argv)
	MainWindow = MainWindow()
	MainWindow.show()
	sys.exit(app.exec_())

