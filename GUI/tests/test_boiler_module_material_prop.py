"""
author: EDF Energy R&D UKC
"""

import sys, os
import boiler_module_material_prop
import pytest
from pytestqt.plugin import QtBot
from PyQt5 import QtCore, QtWidgets

myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')

@pytest.fixture
def app(qtbot):
    """
    Creates app
    """
    test_gui=boiler_module_material_prop.ModuleMaterialPropMainWindow()
    qtbot.addWidget(test_gui)
    return test_gui


def test_button_add1(app,qtbot):
    """
    Tests submit button on app
    """
# ARRANGE
    is_file = os.path.isfile('mat_prop_inputs.txt')
    if is_file is True:
        os.remove("mat_prop_inputs.txt")
# ACT
    qtbot.mouseClick(app.ui.button_add1, QtCore.Qt.LeftButton)
    app.ui.Table_P1.setItem(0, 0, QtWidgets.QTableWidgetItem("1."))
    app.ui.Table_P1.setItem(0, 1, QtWidgets.QTableWidgetItem("2."))
    qtbot.mouseClick(app.ui.button_add1, QtCore.Qt.LeftButton)
    app.ui.Table_P1.setItem(1, 0, QtWidgets.QTableWidgetItem("3."))
    app.ui.Table_P1.setItem(1, 1, QtWidgets.QTableWidgetItem("4."))
    app.ui.P2.setCurrentIndex(0) # Thermal diffusivity
    qtbot.mouseClick(app.ui.button_add2, QtCore.Qt.LeftButton)
    app.ui.Table_P2.setItem(0, 0, QtWidgets.QTableWidgetItem("12."))
    app.ui.Table_P2.setItem(0, 1, QtWidgets.QTableWidgetItem("22."))
    qtbot.mouseClick(app.ui.button_add2, QtCore.Qt.LeftButton)
    app.ui.Table_P2.setItem(1, 0, QtWidgets.QTableWidgetItem("22."))
    app.ui.Table_P2.setItem(1, 1, QtWidgets.QTableWidgetItem("0."))
    
    qtbot.mouseClick(app.ui.button_add3, QtCore.Qt.LeftButton)
    app.ui.Table_W1.setItem(0, 0, QtWidgets.QTableWidgetItem("0."))
    app.ui.Table_W1.setItem(0, 1, QtWidgets.QTableWidgetItem("1."))    
    qtbot.mouseClick(app.ui.button_add3, QtCore.Qt.LeftButton)
    app.ui.Table_W1.setItem(1, 0, QtWidgets.QTableWidgetItem("2."))
    app.ui.Table_W1.setItem(1, 1, QtWidgets.QTableWidgetItem("2."))    
    app.ui.W2.setCurrentIndex(0) # Thermal diffusivity
    qtbot.mouseClick(app.ui.button_add4, QtCore.Qt.LeftButton)
    app.ui.Table_W2.setItem(0, 0, QtWidgets.QTableWidgetItem("0."))
    app.ui.Table_W2.setItem(0, 1, QtWidgets.QTableWidgetItem("1."))    
    qtbot.mouseClick(app.ui.button_add4, QtCore.Qt.LeftButton)
    app.ui.Table_W2.setItem(1, 0, QtWidgets.QTableWidgetItem("2."))
    app.ui.Table_W2.setItem(1, 1, QtWidgets.QTableWidgetItem("2."))       
# ACT
    qtbot.mouseClick(app.ui.finish, QtCore.Qt.LeftButton)
# ASSERT
    is_file = os.path.isfile('mat_prop_inputs.txt')
    assert is_file is True
'''
'''
