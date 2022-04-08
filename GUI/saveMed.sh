#!/bin/bash

. ../user.config

export USER_WELDWB_srcDir

USER_INP_FILE=$mesh_file
USER_SAVE_FILE=$input
export USER_INP_FILE
export USER_SAVE_FILE

echo $USER_SAVE_FILE >> outputMe

cp $USER_WELDWB_srcDir$USER_INP_FILE $USER_SAVE_FILE

unset USER_INP_FILE
unset USER_SAVE_FILE
