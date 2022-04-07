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
from module_heat_source import UiModuleHeatSource


class ModuleHeatSourceMainWindow(QWidget):
    """
    Creates Heat source gui module
    """
    def __init__(self):
        """
        initialises class
        """
        super().__init__()
        self.settings = QtCore.QSettings('wbSettings', 'app7')
        print(self.settings.fileName())
        self.module_heat_source_main_window = QMainWindow()
        self.ui = UiModuleHeatSource()
        self.ui.setupUi(self.module_heat_source_main_window)
        self.ui.stackedWidget.setCurrentWidget(self.ui.home)

# Non standard template
# Events from Stage 1
        self.ui.type.activated.connect(self.select_type)
        self.ui.button_ok.clicked.connect(self.clicked_ok)

    def select_type(self):
        """
        User choice of heat source type
        """
        if int(self.ui.type.currentIndex()) == 0:
            self.ui.stackedWidget.setCurrentWidget(self.ui.goldak)
        else:
            self.ui.stackedWidget.setCurrentWidget(self.ui.ellipsoid)

    def clicked_ok(self):
        """
        OK Button event
        """
        lines = []
        if int(self.ui.type.currentIndex()) == 0:
            lines.append('gui_heat_source_type = \'GOLDAK\'' + '\n')
            lines.append('gui_goldak_a = ' +
                         str(self.ui.goldak_a.toPlainText().strip()) + '\n')

            lines.append('gui_goldak_b = ' + str(self.ui.goldak_b.toPlainText().strip()) + '\n')
            lines.append('gui_goldak_cr = ' + str(self.ui.goldak_cr.toPlainText().strip()) + '\n')
            lines.append('gui_goldak_cf = ' + str(self.ui.goldak_cf.toPlainText().strip()) + '\n')
        else:
            lines.append('gui_heat_source_type = \'ELLIPSOID\'' + '\n')
            lines.append('gui_ellipsoid_a = ' + str(self.ui.ellipsoid_a.
                         toPlainText().strip()) + '\n')
            lines.append('gui_ellipsoid_b = ' + str(self.ui.ellipsoid_b.
                         toPlainText().strip()) + '\n')
            lines.append('gui_ellipsoid_c = ' + str(self.ui.ellipsoid_c.
                         toPlainText().strip()) + '\n')
        with open('heat_source_inputs.txt', 'w') as f:
            f.writelines(lines)
        
        my_env = os.environ.copy()
        my_env["file_no_exp"] = str("94")
        my_env["dynamic_inp"] = str("/GUI/heat_source_inputs.txt")
        p=subprocess.Popen(["sh","./modifyExport.sh",],env=my_env)
        outputCall = p.communicate()
        self.module_heat_source_main_window.close()

    def show(self):
        """
        show module
        """
        self.module_heat_source_main_window.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    module_heat_source_main_window = ModuleHeatSourceMainWindow()
    module_heat_source_main_window.show()
    sys.exit(app.exec_())
