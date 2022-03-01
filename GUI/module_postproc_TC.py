import sys
import os
import subprocess
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QFileDialog, QDialog, QPlainTextEdit
from PyQt5.QtWidgets import QMainWindow
import inspect

class Ui_modulePostProcTC(object):
    def setupUi(self, modulePostProcTC):
        modulePostProcTC.setObjectName("modulePostProcTC")
        modulePostProcTC.resize(520, 510)
        self.centralwidget = QtWidgets.QWidget(modulePostProcTC)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(20, 50, 401, 192))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(120)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 20, 231, 18))
        self.label_2.setObjectName("label_2")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(420, 430, 95, 26))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.setEnabled(False)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 380, 481, 20))
        self.label_3.setObjectName("label_3")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(20, 340, 161, 26))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(20, 250, 95, 26))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(130, 250, 95, 26))
        self.pushButton_4.setObjectName("pushButton_4")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(20, 310, 171, 20))
        self.label_4.setObjectName("label_4")
        modulePostProcTC.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(modulePostProcTC)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 520, 23))
        self.menubar.setObjectName("menubar")
        modulePostProcTC.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(modulePostProcTC)
        self.statusbar.setObjectName("statusbar")
        modulePostProcTC.setStatusBar(self.statusbar)

        self.retranslateUi(modulePostProcTC)
        QtCore.QMetaObject.connectSlotsByName(modulePostProcTC)

    def retranslateUi(self, modulePostProcTC):
        _translate = QtCore.QCoreApplication.translate
        modulePostProcTC.setWindowTitle(_translate("modulePostProcTC", "modulePostProcTC"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("modulePostProcTC", "x"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("modulePostProcTC", "y"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("modulePostProcTC", "z"))
        self.label_2.setText(_translate("modulePostProcTC", "Thermocouple locations (mm)"))
        self.pushButton_2.setText(_translate("modulePostProcTC", "Run"))
        self.label_3.setText(_translate("modulePostProcTC", "Select experimental results..."))
        self.pushButton_3.setText(_translate("modulePostProcTC", "Select Data File"))
        self.pushButton.setText(_translate("modulePostProcTC", "add"))
        self.pushButton_4.setText(_translate("modulePostProcTC", "remove"))
        self.label_4.setText(_translate("modulePostProcTC", "Experimental results:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    modulePostProcTC = QtWidgets.QMainWindow()
    ui = Ui_modulePostProcTC()
    ui.setupUi(modulePostProcTC)
    modulePostProcTC.show()
    sys.exit(app.exec_())

