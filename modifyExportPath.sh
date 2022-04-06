#!/bin/bash

source user.config

export USER_WELDWB_srcDir

cd $USER_WELDWB_srcDir/templates

sed -i "s@ReplaceMe@$USER_WELDWB_srcDir@g" nonlinearthermal.export
sed -i "s@ReplaceMe@$USER_WELDWB_srcDir@g" steadystate.export

cd $USER_WELDWB_srcDir/postprocessing
sed -i "s@ReplaceMe@$USER_WELDWB_srcDir@g" project.export
