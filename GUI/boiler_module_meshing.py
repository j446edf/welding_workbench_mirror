"""
author: EDF Energy R&D UKC
"""
import sys
import os
import subprocess
import inspect
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QFileDialog, QDialog, QPlainTextEdit
from PyQt5.QtWidgets import QMainWindow, QWidget
from PyQt5 import QtCore
from module_meshing import UiModuleMeshing


class ModuleMeshingMainWindow(QWidget):
    """
    Creates Meshing gui module
    """
    def __init__(self):
        """
        initialises class
        """
        super().__init__()
        self.settings = QtCore.QSettings('wbSettings', 'app9')
        print(self.settings.fileName())
        self.ModuleMeshingMainWindow = QMainWindow()
        self.ui = UiModuleMeshing()
        self.ui.setupUi(self.ModuleMeshingMainWindow)
        self.ui.stackedWidget.setCurrentWidget(self.ui.home)

# Non standard template
# Events from Stage 1
        self.ui.weld.activated.connect(self.select_type)
        self.ui.button_ok.clicked.connect(self.clicked_ok)
        self.ui.button_save.clicked.connect(self.clicked_save)

    def select_type(self):
        """
        User choice of weld geometry
        """
        if int(self.ui.weld.currentIndex()) == 0:
            self.ui.stackedWidget.setCurrentWidget(self.ui.Edge_Weld)
            self.ui.button_ok.setEnabled(True)
        elif int(self.ui.weld.currentIndex()) == 1:
            self.ui.stackedWidget.setCurrentWidget(self.ui.TG9)
            self.ui.button_ok.setEnabled(False)
        else:
            self.ui.stackedWidget.setCurrentWidget(self.ui.Tekken)
            self.ui.button_ok.setEnabled(False)

    def clicked_ok(self):
        """
        OK Button event
        """
        if int(self.ui.weld.currentIndex()) == 0:
            my_env = os.environ.copy()
            get_a = self.ui.a.toPlainText().strip()
            get_b = self.ui.b.toPlainText().strip()
            get_c = self.ui.c.toPlainText().strip()
            get_d = self.ui.d.toPlainText().strip()
            get_e = self.ui.e.toPlainText().strip()
            get_f = self.ui.f.toPlainText().strip()
            get_g = self.ui.g.toPlainText().strip()
            get_h = self.ui.h.toPlainText().strip()
            get_i = self.ui.i.toPlainText().strip()
            get_j = self.ui.j.toPlainText().strip()
            get_k = self.ui.k.toPlainText().strip()
            get_l = self.ui.l.toPlainText().strip()
            get_m = self.ui.m.toPlainText().strip()
            my_env["geom"] = str("0")
            my_env["ewb_a"] = get_a
            my_env["ewb_b"] = get_b
            my_env["ewb_c"] = get_c
            my_env["ewb_d"] = get_d
            my_env["ewb_e"] = get_e
            my_env["ewb_f"] = get_f
            my_env["ewb_g"] = get_g
            my_env["ewb_h"] = get_h
            my_env["ewb_i"] = get_i
            my_env["ewb_j"] = get_j
            my_env["ewb_k"] = get_k
            my_env["ewb_l"] = get_l
            my_env["ewb_m"] = get_m
            p = subprocess.Popen(["sh", "./buildMesh.sh", ],env=my_env)
            outputCall = p.communicate()
        elif int(self.ui.weld.currentIndex()) == 1:
            print("TG9 mesh builder not setup yet")
            my_env = os.environ.copy()
            my_env["geom"] = 1
        else:
            print("Tekken mesh builder not setup yet")
            my_env = os.environ.copy()
            my_env["geom"] = 2
        self.ui.button_save.setEnabled(True)

            
    def clicked_save(self):
        sfile=QFileDialog.getSaveFileName(self.ModuleMeshingMainWindow, 'Save as', './', '*.med')
        sfilename = sfile[0]
        my_env = os.environ.copy()
        if int(self.ui.weld.currentIndex()) == 0:
            my_env["mesh_file"] = str("/meshing/Edge_Welded_Beam_fromGUI.med")
        elif int(self.ui.weld.currentIndex()) == 1:
            my_env["mesh_file"] = str("/meshing/TG9_fromGUI.med")
        else:
            my_env["mesh_file"] = str("/meshing/Tekken_fromGUI.med")
        my_env["input"] = str(sfilename)
        p=subprocess.Popen(["sh","./saveMed.sh",],env=my_env)
        
    def show(self):
        """
        show module
        """
        self.ModuleMeshingMainWindow.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ModuleMeshingMainWindow = ModuleMeshingMainWindow()
    ModuleMeshingMainWindow.show()
    sys.exit(app.exec_())
            
