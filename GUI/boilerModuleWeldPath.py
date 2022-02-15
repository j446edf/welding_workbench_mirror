import sys
import os
import subprocess
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QFileDialog, QDialog, QPlainTextEdit
from PyQt5.QtWidgets import QMainWindow
import inspect

from module_weld_path import Ui_moduleWeldPath

class ModuleWeldPathMainWindow:
	
	def __init__(self):
		self.settings = QtCore.QSettings('wbSettings','app5')
		print(self.settings.fileName())
		self.ModuleWeldPathMainWindow = QMainWindow()
		self.ui = Ui_moduleWeldPath ()
		self.ui.setupUi(self.ModuleWeldPathMainWindow)

		self.ui.v_t_addRow_button.clicked.connect(self.addRow1)

		self.ui.v_t_removeRow_button.clicked.connect(self.removeRow1)

		self.ui.path_addRow_button.clicked.connect(self.addRow2)

		self.ui.path_removeRow_button.clicked.connect(self.removeRow2)

		#self.ui.button_apply.clicked.connect(self.apply)

		self.ui.button_ok.clicked.connect(self.ok)
		
	def addRow1(self):
		rowCount1 = self.ui.v_t_table.rowCount()
		self.ui.v_t_table.insertRow(rowCount1)

	def removeRow1(self):
		if self.ui.v_t_table.rowCount() > 0:
			self.ui.v_t_table.removeRow(self.ui.v_t_table.rowCount()-1)
			
	def addRow2(self):
		rowCount2 = self.ui.path_table.rowCount()
		self.ui.path_table.insertRow(rowCount2)

	def removeRow2(self):
		if self.ui.path_table.rowCount() > 0:
			self.ui.path_table.removeRow(self.ui.path_table.rowCount()-1)
			
	def ok(self):
		Lines = []
		dsdt = []
		beam = []
		path = []
		normals = []
		dir0 = []
		rowCount1 = self.ui.v_t_table.rowCount()
		rowCount2 = self.ui.path_table.rowCount()
		columnCount1 = 2
		columnCount2 = 3
		end = 0
		
		for i in range(rowCount1):
			if self.ui.v_t_table.item(i,0) and self.ui.v_t_table.item(i,0).text():
				if self.ui.v_t_table.item(i,1) and self.ui.v_t_table.item(i,1).text():
					for j in range(columnCount1):
						dsdt.append(float(self.ui.v_t_table.item(i,j).text()))
				else:
					print("Cell empty --> Next row")	
			else:
				print("Cell empty --> Next row")
		if not dsdt:
			Lines.append('gui_torch_dsdt=[[ ]]' + '\n' + '\n')
		else:
			end = float(dsdt[len(dsdt)-2])
			Lines.append('gui_torch_dsdt=[[ ' + str(dsdt[0]) + ' ,  ' + str(dsdt[1]) + ' ]')
			for i in range((len(dsdt)/2)-1):
				Lines.append(',' + '\n' + '   [ ' + str(dsdt[2*i+2]) + ' ,  ' + str(dsdt[2*i+3]) + ' ]')
			Lines.append(']' + '\n' + '\n')
			
		if str(self.ui.beam_on.toPlainText().strip()) is '':
			Lines.append('gui_torch_beam=[[ ]]' + '\n' + '\n')
		elif str(self.ui.beam_off.toPlainText().strip()) is '':
			Lines.append('gui_torch_beam=[[ ]]' + '\n' + '\n')
		else:
			b_on = float(self.ui.beam_on.toPlainText().strip())
			b_off = float(self.ui.beam_off.toPlainText().strip())
			beam = [0., 0., (b_on-0.01), 0., b_on, 1., b_off, 1., (b_off+0.01), 0, end, 0.]
			Lines.append('gui_torch_beam=[[ ' + str(beam[0]) + ' ,  ' + str(beam[1]) + ' ]')
			for i in range(5):
				Lines.append(',' + '\n' + '   [ ' + str(beam[2*i+2]) + ' ,  ' + str(beam[2*i+3]) + ' ]')
			Lines.append(']' + '\n' + '\n')
		
		for i in range(rowCount2):
			if self.ui.path_table.item(i,0) and self.ui.path_table.item(i,0).text():
				if self.ui.path_table.item(i,1) and self.ui.path_table.item(i,1).text():
					if self.ui.path_table.item(i,2) and self.ui.path_table.item(i,2).text():
						for j in range(columnCount2):
							path.append(float(self.ui.path_table.item(i,j).text()))
					else:
						print("Cell empty --> Next row")
				else:
					print("Cell empty --> Next row")	
			else:
				print("Cell empty --> Next row")
		if not path:
			Lines.append('gui_torch_path_torch=[[ ]]' + '\n' + '\n')
		else:
			Lines.append('gui_torch_path_torch=[[ ' + str(path[0]) + ' ,  ' + str(path[1]) + ' ,  ' + str(path[2]) + ' ]')
			for i in range((len(path)/3)-1):
				Lines.append(',' + '\n' + '   [ ' + str(path[(3*i)+3]) + ' ,  ' + str(path[(3*i)+4]) + ' ,  ' + str(path[(3*i)+5]) + ' ]')
			Lines.append(']' + '\n' + '\n')
		
		for i in range(rowCount2):
			if self.ui.path_table.item(i,3) and self.ui.path_table.item(i,3).text():
				if self.ui.path_table.item(i,4) and self.ui.path_table.item(i,4).text():
					if self.ui.path_table.item(i,5) and self.ui.path_table.item(i,5).text():
						for j in range(columnCount2):
							normals.append(float(self.ui.path_table.item(i,j+3).text()))
					else:
						print("Cell empty --> Next row")
				else:
					print("Cell empty --> Next row")	
			else:
				print("Cell empty --> Next row")
		if not path:
			Lines.append('gui_torch_pathNormals_torch=[[ ]]' + '\n' + '\n')
		else:
			Lines.append('gui_torch_pathNormals_torch=[[ ' + str(normals[0]) + ' ,  ' + str(normals[1]) + ' ,  ' + str(normals[2]) + ' ]')
			for i in range((len(normals)/3)-1):
				Lines.append(',' + '\n' + '   [ ' + str(normals[(3*i)+3]) + ' ,  ' + str(normals[(3*i)+4]) + ' ,  ' + str(normals[(3*i)+5]) + ' ]')
			Lines.append(']' + '\n' + '\n')
		
		if str(self.ui.dirx0.toPlainText().strip()) is '':
			Lines.append('gui_torch_dir0=[[ ]]' + '\n' + '\n')
		elif str(self.ui.diry0.toPlainText().strip()) is '':
			Lines.append('gui_torch_dir0=[[ ]]' + '\n' + '\n')
		elif str(self.ui.dirz0.toPlainText().strip()) is '':
			Lines.append('gui_torch_dir0=[[ ]]' + '\n' + '\n')
		else:
			dir0.append(float(self.ui.dirx0.toPlainText().strip()))
			dir0.append(float(self.ui.diry0.toPlainText().strip()))
			dir0.append(float(self.ui.dirz0.toPlainText().strip()))
			Lines.append("gui_torch_dir0=["+repr(dir0)+"]")
		
		with open('path_outputs.txt', 'w') as f:
			f.writelines(Lines)

		
	def show(self):
		self.ModuleWeldPathMainWindow.show()



if __name__ == '__main__':
	app = QApplication(sys.argv)
	ModuleWeldPathMainWindow = ModuleWeldPathMainWindow()
	ModuleWeldPathMainWindow.show()
	sys.exit(app.exec_())
