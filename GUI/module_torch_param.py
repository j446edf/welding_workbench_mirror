import sys
import os
import subprocess
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QFileDialog, QDialog, QPlainTextEdit
from PyQt5.QtWidgets import QMainWindow
import inspect

class Ui_moduleTorchParam(object):
    def setupUi(self, moduleTorchParam):
        moduleTorchParam.setObjectName("moduleTorchParam")
        moduleTorchParam.resize(422, 256)
        self.centralwidget = QtWidgets.QWidget(moduleTorchParam)
        self.centralwidget.setObjectName("centralwidget")
        self.ita_label = QtWidgets.QLabel(self.centralwidget)
        self.ita_label.setGeometry(QtCore.QRect(50, 20, 361, 18))
        self.ita_label.setObjectName("ita_label")
        self.i_label = QtWidgets.QLabel(self.centralwidget)
        self.i_label.setGeometry(QtCore.QRect(50, 70, 361, 18))
        self.i_label.setObjectName("i_label")
        self.v_label = QtWidgets.QLabel(self.centralwidget)
        self.v_label.setGeometry(QtCore.QRect(50, 120, 361, 18))
        self.v_label.setObjectName("v_label")
        self.ita = QtWidgets.QTextEdit(self.centralwidget)
        self.ita.setGeometry(QtCore.QRect(250, 10, 104, 31))
        self.ita.setObjectName("ita")
        self.i = QtWidgets.QTextEdit(self.centralwidget)
        self.i.setGeometry(QtCore.QRect(250, 60, 104, 31))
        self.i.setObjectName("i")
        self.v = QtWidgets.QTextEdit(self.centralwidget)
        self.v.setGeometry(QtCore.QRect(250, 110, 104, 31))
        self.v.setObjectName("v")
        self.button_ok = QtWidgets.QPushButton(self.centralwidget)
        self.button_ok.setGeometry(QtCore.QRect(300, 170, 95, 26))
        self.button_ok.setObjectName("button_ok")
        moduleTorchParam.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(moduleTorchParam)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 422, 23))
        self.menubar.setObjectName("menubar")
        moduleTorchParam.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(moduleTorchParam)
        self.statusbar.setObjectName("statusbar")
        moduleTorchParam.setStatusBar(self.statusbar)

        self.retranslateUi(moduleTorchParam)
        QtCore.QMetaObject.connectSlotsByName(moduleTorchParam)

    def retranslateUi(self, moduleTorchParam):
        _translate = QtCore.QCoreApplication.translate
        moduleTorchParam.setWindowTitle(_translate("moduleTorchParam", "moduleTorchParam"))
        self.ita_label.setText(_translate("moduleTorchParam", "Weld torch efficiency                                  %"))
        self.i_label.setText(_translate("moduleTorchParam", "Weld torch current                                      A"))
        self.v_label.setText(_translate("moduleTorchParam", "Weld torch voltage                                      V"))
        self.button_ok.setText(_translate("moduleTorchParam", "Ok"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    moduleTorchParam = QtWidgets.QMainWindow()
    ui = Ui_moduleTorchParam()
    ui.setupUi(moduleTorchParam)
    moduleTorchParam.show()
    sys.exit(app.exec_())

