"""
author: EDF Energy R&D UKC
"""
import sys
import os
import subprocess
import inspect
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QFileDialog, QDialog, QPlainTextEdit
from PyQt5.QtWidgets import QMainWindow

class UiModuleHeatSource(object):
    """
    heat source gui module
    """

    def setupUi(self, module_heat_source):
        """
        setup GUI
        """
        module_heat_source.setObjectName("module_heat_source")
        module_heat_source.resize(494, 417)
        self.centralwidget = QtWidgets.QWidget(module_heat_source)
        self.centralwidget.setObjectName("centralwidget")
        self.type = QtWidgets.QComboBox(self.centralwidget)
        self.type.setGeometry(QtCore.QRect(180, 20, 121, 26))
        self.type.setObjectName("type")
        self.type.addItem("")
        self.type.addItem("")
        self.type_label = QtWidgets.QLabel(self.centralwidget)
        self.type_label.setGeometry(QtCore.QRect(30, 20, 141, 18))
        self.type_label.setObjectName("type_label")
        self.button_ok = QtWidgets.QPushButton(self.centralwidget)
        self.button_ok.setGeometry(QtCore.QRect(380, 330, 95, 26))
        self.button_ok.setObjectName("button_ok")
        self.stacked_widget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stacked_widget.setGeometry(QtCore.QRect(30, 70, 441, 241))
        self.stacked_widget.setObjectName("stacked_widget")
        self.home = QtWidgets.QWidget()
        self.home.setObjectName("home")
        self.label = QtWidgets.QLabel(self.home)
        self.label.setGeometry(QtCore.QRect(20, 50, 321, 141))
        self.label.setObjectName("label")
        self.stacked_widget.addWidget(self.home)
        self.goldak = QtWidgets.QWidget()
        self.goldak.setObjectName("goldak")
        self.goldak_a = QtWidgets.QTextEdit(self.goldak)
        self.goldak_a.setGeometry(QtCore.QRect(40, 40, 104, 31))
        self.goldak_a.setObjectName("goldak_a")
        self.goldak_cr = QtWidgets.QTextEdit(self.goldak)
        self.goldak_cr.setGeometry(QtCore.QRect(40, 140, 104, 31))
        self.goldak_cr.setObjectName("goldak_cr")
        self.goldak_cr_label = QtWidgets.QLabel(self.goldak)
        self.goldak_cr_label.setGeometry(QtCore.QRect(0, 150, 74, 18))
        self.goldak_cr_label.setObjectName("goldak_cr_label")
        self.goldak_b_label = QtWidgets.QLabel(self.goldak)
        self.goldak_b_label.setGeometry(QtCore.QRect(0, 100, 74, 18))
        self.goldak_b_label.setObjectName("goldak_b_label")
        self.goldak_measurement = QtWidgets.QLabel(self.goldak)
        self.goldak_measurement.setGeometry(QtCore.QRect(0, 0, 111, 20))
        self.goldak_measurement.setObjectName("goldak_measurement")
        self.goldak_cf = QtWidgets.QTextEdit(self.goldak)
        self.goldak_cf.setGeometry(QtCore.QRect(40, 190, 104, 31))
        self.goldak_cf.setObjectName("goldak_cf")
        self.goldak_image = QtWidgets.QLabel(self.goldak)
        self.goldak_image.setGeometry(QtCore.QRect(170, 0, 251, 201))
        self.goldak_image.setText("")
        self.goldak_image.setPixmap(QtGui.QPixmap("Goldak.png"))
        self.goldak_image.setScaledContents(True)
        self.goldak_image.setObjectName("goldak_image")
        self.goldak_a_label = QtWidgets.QLabel(self.goldak)
        self.goldak_a_label.setGeometry(QtCore.QRect(0, 50, 74, 18))
        self.goldak_a_label.setObjectName("goldak_a_label")
        self.goldak_b = QtWidgets.QTextEdit(self.goldak)
        self.goldak_b.setGeometry(QtCore.QRect(40, 90, 104, 31))
        self.goldak_b.setObjectName("goldak_b")
        self.goldak_cf_label = QtWidgets.QLabel(self.goldak)
        self.goldak_cf_label.setGeometry(QtCore.QRect(0, 200, 74, 18))
        self.goldak_cf_label.setObjectName("goldak_cf_label")
        self.z_direction_1 = QtWidgets.QLabel(self.goldak)
        self.z_direction_1.setGeometry(QtCore.QRect(190, 210, 201, 18))
        self.z_direction_1.setObjectName("z_direction_1")
        self.stacked_widget.addWidget(self.goldak)
        self.ellipsoid = QtWidgets.QWidget()
        self.ellipsoid.setObjectName("ellipsoid")
        self.ellipsoid_a = QtWidgets.QTextEdit(self.ellipsoid)
        self.ellipsoid_a.setGeometry(QtCore.QRect(40, 40, 104, 31))
        self.ellipsoid_a.setObjectName("ellipsoid_a")
        self.ellipsoid_image = QtWidgets.QLabel(self.ellipsoid)
        self.ellipsoid_image.setGeometry(QtCore.QRect(170, 0, 251, 201))
        self.ellipsoid_image.setText("")
        self.ellipsoid_image.setPixmap(QtGui.QPixmap("Ellipsoid.png"))
        self.ellipsoid_image.setScaledContents(True)
        self.ellipsoid_image.setObjectName("ellipsoid_image")
        self.ellipsoid_c_label = QtWidgets.QLabel(self.ellipsoid)
        self.ellipsoid_c_label.setGeometry(QtCore.QRect(0, 150, 74, 18))
        self.ellipsoid_c_label.setObjectName("ellipsoid_c_label")
        self.ellipsoid_measurement = QtWidgets.QLabel(self.ellipsoid)
        self.ellipsoid_measurement.setGeometry(QtCore.QRect(0, 0, 111, 20))
        self.ellipsoid_measurement.setObjectName("ellipsoid_measurement")
        self.ellipsoid_c = QtWidgets.QTextEdit(self.ellipsoid)
        self.ellipsoid_c.setGeometry(QtCore.QRect(40, 140, 104, 31))
        self.ellipsoid_c.setObjectName("ellipsoid_c")
        self.ellipsoid_a_label = QtWidgets.QLabel(self.ellipsoid)
        self.ellipsoid_a_label.setGeometry(QtCore.QRect(0, 50, 74, 18))
        self.ellipsoid_a_label.setObjectName("ellipsoid_a_label")
        self.ellipsoid_b = QtWidgets.QTextEdit(self.ellipsoid)
        self.ellipsoid_b.setGeometry(QtCore.QRect(40, 90, 104, 31))
        self.ellipsoid_b.setObjectName("ellipsoid_b")
        self.ellipsoid_b_label = QtWidgets.QLabel(self.ellipsoid)
        self.ellipsoid_b_label.setGeometry(QtCore.QRect(0, 100, 74, 18))
        self.ellipsoid_b_label.setObjectName("ellipsoid_b_label")
        self.z_direction_2 = QtWidgets.QLabel(self.ellipsoid)
        self.z_direction_2.setGeometry(QtCore.QRect(190, 210, 201, 18))
        self.z_direction_2.setObjectName("z_direction_2")
        self.stacked_widget.addWidget(self.ellipsoid)
        module_heat_source.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(module_heat_source)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 494, 23))
        self.menubar.setObjectName("menubar")
        module_heat_source.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(module_heat_source)
        self.statusbar.setObjectName("statusbar")
        module_heat_source.setStatusBar(self.statusbar)

        self.retranslateUi(module_heat_source)
        self.stacked_widget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(module_heat_source)

    def retranslateUi(self, module_heat_source):
        """
        positioning
        """
        _translate = QtCore.QCoreApplication.translate
        module_heat_source.setWindowTitle(_translate("module_heat_source", "module_heat_source"))
        self.type.setItemText(0, _translate("module_heat_source", "Goldak"))
        self.type.setItemText(1, _translate("module_heat_source", "Ellipsoid"))
        self.type_label.setText(_translate("module_heat_source", "Heat Source Type:"))
        self.z_direction_1.setText(_translate("module_heat_source", "Welding direction - txn axis"))
        self.z_direction_2.setText(_translate("module_heat_source", "Welding direction - txn axis"))
        self.button_ok.setText(_translate("module_heat_source", "Ok"))
        self.label.setText(_translate("module_heat_source", "Please select a heat source type..."))
        self.goldak_cr_label.setText(_translate("module_heat_source", "cr"))
        self.goldak_b_label.setText(_translate("module_heat_source", "b"))
        self.goldak_measurement.setText(_translate("module_heat_source", "Length (mm):"))
        self.goldak_a_label.setText(_translate("module_heat_source", "a"))
        self.goldak_cf_label.setText(_translate("module_heat_source", "cf"))
        self.ellipsoid_c_label.setText(_translate("module_heat_source", "c"))
        self.ellipsoid_measurement.setText(_translate("module_heat_source", "Radius (mm):"))
        self.ellipsoid_a_label.setText(_translate("module_heat_source", "a"))
        self.ellipsoid_b_label.setText(_translate("module_heat_source", "b"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    module_heat_source = QtWidgets.QMainWindow()
    ui = UiModuleHeatSource()
    ui.setupUi(module_heat_source)
    moduleHeatSource.show()
    sys.exit(app.exec_())

