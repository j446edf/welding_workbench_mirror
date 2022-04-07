import sys
import os
import subprocess
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QFileDialog, QDialog, QPlainTextEdit
from PyQt5.QtWidgets import QMainWindow, QWidget
import inspect

from module_weld_path_steady import UiModuleWeldPathSteady

class ModuleWeldPathSteadyMainWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.settings = QtCore.QSettings('wbSettings','app5')
        print(self.settings.fileName())
        self.ModuleWeldPathSteadyMainWindow = QMainWindow()
        self.ui = UiModuleWeldPathSteady()
        self.ui.setupUi(self.ModuleWeldPathSteadyMainWindow)
        self.ui.pushButton.clicked.connect(self.ok)

    def ok(self):
        """
        OK Button event
        """
        lines = []
        lines.append('gui_torch_lin_vnom = ' + str(self.ui.textEdit.toPlainText().strip()) + '\n')
        lines.append('gui_torch_x0 = ' + str(self.ui.textEdit_2.toPlainText().strip()) + '\n')
        lines.append('gui_torch_y0 = ' + str(self.ui.textEdit_3.toPlainText().strip()) + '\n')
        lines.append('gui_torch_z0 = ' + str(self.ui.textEdit_4.toPlainText().strip()) + '\n')
        lines.append("gui_torch_path = 'LINEAR'")

        with open('weld_path_inputs_steady.txt', 'w') as f:
            f.writelines(lines)

        my_env = os.environ.copy()
        my_env["file_no_exp"] = str("92")
        my_env["dynamic_inp"] = str("/GUI/weld_path_inputs_steady.txt")
        p=subprocess.Popen(["sh","./modifyExport_steady.sh",],env=my_env)
        outputCall = p.communicate()
        self.ModuleWeldPathSteadyMainWindow.close()

    def show(self):
        self.ModuleWeldPathSteadyMainWindow.show()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ModuleWeldPathSteadyMainWindow = ModuleWeldPathSteadyMainWindow()
    ModuleWeldPathSteadyMainWindow.show()
    sys.exit(app.exec_())
