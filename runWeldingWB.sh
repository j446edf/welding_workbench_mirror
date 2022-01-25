#!/bin/bash

######################################
# Author: Jefri Draup                #
# Email: jefri.draup@edfenergy.com   #
######################################

# Please refer to Issue:
# https://gitlab.cs.man.ac.uk/mbgm6aab/weldingworkbench/issues/2

#### You need to set these up front ################################################################################
####################################################################################################################
#source /home/mbgm6aab/codes/tfel/master/install/env.sh
#export pathToSalome='/home/mbgm6aab/salome_meca/appli_V2019.0.3_universal'
#export pathToHere=$( pwd )
#export srcDir='/home/mbgm6aab/Documents/weldingworkbench'
####################################################################################################################
####################################################################################################################

####################################################################################################################
### Check user profile exists
####################################################################################################################
checkConfig=$(ls ./ | grep 'user.config')

if [ -z $checkConfig ] 
then 
echo 'File does not exist'
echo 'Creating user.config'
echo export USER_WELDWB_pathToSalome="'"/home/mbgm6aab/salome_meca/appli_V2019.0.3_universal"'" > user.config
echo export USER_WELDWB_pathToHere="$""("" pwd "")" >> user.config
echo export USER_WELDWB_srcDir="'"/home/mbgm6aab/Documents/weldingworkbench"'" >> user.config
cat user.config

else
echo 'File does exist'
fi

####################################################################################################################
### Set environment variables
####################################################################################################################
source user.config

####################################################################################################################
### Launch Workbench
####################################################################################################################
python ./GUI/boiler.py &
