#!/bin/bash

######################################
# Author: Jefri Draup                #
# Email: jefri.draup@edfenergy.com   #
######################################

# Please refer to Issue:
# https://gitlab.cs.man.ac.uk/mbgm6aab/weldingworkbench/issues/5

####################################################################################################################
### Checking pre-requisites
####################################################################################################################
checkZen=$( whereis zenity )
if [[ -z $checkZen ]]
then 
	echo you need Zenity installed on your system
	echo Do you wish to install it? y/n
	read installZen
	if [ $installZen == 'y' ]
	then
		apt install zenity
	else
		echo Terminating Program
		exit 1
	fi
else
	echo Zenity found on system
fi

####################################################################################################################
### Check user profile exists
####################################################################################################################
checkConfig=$( ls ./ | grep 'user.config')

if [ -z $checkConfig ] 
then 
	echo 'File does not exist'
	echo 'Creating user.config'
	. ./setupSalomeMeca.sh
else
	echo 'File does exist'
fi

####################################################################################################################
### Set environment variables
####################################################################################################################
if [ -e user.config ] 
then
	source user.config
	printenv | grep 'USER'
else
	echo "Configuration failed!"
	echo "Try running cleanEnv.sh then runWeldingWB.sh"
	echo "Terminating program"
	exit 1
fi
####################################################################################################################
### Launch Workbench
####################################################################################################################
pushd $USER_WELDWB_pathToHere/GUI
python boiler.py &
popd
