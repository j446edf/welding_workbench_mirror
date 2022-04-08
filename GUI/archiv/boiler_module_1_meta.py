"""
author: EDF Energy R&D UKC
"""
import sys
import os
import subprocess
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
from PyQt5 import QtCore


from module_metallurgy import UiModuleMeta


class ModuleMetaMainWindow(QWidget):
    """
    Creates the metallurgical GUI module
    """
    def __init__(self):
        """
        Initialises the module
        """
        super().__init__()
        self.settings = QtCore.QSettings('wbSettings', 'app3')
        print(self.settings.fileName())
        self.module_meta_main_window = QMainWindow()
        self.ui = UiModuleMeta()
        self.ui.setupUi(self.module_meta_main_window)

# Non standard template
# Events from Stage 1
        self.ui.finish.clicked.connect(self.clicked)

    def clicked(self):
        """
        Action on clicking 'finish' button
        """
        get_t_aust = self.ui.t_aust.toPlainText().strip()
        get_t_end = self.ui.t_end.toPlainText().strip()
        get_gs = self.ui.gs.toPlainText().strip()
        get_cr = self.ui.cr.toPlainText().strip()
        get_usr = self.ui.usr.toPlainText().strip()

        get_ggm = self.ui.ggm.currentText()
        get_m = self.ui.material.currentText()
        get_am = self.ui.ae13.currentText()

        my_env = os.environ.copy()
        print(my_env["PATH"])

        if self.ui.cct.isChecked():
            my_env["CCT"] = "Yes"
        else:
            my_env["CCT"] = "No"

        if self.ui.ttt.isChecked():
            my_env["TTT"] = "Yes"
        else:
            my_env["TTT"] = "No"

        if get_m == "USER":
            get_usr = self.ui.usr.toPlainText().strip()
            my_env["USER_M"] = get_usr

        my_env["T_A"] = get_t_aust
        my_env["T_E"] = get_t_end
        my_env["G_S"] = get_gs
        my_env["C_R"] = get_cr
        my_env["GG_M"] = get_ggm
        my_env["M"] = get_m
        my_env["A_M"] = get_am

        print(my_env)
        p = subprocess.Popen(["xterm", "-e", "./basicBatchpro.sh", ],
                             env=my_env)
        outputCall = p.communicate()

    def show(self):
        """
        Show GUI
        """
        self.module_meta_main_window.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    module_meta_main_window = ModuleMetaMainWindow()
    module_meta_main_window.show()
    sys.exit(app.exec_())
