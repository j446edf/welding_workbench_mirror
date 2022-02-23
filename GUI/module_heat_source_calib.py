import sys
import os
import subprocess
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QFileDialog, QDialog, QPlainTextEdit
from PyQt5.QtWidgets import QMainWindow
import inspect


class Ui_moduleHeatSourceCalib(object):
    def setupUi(self, moduleHeatSourceCalib):
        moduleHeatSourceCalib.setObjectName("moduleHeatSourceCalib")
        moduleHeatSourceCalib.resize(848, 623)
        self.centralwidget = QtWidgets.QWidget(moduleHeatSourceCalib)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(110, 10, 724, 107))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_1 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_1.setObjectName("label_1")
        self.verticalLayout.addWidget(self.label_1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(0, 10, 91, 91))
        self.label_6.setObjectName("label_6")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(30, 420, 781, 115))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.pushButton_8 = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.pushButton_8.setObjectName("pushButton_8")
        self.verticalLayout_5.addWidget(self.pushButton_8)
        self.pushButton_9 = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.pushButton_9.setObjectName("pushButton_9")
        self.verticalLayout_5.addWidget(self.pushButton_9)
        self.label_5 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label_5.setMaximumSize(QtCore.QSize(16777215, 26))
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_5.addWidget(self.label_5)
        self.horizontalLayout_3.addLayout(self.verticalLayout_5)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.pushButton_10 = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.pushButton_10.setObjectName("pushButton_10")
        self.verticalLayout_6.addWidget(self.pushButton_10)
        self.horizontalLayout_3.addLayout(self.verticalLayout_6)
        self.pushButton_11 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_11.setGeometry(QtCore.QRect(420, 550, 386, 25))
        self.pushButton_11.setObjectName("pushButton_11")
        self.pushButton_11.setEnabled(False)
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(30, 550, 371, 17))
        self.label_8.setObjectName("label_8")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(310, 130, 371, 17))
        self.label_7.setObjectName("label_7")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(40, 190, 781, 141))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.pushButton_2 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout_2.addWidget(self.pushButton_2)
        self.pushButton_3 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout_2.addWidget(self.pushButton_3)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_3.addWidget(self.label_3)
        self.pushButton_4 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_4.setObjectName("pushButton_4")
        self.verticalLayout_3.addWidget(self.pushButton_4)
        self.pushButton_5 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_5.setObjectName("pushButton_5")
        self.verticalLayout_3.addWidget(self.pushButton_5)
        self.horizontalLayout_2.addLayout(self.verticalLayout_3)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_4 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_4.addWidget(self.label_4)
        self.pushButton_6 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_6.setObjectName("pushButton_6")
        self.verticalLayout_4.addWidget(self.pushButton_6)
        self.pushButton_7 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_7.setObjectName("pushButton_7")
        self.verticalLayout_4.addWidget(self.pushButton_7)
        self.horizontalLayout_2.addLayout(self.verticalLayout_4)
        moduleHeatSourceCalib.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(moduleHeatSourceCalib)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 848, 23))
        self.menubar.setObjectName("menubar")
        moduleHeatSourceCalib.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(moduleHeatSourceCalib)
        self.statusbar.setObjectName("statusbar")
        moduleHeatSourceCalib.setStatusBar(self.statusbar)

        self.retranslateUi(moduleHeatSourceCalib)
        QtCore.QMetaObject.connectSlotsByName(moduleHeatSourceCalib)

    def retranslateUi(self, moduleHeatSourceCalib):
        _translate = QtCore.QCoreApplication.translate
        moduleHeatSourceCalib.setWindowTitle(_translate("moduleHeatSourceCalib", "moduleHeatSourceCalib"))
        self.label_1.setText(_translate("moduleHeatSourceCalib", "HEAT SOURCE CALIBRATION"))
        self.label.setText(_translate("moduleHeatSourceCalib", "The purpose of this tool is to help you calibrate the weld heat source"))
        self.pushButton.setText(_translate("moduleHeatSourceCalib", "Refer to ISO 18166:2016"))
        self.label_6.setText(_translate("moduleHeatSourceCalib", "INSERT LOGO"))
        self.pushButton_8.setText(_translate("moduleHeatSourceCalib", "Run Simulation"))
        self.pushButton_9.setText(_translate("moduleHeatSourceCalib", "Load Simulation Results"))
        self.label_5.setText(_translate("moduleHeatSourceCalib", "User selection results file"))
        self.pushButton_10.setText(_translate("moduleHeatSourceCalib", "Error Checking"))
        self.pushButton_11.setText(_translate("moduleHeatSourceCalib", "Proceed to Next step?"))
        self.label_8.setText(_translate("moduleHeatSourceCalib", "DATABASE PATH UPDATED AND SENT TO MAIN WIN"))
        self.label_7.setText(_translate("moduleHeatSourceCalib", "MESH UPDATED FROM MAIN WINDOW STEP 1"))
        self.label_2.setText(_translate("moduleHeatSourceCalib", "Material Data Definition"))
        self.pushButton_2.setText(_translate("moduleHeatSourceCalib", "Load Material Data"))
        self.pushButton_3.setText(_translate("moduleHeatSourceCalib", "Specify Material Data"))
        self.label_3.setText(_translate("moduleHeatSourceCalib", "Welding Process Parameters"))
        self.pushButton_4.setText(_translate("moduleHeatSourceCalib", "Specify beam conditions"))
        self.pushButton_5.setText(_translate("moduleHeatSourceCalib", "Specify Weld Path"))
        self.label_4.setText(_translate("moduleHeatSourceCalib", "Heat source type"))
        self.pushButton_6.setText(_translate("moduleHeatSourceCalib", "Specify input power"))
        self.pushButton_7.setText(_translate("moduleHeatSourceCalib", "Choose heat distribution type"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    moduleHeatSourceCalib = QtWidgets.QMainWindow()
    ui = Ui_moduleHeatSourceCalib()
    ui.setupUi(moduleHeatSourceCalib)
    moduleHeatSourceCalib.show()
    sys.exit(app.exec_())
