#!/bin/bash

. ../user.config

export USER_WELDWB_srcDir

USER_INP_RESU_FILE=$resu
export USER_INP_RESU_FILE

./modifyErrorExport.sh

unset USER_INP_RESU_FILE
