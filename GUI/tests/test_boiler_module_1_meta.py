"""
author: EDF Energy R&D UKC
"""

import sys, os
import boiler_module_1_meta
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
    test_gui=boiler_module_1_meta.ModuleMetaMainWindow()
    qtbot.addWidget(test_gui)
    return test_gui


def test_submit(app,qtbot):
    """
    Tests submit button on app
    """
# ARRANGE
    app.ui.t_aust.setPlainText("900.")
    app.ui.t_end.setPlainText("20.")
    app.ui.gs.setPlainText("6.")
    app.ui.cr.setPlainText("0.1")
    app.ui.usr.setPlainText("")
    app.ui.ggm.setCurrentIndex(0)#IKAWA
    app.ui.material.setCurrentIndex(0)#SA508
    app.ui.ae13.setCurrentIndex(0)#Grange
    app.ui.cct.setChecked(True)
    app.ui.ttt.setChecked(True)
    

    is_file = os.path.isfile('CCT_with_Cooling_Curves.png')
    if is_file is True:
        os.remove("CCT_with_Cooling_Curves.png")
    is_file = os.path.isfile('CCT_with_Cooling_Curves.png')
    if is_file is True:
        os.remove("TTT_with_Cooling_Curves.png")
    is_file = os.path.isfile('TCCT.66')
    if is_file is True:
        os.remove("CCT.66")

# ACT
    qtbot.mouseClick(app.ui.finish, QtCore.Qt.LeftButton)

# ASSERT
    is_file = os.path.isfile('CCT_with_Cooling_Curves.png')
    assert is_file is True
    is_file = os.path.isfile('TTT_with_Cooling_Curves.png')
    assert is_file is True
    is_file = os.path.isfile('CCT.66')
    assert is_file is True   
