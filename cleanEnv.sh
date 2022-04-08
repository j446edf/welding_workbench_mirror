#!/bin/bash

######################################
# Author: Jefri Draup                #
# Email: jefri.draup@edfenergy.com   #
######################################



if zenity --question --text="You are going to clean the environment setup \nDo you wish to continue?"
then
if [ -e $USER_WELDWB_pathToHere/user.config ]
then
mv $USER_WELDWB_pathToHere/user.config $USER_WELDWB_pathToHere/user.old.config
zenity --info --text="Clean completed"
else
zenity --warning --text="Coulcn't clean user.config / It doesn't exist. Relaunch Workbench."
fi
else
zenity --info --text="You aborted the environment cleaning"
fi
