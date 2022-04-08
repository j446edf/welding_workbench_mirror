import sys
import os
import subprocess
from PyQt5.QtWidgets import QApplication, QFileDialog, QDialog, QPlainTextEdit
from PyQt5.QtWidgets import QMainWindow
from PyQt5 import QtCore 
import inspect

from module2 import Ui_module2

class Module2MainWindow:
	
	def __init__(self):
		self.settings = QtCore.QSettings('wbSettings','app1b')
		print(self.settings.fileName())
		self.Module2MainWindow = QMainWindow()
		self.ui = Ui_module2()
		self.ui.setupUi(self.Module2MainWindow)
		

	def show(self):
		self.Module2MainWindow.show()




if __name__ == '__main__':
	app = QApplication(sys.argv)
	Module2MainWindow = Module2MainWindow()
	Module2MainWindow.show()
	sys.exit(app.exec_())

