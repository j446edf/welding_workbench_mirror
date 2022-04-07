#!/bin/bash
. ../user.config

USER_INP_SIM=$sim_type

cd $USER_WELDWB_srcDir/simulation


if [ $USER_INP_SIM = "0" ]
then
./runSimulation.sh
else
./runSimulation2.sh
fi
