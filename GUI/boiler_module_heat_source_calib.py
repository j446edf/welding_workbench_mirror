import sys
import os
import subprocess
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QFileDialog, QDialog, QPlainTextEdit
from PyQt5.QtWidgets import QMainWindow, QWidget
import inspect

from module_heat_source_calib import UiModuleHeatSourceCalib
from boiler_module_material_prop import ModuleMaterialPropMainWindow
from boiler_module_weld_path import ModuleWeldPathMainWindow
from boiler_module_torch_param import ModuleTorchParamMainWindow
from boiler_module_heat_source import ModuleHeatSourceMainWindow

class ModuleHeatSourceCalibMainWindow(QWidget):

    def __init__(self):
        self.settings = QtCore.QSettings('wbSettings','app8')
        print(self.settings.fileName())
        self.ModuleHeatSourceCalibMainWindow = QMainWindow()
        self.ui = UiModuleHeatSourceCalib()
        self.ui.setupUi(self.ModuleHeatSourceCalibMainWindow)

        #Non standard template
        # Events from Stage 1
        self.ui.pushButton_8.clicked.connect(self.clicked8) # <- Run Simulation
        self.ui.pushButton_2.clicked.connect(self.clicked2) # <- Load Material data
        self.ui.pushButton_3.clicked.connect(self.clicked3) # <- Specify MAterial data
        self.ui.pushButton_4.clicked.connect(self.clicked4) # <- Specify beam conditions
#        self.ui.pushButton_5.clicked.connect(self.clicked5) # <- REDUNDANT BUTTON
        self.ui.pushButton_6.clicked.connect(self.clicked6) # <- Specify input power
        self.ui.pushButton_7.clicked.connect(self.clicked7) # <- Specify heat source type


    def clicked8(self):
        #p=subprocess.Popen(["xterm","-e","./runSimConnect.sh",])
        p=subprocess.Popen(["sh","./runSimConnect.sh",])
        outputCall = p.communicate()
        self.ui.pushButton_11.setEnabled(True)
        self.ui.pushButton_10.setEnabled(True)

    def clicked2(self):
        fname,_=QFileDialog.getOpenFileName(self.ModuleHeatSourceCalibMainWindow, 'Open file', './', 'outputs.txt (*.txt)')
        print(fname)
        self.ui.pushButton_4.setEnabled(True)


    def clicked3(self):
        self.ui.ModuleMaterialPropMainWindow=ModuleMaterialPropMainWindow()
        self.ui.ModuleMaterialPropMainWindow.show()
        
        
    def clicked4(self):
        self.ui.ModuleWeldPathMainWindow=ModuleWeldPathMainWindow()
        self.ui.ModuleWeldPathMainWindow.show()
        self.ui.pushButton_6.setEnabled(True)
        
    def clicked6(self):
        self.ui.ModuleTorchParamMainWindow=ModuleTorchParamMainWindow()
        self.ui.ModuleTorchParamMainWindow.show()
        self.ui.pushButton_7.setEnabled(True)
        
    def clicked7(self):
        self.ui.ModuleHeatSourceMainWindow=ModuleHeatSourceMainWindow()
        self.ui.ModuleHeatSourceMainWindow.show()
        self.ui.pushButton_8.setEnabled(True)


    def show(self):
        self.ModuleHeatSourceCalibMainWindow.show()




if __name__ == '__main__':
    app = QApplication(sys.argv)
    ModuleHeatSourceCalibMainWindow = ModuleHeatSourceCalibMainWindow()
    ModuleHeatSourceCalibMainWindow.show()
    sys.exit(app.exec_())
