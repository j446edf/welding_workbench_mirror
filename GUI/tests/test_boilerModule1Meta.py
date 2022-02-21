import sys, os
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')

import boilerModule1Meta
import pytest
from pytestqt.plugin import QtBot
from PyQt5 import QtCore

#from boilerModule1Meta import ModuleMetaMainWindow
'''
@pytest.fixture
def app(qtbot):
	# ARRANGE
	test_gui=boilerModule1Meta.ModuleMetaMainWindow()
	qtbot.addWidget(test_gui)
	return test_gui


def test_submit(app,qtbot):
	#window=boilerModule1Meta.ModuleMetaMainWindow()
	qtbot.mouseClick(app.ui.Finish, QtCore.Qt.LeftButton)
	isFile = os.path.isfile('CCT_with_Cooling_Curves.png')
	assert isFile == True
'''
def test_submit(qtbot):
	# ARRANGE
	window=boilerModule1Meta.ModuleMetaMainWindow()
	window.ui.T_Aust.setPlainText("900.")
	window.ui.T_End.setPlainText("20.")
	window.ui.GS.setPlainText("6.")
	window.ui.CR.setPlainText("0.1")
	window.ui.USR.setPlainText("")
	window.ui.GGM.setCurrentIndex(0)#IKAWA
	window.ui.Material.setCurrentIndex(0)#SA508
	window.ui.AE13.setCurrentIndex(0)#Grange
	window.ui.CCT.setChecked(True)
	window.ui.TTT.setChecked(True)
	

	isFile = os.path.isfile('CCT_with_Cooling_Curves.png')
	if isFile == True:
		os.remove("CCT_with_Cooling_Curves.png")
	isFile = os.path.isfile('CCT_with_Cooling_Curves.png')
	if isFile == True:
		os.remove("TTT_with_Cooling_Curves.png")
	isFile = os.path.isfile('TCCT.66')
	if isFile == True:
		os.remove("CCT.66")

	# ACT
	qtbot.mouseClick(window.ui.Finish, QtCore.Qt.LeftButton)

	# ASSERT
	isFile = os.path.isfile('CCT_with_Cooling_Curves.png')
	assert isFile == True
	isFile = os.path.isfile('TTT_with_Cooling_Curves.png')
	assert isFile == True
	isFile = os.path.isfile('CCT.66')
	assert isFile == True	
