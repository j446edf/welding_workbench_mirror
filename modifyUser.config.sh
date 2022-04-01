#!/bin/bash
source user.config
export USER_WELDWB_srcDir
echo $USER_WELDWB_srcDir >> outputMe
sed -i "s@export USER_WELDWB_srcDir.*@export USER_WELDWB_srcDir='$USER_WELDWB_srcDir'@g" user.config

