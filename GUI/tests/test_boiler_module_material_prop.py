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
# ACT
    qtbot.mouseClick(app.ui.button_add1, QtCore.Qt.LeftButton)
# ASSERT
    print(app.ui.Table_P1.rowCount())
    assert app.ui.Table_P1.rowCount() is 1

# ARRANGE
    is_file = os.path.isfile('outputs.txt')
    if is_file is True:
        os.remove("outputs.txt")
# ACT
    qtbot.mouseClick(app.ui.finish, QtCore.Qt.LeftButton)
# ASSERT
    is_file = os.path.isfile('outputs.txt')
    assert is_file is True
'''
'''
