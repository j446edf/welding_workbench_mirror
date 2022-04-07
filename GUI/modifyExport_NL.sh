#!/bin/bash

. ../user.config

export USER_WELDWB_srcDir

USER_INP_FILE=$dynamic_inp
FILE_NO=$file_no_exp
export USER_INP_FILE
export FILE_NO

#echo $USER_WELDWB_srcDir$USER_INP_FILE > outputMe

cd $USER_WELDWB_srcDir/templates
sed -i "s@.*D $FILE_NO.*@F libr $USER_WELDWB_srcDir$USER_INP_FILE D $FILE_NO@g" nonlinearthermal.export
#sed -i "s@.*D $FILE_NO.*@F libr $USER_WELDWB_srcDir$USER_INP_FILE D $FILE_NO@g" steadystate.export

unset USER_INP_FILE
unset FILE_NO
