import sys
import os
import subprocess
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QFileDialog, QDialog, QPlainTextEdit
from PyQt5.QtWidgets import QMainWindow
import inspect

from module_torch_param import Ui_moduleTorchParam

class ModuleTorchParamMainWindow:

	def __init__(self):
		self.settings = QtCore.QSettings('wbSettings','app6')
		print(self.settings.fileName())
		self.ModuleTorchParamMainWindow = QMainWindow()
		self.ui = Ui_moduleTorchParam ()
		self.ui.setupUi(self.ModuleTorchParamMainWindow)
		
		self.ui.button_ok.clicked.connect(self.ok)
		
	def ok(self):
		Lines = []
		ita_dec = (float(self.ui.ita.toPlainText().strip()))/100
		Lines.append('gui_weld_ita = ' + str(ita_dec) + '\n')
		Lines.append('gui_weld_I = ' + str(self.ui.i.toPlainText().strip()) + '\n')
		Lines.append('gui_weld_V = ' + str(self.ui.v.toPlainText().strip()) + '\n')

		with open('param_outputs.txt', 'w') as f:
				f.writelines(Lines)
				
	def show(self):
		self.ModuleTorchParamMainWindow.show()



if __name__ == '__main__':
	app = QApplication(sys.argv)
	ModuleTorchParamMainWindow = ModuleTorchParamMainWindow()
	ModuleTorchParamMainWindow.show()
	sys.exit(app.exec_())
