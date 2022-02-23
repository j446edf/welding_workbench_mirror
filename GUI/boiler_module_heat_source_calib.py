import sys
import os
import subprocess
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QFileDialog, QDialog, QPlainTextEdit
from PyQt5.QtWidgets import QMainWindow, QWidget
import inspect

from module_heat_source_calib import Ui_moduleHeatSourceCalib

class ModuleHeatSourceCalibMainWindow:
	
	def __init__(self):
		self.settings = QtCore.QSettings('wbSettings','app8')
		print(self.settings.fileName())
		self.ModuleHeatSourceCalibMainWindow = QMainWindow()
		self.ui = Ui_moduleHeatSourceCalib()
		self.ui.setupUi(self.ModuleHeatSourceCalibMainWindow)
		
		#Non standard template
		# Events from Stage 1
		self.ui.pushButton_8.clicked.connect(self.clicked)
	

	def clicked(self):
		#p=subprocess.Popen(["xterm","-e","./runSimConnect.sh",])
		p=subprocess.Popen(["sh","./runSimConnect.sh",])
		outputCall = p.communicate()
		self.ui.pushButton_11.setEnabled(True)
		
	
	
	def show(self):
		self.ModuleHeatSourceCalibMainWindow.show()




if __name__ == '__main__':
	app = QApplication(sys.argv)
	ModuleHeatSourceCalibMainWindow = ModuleHeatSourceCalibMainWindow()
	ModuleHeatSourceCalibMainWindow.show()
	sys.exit(app.exec_())
