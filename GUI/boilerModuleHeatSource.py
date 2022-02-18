import sys
import os
import subprocess
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QFileDialog, QDialog, QPlainTextEdit
from PyQt5.QtWidgets import QMainWindow
from PyQt5 import QtCore 
import inspect

from module_heat_source import Ui_moduleHeatSource

class ModuleHeatSourceMainWindow:
	
	def __init__(self):
		self.settings = QtCore.QSettings('wbSettings','app7')
		print(self.settings.fileName())
		self.ModuleHeatSourceMainWindow = QMainWindow()
		self.ui = Ui_moduleHeatSource ()
		self.ui.setupUi(self.ModuleHeatSourceMainWindow)

		#Non standard template
		# Events from Stage 1
		self.ui.type.activated.connect(self.SelectType)
		self.ui.button_ok.clicked.connect(self.clicked)

	def SelectType(self):
		if int(self.ui.type.currentIndex()) == 0:
			self.ui.stackedWidget.setCurrentWidget(self.ui.goldak)
		else:
			self.ui.stackedWidget.setCurrentWidget(self.ui.ellipsoid)
			
	def clicked(self):
		Lines = []
		if int(self.ui.type.currentIndex()) == 0:
			Lines.append('gui_heat_source_type = \'GOLDAK\'' + '\n')
			Lines.append('gui_goldak_a = ' + str(self.ui.goldak_a.toPlainText().strip()) + '\n')
			Lines.append('gui_goldak_b = ' + str(self.ui.goldak_b.toPlainText().strip()) + '\n')
			Lines.append('gui_goldak_cr = ' + str(self.ui.goldak_cr.toPlainText().strip()) + '\n')
			Lines.append('gui_goldak_cf = ' + str(self.ui.goldak_cf.toPlainText().strip()) + '\n')
		else:
			Lines.append('gui_heat_source_type = \'ELLIPSOID\'' + '\n')
			Lines.append('gui_ellipsoid_a = ' + str(self.ui.ellipsoid_a.toPlainText().strip()) + '\n')
			Lines.append('gui_ellipsoid_b = ' + str(self.ui.ellipsoid_b.toPlainText().strip()) + '\n')
			Lines.append('gui_ellipsoid_c = ' + str(self.ui.ellipsoid_c.toPlainText().strip()) + '\n')
		with open('HeatSource_outputs.txt', 'w') as f:
			f.writelines(Lines)

	def show(self):
		self.ModuleHeatSourceMainWindow.show()



if __name__ == '__main__':
	app = QApplication(sys.argv)
	ModuleHeatSourceMainWindow = ModuleHeatSourceMainWindow()
	ModuleHeatSourceMainWindow.show()
	sys.exit(app.exec_())

