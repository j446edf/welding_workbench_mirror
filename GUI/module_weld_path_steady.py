import sys
import os
import subprocess
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QFileDialog, QDialog, QPlainTextEdit
from PyQt5.QtWidgets import QMainWindow
import inspect

class UiModuleWeldPathSteady(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(338, 268)
        self.textEdit = QtWidgets.QTextEdit(Form)
        self.textEdit.setGeometry(QtCore.QRect(200, 20, 104, 31))
        self.textEdit.setObjectName("textEdit")
        self.textEdit_2 = QtWidgets.QTextEdit(Form)
        self.textEdit_2.setGeometry(QtCore.QRect(230, 70, 71, 31))
        self.textEdit_2.setObjectName("textEdit_2")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(20, 30, 181, 17))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(20, 80, 191, 17))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(210, 80, 21, 17))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(210, 120, 21, 17))
        self.label_4.setObjectName("label_4")
        self.textEdit_3 = QtWidgets.QTextEdit(Form)
        self.textEdit_3.setGeometry(QtCore.QRect(230, 110, 71, 31))
        self.textEdit_3.setObjectName("textEdit_3")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(210, 160, 21, 17))
        self.label_5.setObjectName("label_5")
        self.textEdit_4 = QtWidgets.QTextEdit(Form)
        self.textEdit_4.setGeometry(QtCore.QRect(230, 150, 71, 31))
        self.textEdit_4.setObjectName("textEdit_4")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(230, 210, 89, 25))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Nominal Velocity (mm/s):"))
        self.label_2.setText(_translate("Form", "Initial heat source position:"))
        self.label_3.setText(_translate("Form", "x:"))
        self.label_4.setText(_translate("Form", "y:"))
        self.label_5.setText(_translate("Form", "z:"))
        self.pushButton.setText(_translate("Form", "Ok"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = UiModuleWeldPathSteady()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

