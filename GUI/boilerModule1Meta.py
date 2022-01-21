import sys
import os
import subprocess
from PyQt5.QtWidgets import QApplication, QFileDialog, QDialog, QPlainTextEdit
from PyQt5.QtWidgets import QMainWindow
from PyQt5 import QtCore 
import inspect

from module_metallurgy import Ui_moduleMeta

class ModuleMetaMainWindow:
	
	def __init__(self):
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
		
		command=[]		
		#command.append("export T_A="+str(getT_Aust)+";")
		#command.append("export T_E="+str(getT_End)+";")
		#command.append("export G_S="+str(getGS)+";")
		command.append("./basicBatchpro.sh;")
		#command.append("unset T_A;")
		#command.append("unset T_E;")
		#command.append("unset G_S;")
		command.append("$T_A;")
		command.append("$T_E;")
		command.append("$G_S;")
		command.append("$C_R;")
		command.append("$GG_M;")
		command.append("$M;")
		command.append("$A_M;")
		commandMe=""
		for i in command:
			commandMe+=i
		#print(getT_Aust)
		#print(getT_End)
		# print(getGS)
		# print(commandMe)
		#p=subprocess.Popen(["sh",commandMe], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True,env=my_env,)
		#p=subprocess.Popen(["sh",commandMe,'getT_Aust'], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True,env=my_env,)
		#proc_fb = sub.Popen(["xterm", "-e",FOLDER_Supervisor+'/runFUELBRICK_MAIN.sh',str(globals.ramFB),str(globals.mpi_or_not),str(globals.ncpusfb)])
		########p=subprocess.Popen(["sh","sudo","./basicBatchpro.sh","$T_A","$T_E","$G_S","$C_R","$GG_M","$M","$A_M"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True,env=my_env)
		p=subprocess.Popen(["xterm","-e","./basicBatchpro.sh",],env=my_env)
		#p=subprocess.Popen(["sh",commandMe], stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
		outputCall = p.communicate()
	
	
	def show(self):
		self.ModuleMetaMainWindow.show()




if __name__ == '__main__':
	app = QApplication(sys.argv)
	ModuleMetaMainWindow = ModuleMetaMainWindow()
	ModuleMetaMainWindow.show()
	sys.exit(app.exec_())

