"""
author: EDF Energy R&D UKC
"""

import sys, os
import boiler_module_heat_source
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
    test_gui=boiler_module_heat_source.ModuleHeatSourceMainWindow()
    qtbot.addWidget(test_gui)
    return test_gui


def test_submit(app,qtbot):
    """
    Tests submit button on app
    """
# ARRANGE
    app.ui.stackedWidget.setCurrentWidget(app.ui.goldak)
    app.ui.goldak_a.setPlainText("1.")
    app.ui.goldak_b.setPlainText("2.")
    app.ui.goldak_cr.setPlainText("3.")
    app.ui.goldak_cf.setPlainText("4.")

    is_file = os.path.isfile('heat_source_inputs.txt')
    if is_file is True:
        os.remove("heat_source_inputs.txt")

# ACT
    qtbot.mouseClick(app.ui.button_ok, QtCore.Qt.LeftButton)

# ASSERT
    is_file = os.path.isfile('heat_source_inputs.txt')
    assert is_file is True

# ARRANGE
    app.ui.stackedWidget.setCurrentWidget(app.ui.ellipsoid)
    app.ui.ellipsoid_a.setPlainText("1.")
    app.ui.ellipsoid_b.setPlainText("2.")
    app.ui.ellipsoid_c.setPlainText("3.")

    is_file = os.path.isfile('heat_source_inputs.txt')
    if is_file is True:
        os.remove("heat_source_inputs.txt")

# ACT
    qtbot.mouseClick(app.ui.button_ok, QtCore.Qt.LeftButton)

# ASSERT
    is_file = os.path.isfile('heat_source_inputs.txt')
    assert is_file is True
