import sys
import os
import subprocess
from PyQt5.QtWidgets import QApplication, QFileDialog, QDialog, QPlainTextEdit
from PyQt5.QtWidgets import QMainWindow
from PyQt5 import QtCore 
import inspect

from mainWB import Ui_MainWindow
from module1 import Ui_module1
from module2 import Ui_module2

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
	

	def clickpushButton(self):
		self.window = QMainWindow()
		self.ui = Ui_module1()
		self.ui.setupUi(self.window)
		self.window.show()

	def clickpushButton_2(self):
		self.window = QMainWindow()
		self.ui = Ui_module2()
		self.ui.setupUi(self.window)
		self.window.show()



	def show(self):
		self.MainWindow.show()




if __name__ == '__main__':
	app = QApplication(sys.argv)
	MainWindow = MainWindow()
	MainWindow.show()
	sys.exit(app.exec_())

