# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'module1.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!
import sys
import os
import subprocess
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow

from module_metallurgy import Ui_moduleMeta

class Ui_module1(object):
    def setupUi(self, module1):
        module1.setObjectName("module1")
        module1.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(module1)
        self.centralwidget.setObjectName("centralwidget")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(150, 160, 256, 192))
        self.textBrowser.setObjectName("textBrowser")
        self.pushButton_mod1_1 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_mod1_1.setGeometry(QtCore.QRect(480, 160, 201, 181))
        self.pushButton_mod1_1.setObjectName("pushButton_mod1_1")
        self.pushButton_mod1_1.clicked.connect(self.clickpushButton_mod1_1)
        module1.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(module1)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 24))
        self.menubar.setObjectName("menubar")
        module1.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(module1)
        self.statusbar.setObjectName("statusbar")
        module1.setStatusBar(self.statusbar)

        self.retranslateUi(module1)
        QtCore.QMetaObject.connectSlotsByName(module1)


    def clickpushButton_mod1_1(self):
        self.window = QMainWindow()
        self.ui = Ui_moduleMeta()
        self.ui.setupUi(self.window)
        self.window.show()


    def retranslateUi(self, module1):
        _translate = QtCore.QCoreApplication.translate
        module1.setWindowTitle(_translate("module1", "MainWindow"))
        self.textBrowser.setHtml(_translate("module1", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Whatever module you created</p></body></html>"))
        self.pushButton_mod1_1.setText(_translate("module1", "Metallurgical module"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    module1 = QtWidgets.QMainWindow()
    ui = Ui_module1()
    ui.setupUi(module1)
    module1.show()
    sys.exit(app.exec_())

