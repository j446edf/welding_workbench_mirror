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
export pathToSalome='/home/mbgm6aab/salome_meca/appli_V2019.0.3_universal'
export pathToHere=$( pwd )
export srcDir='/home/mbgm6aab/Documents/weldingworkbench'
####################################################################################################################
####################################################################################################################

rm -r $srcDir/simulation/tmp
mkdir $srcDir/simulation/tmp

####################################################################################################################
### Build Mesh
####################################################################################################################
#$pathToSalome/salome -t $pathToHere/buildGeom.py
#$pathToSalome/salome shell killSalome.py		

####################################################################################################################
### Launch simulation
####################################################################################################################
pushd $srcDir/simulation/tmp
cp $srcDir/templates/* .
$pathToSalome/salome shell -- as_run $srcDir/simulation/tmp/steadystate.export
$pathToSalome/salome shell killSalome.py		

####################################################################################################################
### END
####################################################################################################################
unset pathToSalome
unset pathToHere
unset srcDir

