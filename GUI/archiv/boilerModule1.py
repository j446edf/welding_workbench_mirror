import sys
import os
import subprocess
from PyQt5.QtWidgets import QApplication, QFileDialog, QDialog, QPlainTextEdit
from PyQt5.QtWidgets import QMainWindow
from PyQt5 import QtCore 
import inspect

from module1 import Ui_module1
from boilerModule1Meta import ModuleMetaMainWindow
    

class Module1MainWindow:
    
    def __init__(self):
        self.settings = QtCore.QSettings('wbSettings','app1a')
        print(self.settings.fileName())
        self.Module1MainWindow = QMainWindow()
        self.ui = Ui_module1()
        self.ui.setupUi(self.Module1MainWindow)
        
        #Non standard template
        # Events from Stage 1
        self.ui.pushButton_mod1_1.clicked.connect(self.clickpushButton_mod1_1)
        
        
    # def clickpushButton_mod1_1(self):
        # self.window = QMainWindow()
        # self.ui = Ui_module1()
        # self.ui.setupUi(self.window)
        # self.window.show()
    def clickpushButton_mod1_1(self):  #< ----- Import directly module_metallurgy (no buttoon events)
        self.window3 = QMainWindow()
        self.window3 = ModuleMetaMainWindow()
        self.window3.show()
    def show(self):
        self.Module1MainWindow.show()




if __name__ == '__main__':
    app = QApplication(sys.argv)
    Module1MainWindow = Module1MainWindow()
    Module1MainWindow.show()
    sys.exit(app.exec_())

