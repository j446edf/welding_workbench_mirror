import sys
import os
import subprocess
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QFileDialog, QDialog, QPlainTextEdit
from PyQt5.QtWidgets import QMainWindow, QWidget
import inspect

from module_main_workflow import UiModuleMainWorkflow
from boiler_module_meshing import ModuleMeshingMainWindow
from boiler_module_heat_source_calib import ModuleHeatSourceCalibMainWindow
pathToWorkbench=os.getenv('USER_WELDWB_srcDir')
pathToMeshing=pathToWorkbench+'/meshing'
pathToResults=pathToWorkbench+'/simulation/tmp'
#print("the path is " + pathToWorkbench)
#modelGeom=os.getenv('USER_INP_GEOM')
#resuFile=os.getenv('USER_INP_RESU_FILE')

class ModuleMainWorkflowMainWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.settings = QtCore.QSettings('wbSettings','app8')
        print(self.settings.fileName())
        self.ModuleMainWorkflowMainWindow = QMainWindow()
        self.ui = UiModuleMainWorkflow()
        self.ui.setupUi(self.ModuleMainWorkflowMainWindow)
        
        self.ui.pushButton_2.clicked.connect(self.clicked2) # <- Mesh module
        self.ui.pushButton_5.clicked.connect(self.clicked5) # <- Load Mesh
        self.ui.pushButton_4.clicked.connect(self.clicked4) # <- Heat Source Module
        self.ui.pushButton_8.clicked.connect(self.clicked8) # <- Load heat source results
        
    def clicked2(self):
        self.ui.ModuleMeshingMainWindow=ModuleMeshingMainWindow()
        self.ui.ModuleMeshingMainWindow.show()
        self.ui.pushButton_4.setEnabled(True)
        self.ui.pushButton_8.setEnabled(True)
        #modelGeom=os.getenv('USER_INP_GEOM')
        modelGeom = "0"
        if modelGeom == "0":
            model = str("/meshing/Edge_Welded_Beam_fromGUI.med")
        elif modelGeom == "1":
            model = str("/meshing/TG9_fromGUI.med")
        else:
            model = str("/meshing/Tekken_fromGUI.med")
        pathToModel = pathToWorkbench+model
        self.ui.label_19.setText(pathToModel)
        
    def clicked5(self):
        fname,_=QFileDialog.getOpenFileName(self.ModuleMainWorkflowMainWindow, 'Load Weld Model', pathToMeshing, '(*.med)')
        print(fname)
        fname = str(fname)
        self.ui.label_19.setText(fname)
        my_env = os.environ.copy()
        my_env["model"] = fname
        p=subprocess.Popen(["sh","./modifyExportLoadMesh.sh",],env=my_env)
        outputCall = p.communicate()
        self.ui.pushButton_4.setEnabled(True)
        self.ui.pushButton_8.setEnabled(True)

    def clicked4(self):
        self.ui.ModuleHeatSourceCalibMainWindow=ModuleHeatSourceCalibMainWindow()
        self.ui.ModuleHeatSourceCalibMainWindow.show()
        #self.ui.label_19.setText(resuFile)
        
    def clicked8(self):
        #fname,_=QFileDialog.getOpenFileName(self.ModuleMainWorkflowMainWindow, 'Load Heat Source Calibration Results', pathToResults, '(*.base)')
        dname=QFileDialog.getExistingDirectory(self.ModuleMainWorkflowMainWindow, 'Load Heat Source Calibration Results', 'pathToResults')
        print(dname)
        fname = str(dname)
        self.ui.label_20.setText(dname)
        
    def show(self):
        self.ModuleMainWorkflowMainWindow.show()




if __name__ == '__main__':
    app = QApplication(sys.argv)
    ModuleMainWorkflowMainWindow = ModuleMainWorkflowMainWindow()
    ModuleMainWorkflowMainWindow.show()
    sys.exit(app.exec_())

