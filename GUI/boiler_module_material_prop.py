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

from module_material_prop import UiModuleMaterialProp


class ModuleMaterialPropMainWindow(QWidget):
    """
    Creates MAterial prop parameters
    """
    def __init__(self):
        """
        initialise module
        """
        super().__init__()
        self.settings = QtCore.QSettings('wbSettings', 'app6')
        print(self.settings.fileName())
        self.ModuleMaterialPropMainWindow = QMainWindow()
        self.ui = UiModuleMaterialProp()
        self.ui.setupUi(self.ModuleMaterialPropMainWindow)
        # Events
        self.ui.button_add1.clicked.connect(self.addRow1)
        self.ui.button_remove1.clicked.connect(self.removeRow1)
        self.ui.P2.activated.connect(self.SelectP2)
        self.ui.button_add2.clicked.connect(self.addRow2)
        self.ui.button_remove2.clicked.connect(self.removeRow2)
        self.ui.button_add3.clicked.connect(self.addRow3)
        self.ui.button_remove3.clicked.connect(self.removeRow3)
        self.ui.W2.activated.connect(self.SelectW2)
        self.ui.button_add4.clicked.connect(self.addRow4)
        self.ui.button_remove4.clicked.connect(self.removeRow4)
        self.ui.finish.clicked.connect(self.clicked)

    def addRow1(self):
        """
        Add row p1
        """
        rowCount1 = self.ui.Table_P1.rowCount()
        self.ui.Table_P1.insertRow(rowCount1)
    def removeRow1(self):
        """
        Remove row p1
        """
        if self.ui.Table_P1.rowCount() > 0:
            self.ui.Table_P1.removeRow(self.ui.Table_P1.rowCount()-1)

    def SelectP2(self):
        """
        Select enthalpy
        """
        _translate = QtCore.QCoreApplication.translate
        item = self.ui.Table_P2.horizontalHeaderItem(1)
        if int(self.ui.P2.currentIndex()) == 0:
            item.setText(_translate("MainWindow", "Thermal Diffusivity"))
        else:
            item.setText(_translate("MainWindow", "Enthalpy"))
    def addRow2(self):
        """
        Add row p2
        """
        rowCount2 = self.ui.Table_P2.rowCount()
        self.ui.Table_P2.insertRow(rowCount2)
        _translate = QtCore.QCoreApplication.translate
        item = self.ui.Table_P2.horizontalHeaderItem(1)
        if int(self.ui.P2.currentIndex()) == 0:
            item.setText(_translate("MainWindow", "Thermal Diffusivity"))
        else:
            item.setText(_translate("MainWindow", "Enthalpy"))

    def removeRow2(self):
        """
        Remove row p2
        """
        if self.ui.Table_P2.rowCount() > 0:
            self.ui.Table_P2.removeRow(self.ui.Table_P2.rowCount()-1)

    def addRow3(self):
        """
        Add row p3
        """
        rowCount3 = self.ui.Table_W1.rowCount()
        self.ui.Table_W1.insertRow(rowCount3)

    def removeRow3(self):
        """
        Remove row p3
        """
        if self.ui.Table_W1.rowCount() > 0:
            self.ui.Table_W1.removeRow(self.ui.Table_W1.rowCount()-1)

    def addRow4(self):
        """
        Add row p4
        """
        rowCount4 = self.ui.Table_W2.rowCount()
        self.ui.Table_W2.insertRow(rowCount4)
        _translate = QtCore.QCoreApplication.translate
        item = self.ui.Table_W2.horizontalHeaderItem(1)
        if int(self.ui.W2.currentIndex()) == 0:
            item.setText(_translate("MainWindow", "Thermal Diffusivity"))
        else:
            item.setText(_translate("MainWindow", "Enthalpy"))

    def removeRow4(self):
        """
        Remove row p4
        """
        if self.ui.Table_W2.rowCount() > 0:
            self.ui.Table_W2.removeRow(self.ui.Table_W2.rowCount()-1)

    def SelectW2(self):
        """
        Select enthalpy
        """
        _translate = QtCore.QCoreApplication.translate
        item = self.ui.Table_W2.horizontalHeaderItem(1)
        if int(self.ui.W2.currentIndex()) == 0:
            item.setText(_translate("MainWindow", "Thermal Diffusivity"))
        else:
            item.setText(_translate("MainWindow", "Enthalpy"))

    def clicked(self):
        """
        Click Submit
        """
        Parent_cond = []
        Parent_2 = []
        Weld_cond = []
        Weld_2 = []
        rowCount1 = self.ui.Table_P1.rowCount()
        rowCount2 = self.ui.Table_P2.rowCount()
        rowCount3 = self.ui.Table_W1.rowCount()
        rowCount4 = self.ui.Table_W2.rowCount()
        columnCount = 2
        for i in range(rowCount1):
            if self.ui.Table_P1.item(i,0) and self.ui.Table_P1.item(i,0).text():
                if self.ui.Table_P1.item(i,1) and self.ui.Table_P1.item(i,1).text():
                    for j in range(columnCount):
                        Parent_cond.append(float(self.ui.Table_P1.item(i,j).text()))
                else:
                    print("Cell empty --> Next row")
            else:
                print("Cell empty --> Next row")

        for i in range(rowCount2):
            if self.ui.Table_P2.item(i,0) and self.ui.Table_P2.item(i,0).text():
                if self.ui.Table_P2.item(i,1) and self.ui.Table_P2.item(i,1).text():
                    for j in range(columnCount):
                        Parent_2.append(float(self.ui.Table_P2.item(i,j).text()))
                else:
                    print("Cell empty --> Next row")
            else:
                print("Cell empty --> Next row")

        for i in range(rowCount3):
            if self.ui.Table_W1.item(i,0) and self.ui.Table_W1.item(i,0).text():
                if self.ui.Table_W1.item(i,1) and self.ui.Table_W1.item(i,1).text():
                    for j in range(columnCount):
                        Weld_cond.append(float(self.ui.Table_W1.item(i,j).text()))
                else:
                    print("Cell empty --> Next row")
            else:
                print("Cell empty --> Next row")

        for i in range(rowCount4):
            if self.ui.Table_W2.item(i,0) and self.ui.Table_W2.item(i,0).text():
                if self.ui.Table_W2.item(i,1) and self.ui.Table_W2.item(i,1).text():
                    for j in range(columnCount):
                        Weld_2.append(float(self.ui.Table_W2.item(i,j).text()))
                else:
                    print("Cell empty --> Next row")
            else:
                print("Cell empty --> Next row")

        Lines = []
        Lines.append('parent_lsa_from_GUI=' + str(Parent_cond) + '\n' + '\n')
        if int(self.ui.P2.currentIndex()) == 0:
            Lines.append('user_choice_parent_def=1 #diffusivity' + '\n' + '\n')
            Lines.append('parent_lrhocpsa_from_GUI=' + str(Parent_2) + '\n' + '\n' + '\n')
        else:
            Lines.append('user_choice_parent_def=2 #enthalpy' + '\n' + '\n')
            Lines.append('parent_enthalpy_from_GUI=' + str(Parent_2) + '\n' + '\n' + '\n')

        Lines.append('weld_lsa_from_GUI= ' + str(Weld_cond) + '\n' + '\n')
        if int(self.ui.W2.currentIndex()) == 0:
            Lines.append('user_choice_weld_def=1 #diffusivity' + '\n' + '\n')
            Lines.append('weld_rhocpsa_from_GUI=' + str(Weld_2) + '\n' + '\n' + '\n')
        else:
            Lines.append('user_choice_weld_def=2 #enthalpy' + '\n' + '\n')
            Lines.append('weld_enthalpy_from_GUI=' + str(Weld_2) + '\n' + '\n' + '\n')

        with open('outputs.txt', 'w') as f:
            f.writelines(Lines)

    def show(self):
        """
        show gui
        """
        self.ModuleMaterialPropMainWindow.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ModuleMaterialPropMainWindow = ModuleMaterialPropMainWindow()
    ModuleMaterialPropMainWindow.show()
    sys.exit(app.exec_())
