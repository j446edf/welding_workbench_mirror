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

from module_postproc_TC import Ui_modulePostProcTC

class ModulePostProcTCMainWindow(QWidget):
    """
    Creates the Heat source calibration post-processing GUI module
    """
    def __init__(self):
        """
        Initialises the module
        """
        super().__init__()
        self.settings = QtCore.QSettings('wbSettings','app9')
        print(self.settings.fileName())
        self.ModulePostProcTCMainWindow = QMainWindow()
        self.ui = Ui_modulePostProcTC()
        self.ui.setupUi(self.ModulePostProcTCMainWindow)

        self.ui.pushButton.clicked.connect(self.add_row)
        self.ui.pushButton_4.clicked.connect(self.remove_row)
        self.ui.pushButton_3.clicked.connect(self.browsefiles)
        self.ui.pushButton_2.clicked.connect(self.run)

    def add_row(self):
        """
        Action on clicking 'add' button
        """
        row_count1 = self.ui.tableWidget.rowCount()
        self.ui.tableWidget.insertRow(row_count1) 
        row_count = str(row_count1+1)
        self.ui.comboBox.addItem("")
        self.ui.comboBox_2.addItem("")
        _translate = QtCore.QCoreApplication.translate
        self.ui.comboBox.setItemText(row_count1, _translate("MainWindow", row_count))
        self.ui.comboBox_2.setItemText(row_count1, _translate("MainWindow", row_count))

    def remove_row(self):
        """
        Action on clicking 'remove' button
        """
        if self.ui.tableWidget.rowCount() > 0:
            self.ui.tableWidget.removeRow(
            self.ui.tableWidget.rowCount()-1)
            row_count1 = self.ui.tableWidget.rowCount()
            self.ui.comboBox.removeItem(row_count1)
            self.ui.comboBox_2.removeItem(row_count1)

    def browsefiles(self):
        """
        Action on clicking 'select experimental results' button
        """
        fname,_=QFileDialog.getOpenFileName(
                                       self.ModulePostProcTCMainWindow,
                                       'Open file', './',
                                       'Data files (*.txt)')
        #print(fname)
        self.ui.label_3.setText(str(fname))
        #open filename and update self.ui.textBrowser
        #f = open(str(fname), "r")
        #self.ui.textBrowser.append(f.readline())
        #f.close()
        self.ui.pushButton_2.setEnabled(True)

    def run(self):
        """
        Action on clicking 'run' button
        """
        tc_locs = []
        row_count1 = self.ui.tableWidget.rowCount()
        column_count1 = 3
        for i in range(row_count1):
            if self.ui.tableWidget.item(i,0) and self.ui.tableWidget.item(i,0).text():
                if self.ui.tableWidget.item(i,1) and self.ui.tableWidget.item(i,1).text():
                    if self.ui.tableWidget.item(i,2) and self.ui.tableWidget.item(i,2).text():
                        for j in range(column_count1):
                            tc_locs.append(float(
                            self.ui.tableWidget.item(i,j).text()))
                    else:
                        print("Cell empty --> Next row")
                else:
                    print("Cell empty --> Next row")
            else:
                print("Cell empty --> Next row")
        my_env = os.environ.copy()
        #print(tc_locs)
        fname = self.ui.label_3.text()
        fname = str(fname)
        NearfieldTC = int(self.ui.comboBox.currentIndex())
        FarfieldTC = int(self.ui.comboBox_2.currentIndex())
        my_env["exp_tc"] = fname
        my_env["TC_LOCS_str"] = str(tc_locs)
        my_env["no_of_TC"] = str(len(tc_locs)/3)
        my_env["nearTC"] = str(NearfieldTC)
        my_env["farTC"] = str(FarfieldTC)
        p=subprocess.Popen(["sh","./runErrorCheck.sh",],env=my_env)
        outputCall = p.communicate()

    def show(self):
        """
        Show GUI
        """
        self.ModulePostProcTCMainWindow.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ModulePostProcTCMainWindow = ModulePostProcTCMainWindow()
    ModulePostProcTCMainWindow.show()
    sys.exit(app.exec_())
