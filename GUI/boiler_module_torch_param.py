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

from module_torch_param import UiModuleTorchParam


class ModuleTorchParamMainWindow(QWidget):
    """
    Creates Gui torch parameters
    """
    def __init__(self):
        """
        initialise module
        """
        super().__init__()
        self.settings = QtCore.QSettings('wbSettings', 'app6')
        print(self.settings.fileName())
        self.ModuleTorchParamMainWindow = QMainWindow()
        self.ui = UiModuleTorchParam()
        self.ui.setupUi(self.ModuleTorchParamMainWindow)

        self.ui.button_ok.clicked.connect(self.click_ok)

    def click_ok(self):
        """
        ok button event
        """

        lines = []
        ita_dec = (float(self.ui.ita.toPlainText().strip()))/100
        lines.append('gui_weld_ita = ' + str(ita_dec) + '\n')
        lines.append('gui_weld_I = ' + str(self.ui.i.toPlainText().strip()) + '\n')
        lines.append('gui_weld_V = ' + str(self.ui.v.toPlainText().strip()) + '\n')

        with open('param_outputs.txt', 'w') as f:
                f.writelines(lines)

    def show(self):
        """
        show gui
        """
        self.ModuleTorchParamMainWindow.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ModuleTorchParamMainWindow = ModuleTorchParamMainWindow()
    ModuleTorchParamMainWindow.show()
    sys.exit(app.exec_())
