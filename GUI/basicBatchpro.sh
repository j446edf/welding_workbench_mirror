#!/bin/bash -
#Creating a batch job on CSF
echo === PROGRAM STARTED === >>outputMe

##########################################################
#     USER INPUTS ########################################
##########################################################
#export USER_INP_T_aust=1450. 
#export USER_INP_T_end=20. 
#export USER_INP_GS=9.

#export XDG_RUNTIME_DIR=/run/user/$USER
export USER_INP_T_aust=$T_A
export USER_INP_T_end=$T_E
export USER_INP_GS=$G_S

##<<<<<<< HEAD
#export USER_INP_coolingPlates=(0.1 2.)
##export myArray=(one two three four [5]=five)

##echo "${myArray[*]}"
##echo "${USER_INP_coolingPlates[*]}"
##unset myArray
###(0.01, 0.1, 1., 10.,  50., 100., 200., 300., 400.,)
##echo $USER_INP_coolingPlates
##=======
#export USER_INP_coolingPlates=(0.01,0.1)
## 1., 10.,  50., 100., 200., 300., 400.,)
##>>>>>>> e55cf88b2cf7ba4243818ce5abb8911293e1ad0c
#export USER_INP_grainGrowthMethod="IKAWA" #CONSTANT #TWORATE
#export USER_INP_material="SA508" #4140 #16MND5
#export USER_INP_ae13CHOICE="Grange" #Andrews #Eldis
export USER_INP_coolingPlates=$C_R
export USER_INP_grainGrowthMethod=$GG_M
export USER_INP_material=$M
export USER_INP_userMaterial=$USER_M
export USER_INP_ae13CHOICE=$A_M

##Plotting options
#export USER_INP_CCTplot='Yes' 
#export USER_INP_TTTplot='Yes'
export USER_INP_CCTplot=$CCT
export USER_INP_TTTplot=$TTT

rm -f outputMe
echo Austenisation temp is $T_A >>outputMe
echo Austenisation temp is $USER_INP_T_aust >>outputMe
echo End temp is $T_E >>outputMe
echo $USER_INP_T_end >>outputMe
echo Grain size is $G_S >>outputMe
echo $USER_INP_GS>>outputMe
echo Cooling rates are $C_R >>outputMe
echo $USER_INP_coolingPlates >>outputMe
echo Grain Grwoth Method is $GG_M >>outputMe
echo $USER_INP_grainGrowthMethod >>outputMe
echo Material is $M >>outputMe
echo $USER_INP_material >> outputMe
echo AE13 Method is $A_M >>outputMe
echo $USER_INP_ae13CHOICE >> outputMe
echo $CCT >>outputMe
echo $TTT >>outputMe
echo $USER_INP_CCTplot >>outputMe
echo $USER_INP_TTTplot >>outputMe

#######################################################################



##########################################################################
# Greates a CCT.66 file compatible with code_aster
##########################################################################
#echo "=== Generating new CCT (Jefri) ===";
python3 digitiseCCTpro.py "${USER_INP_coolingPlates[@]}" "${USER_INP_userMaterial[@]}"
#ls -ltr
###########################################################################



############################################################################
#### Plots CCT diagram for your material
############################################################################
if [ $USER_INP_CCTplot == "Yes" ]
then
	echo "=== Plot CCT (Jefri) ==="
	python3 createCCTpro.py "${USER_INP_coolingPlates[@]}"
	##python2 createCCT.py

fi
############################################################################



############################################################################
#### Plots TTT diagram for your material
############################################################################
if [ $USER_INP_TTTplot == "Yes" ]
then
	#echo "=== Plot TTT (Jefri) ==="
	python3 createTTTpro.py "${USER_INP_coolingPlates[@]}"
fi
############################################################################



unset USER_INP_T_aust
unset USER_INP_T_end
unset USER_INP_GS
unset USER_INP_coolingPlates
unset USER_INP_grainGrowthMethod
unset USER_INP_material
unset USER_INP_userMaterial
unset USER_INP_ae13CHOICE
unset USER_INP_CCTplot
unset USER_INP_TTTplot

echo === PROGRAM ENDED === >>outputMe

