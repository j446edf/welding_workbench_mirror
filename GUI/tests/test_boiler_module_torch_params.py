"""
author: EDF Energy R&D UKC
"""

import sys, os
import boiler_module_torch_param
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
    test_gui=boiler_module_torch_param.ModuleTorchParamMainWindow()
    qtbot.addWidget(test_gui)
    return test_gui


def test_submit(app,qtbot):
    """
    Tests submit button on app
    """
# ARRANGE
    app.ui.i.setPlainText("1.")
    app.ui.ita.setPlainText("2.")
    app.ui.v.setPlainText("3.")

    is_file = os.path.isfile('param_outputs.txt')
    if is_file is True:
        os.remove("param_outputs.txt")

# ACT
    qtbot.mouseClick(app.ui.button_ok, QtCore.Qt.LeftButton)

# ASSERT
    is_file = os.path.isfile('param_outputs.txt')
    assert is_file is True
