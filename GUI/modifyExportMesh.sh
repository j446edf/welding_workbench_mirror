#!/bin/bash

. ../user.config

export USER_WELDWB_srcDir

USER_INP_FILE=$model
export USER_INP_FILE

#echo $USER_WELDWB_srcDir$USER_INP_FILE > outputMe

cd $USER_WELDWB_srcDir/templates
sed -i "s@.*D 20.*@F mmed $USER_WELDWB_srcDir$USER_INP_FILE D 20@g" nonlinearthermal.export
sed -i "s@.*D 20.*@F mmed $USER_WELDWB_srcDir$USER_INP_FILE D 20@g" steadystate.export

unset USER_INP_FILE

