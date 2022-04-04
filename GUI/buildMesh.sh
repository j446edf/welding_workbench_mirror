#!/bin/bash

. ../user.config

export USER_WELDWB_srcDir

USER_INP_GEOM=$geom
export USER_INP_GEOM

cd $USER_WELDWB_srcDir/meshing

if [ $USER_INP_GEOM = "0" ]
then
	USER_INP_A=$ewb_a
	USER_INP_B=$ewb_b
	USER_INP_C=$ewb_c
	USER_INP_D=$ewb_d
	USER_INP_E=$ewb_e
	USER_INP_F=$ewb_f
	USER_INP_G=$ewb_g
	USER_INP_H=$ewb_h
	USER_INP_I=$ewb_i
	USER_INP_J=$ewb_j
	USER_INP_K=$ewb_k
	USER_INP_L=$ewb_l
	USER_INP_M=$ewb_m
	
	export USER_INP_A
	export USER_INP_B
	export USER_INP_C
	export USER_INP_D
	export USER_INP_E
	export USER_INP_F
	export USER_INP_G
	export USER_INP_H
	export USER_INP_I
	export USER_INP_J
	export USER_INP_K
	export USER_INP_L
	export USER_INP_M
	
	$USER_WELDWB_pathToSalome/salome shell killSalome.py
	$USER_WELDWB_pathToSalome/salome $USER_WELDWB_srcDir/meshing/Edge_Welded_Beam_curved.py &
	$USER_WELDWB_pathToSalome/salome shell killSalome.py
	unset USER_INP_GEOM
	unset USER_INP_A
	unset USER_INP_B
	unset USER_INP_C
	unset USER_INP_D
	unset USER_INP_E
	unset USER_INP_F
	unset USER_INP_G
	unset USER_INP_H
	unset USER_INP_I
	unset USER_INP_J
	unset USER_INP_K
	unset USER_INP_L
	unset USER_INP_M
	echo 'Edge Welded Beam Mesh Built'
	echo 'Location: '$USER_WELDWB_srcDir'/meshing/Edge_Welded_Beam_fromGUI.med'
fi
