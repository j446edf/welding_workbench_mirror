import sys
import os
import subprocess
from PyQt5.QtWidgets import QApplication, QFileDialog, QDialog, QPlainTextEdit
from PyQt5.QtWidgets import QMainWindow, QWidget
from PyQt5 import QtCore 
import inspect

from delme import Ui_moduleMeta

class ModuleMetaMainWindow(QWidget):
	
	def __init__(self):
		super().__init__()
		self.settings = QtCore.QSettings('wbSettings','app3')
		print(self.settings.fileName())
		self.ModuleMetaMainWindow = QMainWindow()
		self.ui = Ui_moduleMeta()
		self.ui.setupUi(self.ModuleMetaMainWindow)
		
		#Non standard template
		# Events from Stage 1
		self.ui.Finish.clicked.connect(self.clicked)
	

	def clicked(self):
		#import globals
		getT_Aust = self.ui.T_Aust.toPlainText().strip()
		getT_End = self.ui.T_End.toPlainText().strip()
		getGS = self.ui.GS.toPlainText().strip()
		getCR = self.ui.CR.toPlainText().strip()
		getUSR = self.ui.USR.toPlainText().strip()
		
		getGGM = self.ui.GGM.currentText()
		getM = self.ui.Material.currentText()
		getAM = self.ui.AE13.currentText()
		
		my_env=os.environ.copy()
		print(my_env["PATH"])
		
		if self.ui.CCT.isChecked():
			my_env["CCT"]="Yes"
		else:
			my_env["CCT"]="No"
			
		if self.ui.TTT.isChecked():
			my_env["TTT"]="Yes"
		else:
			my_env["TTT"]="No"
		
		if getM=="USER":
			getUSR = self.ui.USR.toPlainText().strip()
			my_env["USER_M"]=getUSR
		
		my_env["T_A"]=getT_Aust
		my_env["T_E"]=getT_End
		my_env["G_S"]=getGS
		my_env["C_R"]=getCR
		
		my_env["GG_M"]=getGGM
		my_env["M"]=getM
		my_env["A_M"]=getAM
		

		print(my_env)
		p=subprocess.Popen(["xterm","-e","./basicBatchpro.sh",],env=my_env)
		outputCall = p.communicate()
	
	
	def show(self):
		self.ModuleMetaMainWindow.show()




if __name__ == '__main__':
	app = QApplication(sys.argv)
	ModuleMetaMainWindow = ModuleMetaMainWindow()
	ModuleMetaMainWindow.show()
	sys.exit(app.exec_())

