#!/bin/bash

. ../user.config

export USER_WELDWB_srcDir

USER_INP_TC_EXP=$exp_tc
USER_INP_TC_LOCS=$TC_LOCS_str
USER_INP_NO_OF_TC=$no_of_TC
export USER_INP_TC_EXP
export USER_INP_TC_LOCS
export USER_INP_NO_OF_TC


cd $USER_WELDWB_srcDir/postprocessing
$USER_WELDWB_pathToSalome/salome shell killSalome.py
$USER_WELDWB_pathToSalome/salome $USER_WELDWB_srcDir/postprocessing/TCPP.py & 
$USER_WELDWB_pathToSalome/salome shell killSalome.py

./runErrorNL.sh
#read -p 'continue' input

./cleanResuSimHist.sh
#read -p 'continue' input

./checkRMS.sh
#read -p 'end' input

unset USER_INP_TC_EXP
unset USER_INP_TC_LOCS
unset USER_INP_NO_OF_TC
unset USER_WELDWB_srcDir
