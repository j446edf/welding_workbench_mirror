#!/bin/bash

. ../user.config

export USER_WELDWB_srcDir

USER_INP_RESU_FILE=$resu
export USER_INP_RESU_FILE

#./modifyErrorExport.sh
cd $USER_WELDWB_srcDir/postprocessing
sed -i "s@R base.*@R base $USER_INP_RESU_FILE DC 0@g" project.export


unset USER_INP_RESU_FILE
