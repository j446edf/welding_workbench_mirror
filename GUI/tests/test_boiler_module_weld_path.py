"""
author: EDF Energy R&D UKC
"""

import sys, os
import boiler_module_weld_path
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
    test_gui=boiler_module_weld_path.ModuleWeldPathMainWindow()
    qtbot.addWidget(test_gui)
    return test_gui


def test_submit(app,qtbot):
    """
    Tests submit button on app
    """
# ARRANGE
    is_file = os.path.isfile('weld_path_inputs.txt')
    if is_file is True:
        os.remove("weld_path_inputs.txt")
    qtbot.mouseClick(app.ui.v_t_addRow_button, QtCore.Qt.LeftButton)
    app.ui.v_t_table.setItem(0, 0, QtWidgets.QTableWidgetItem("1."))
    app.ui.v_t_table.setItem(0, 1, QtWidgets.QTableWidgetItem("2."))
    qtbot.mouseClick(app.ui.v_t_addRow_button, QtCore.Qt.LeftButton)
    app.ui.v_t_table.setItem(1, 0, QtWidgets.QTableWidgetItem("3."))
    app.ui.v_t_table.setItem(1, 1, QtWidgets.QTableWidgetItem("4."))
    app.ui.beam_on.setPlainText("0.")
    app.ui.beam_off.setPlainText("10.")
    qtbot.mouseClick(app.ui.path_addRow_button, QtCore.Qt.LeftButton)
    app.ui.path_table.setItem(0, 0, QtWidgets.QTableWidgetItem("12."))
    app.ui.path_table.setItem(0, 1, QtWidgets.QTableWidgetItem("22."))
    app.ui.path_table.setItem(0, 2, QtWidgets.QTableWidgetItem("22."))
    app.ui.path_table.setItem(0, 3, QtWidgets.QTableWidgetItem("0."))
    app.ui.path_table.setItem(0, 4, QtWidgets.QTableWidgetItem("0."))
    app.ui.path_table.setItem(0, 5, QtWidgets.QTableWidgetItem("1."))    
    qtbot.mouseClick(app.ui.path_addRow_button, QtCore.Qt.LeftButton)
    app.ui.path_table.setItem(1, 0, QtWidgets.QTableWidgetItem("22."))
    app.ui.path_table.setItem(1, 1, QtWidgets.QTableWidgetItem("32."))
    app.ui.path_table.setItem(1, 2, QtWidgets.QTableWidgetItem("42."))
    app.ui.path_table.setItem(1, 3, QtWidgets.QTableWidgetItem("0."))
    app.ui.path_table.setItem(1, 4, QtWidgets.QTableWidgetItem("0."))
    app.ui.path_table.setItem(1, 5, QtWidgets.QTableWidgetItem("10."))    
    app.ui.dirx0.setPlainText("0.")
    app.ui.diry0.setPlainText("10.")
    app.ui.dirz0.setPlainText("104.")
    qtbot.mouseClick(app.ui.button_ok, QtCore.Qt.LeftButton)
# ASSERT
    is_file = os.path.isfile('weld_path_inputs.txt')
    assert is_file is True
