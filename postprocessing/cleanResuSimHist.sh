#!/bin/bash

######################################
# Author: Jefri Draup                #
# Email: jefri.draup@edfenergy.com   #
######################################

# Please refer to README:
# https://gitlab.cs.man.ac.uk/mbgm6aab/st_int_2021/blob/master/tg8/README

#export pathToSalome='/home/mbgm6aab/salome_meca/appli_V2019.0.3_universal'
export pathToHere=$( pwd )

# Clean old .csv
rm $pathToHere/mergeT_Pass_*.csv

#### Run for each pass ########################
###############################################


for pn in $(seq 1 1) # <------------------------------- We use 5 passes in TG8. You need to set appropriate database in test2.py
do
export passNumber=$pn
#### Run for each TC ###################
########################################

for tc in $(seq 1 $USER_INP_NO_OF_TC) # <------------------------------- We use 6 TC from TG8. The coordinates are set in test2.py
do
export tcNumber=$tc
echo 'Extracting weld pass ' $pn 'TC ' $tc
touch $pathToHere/mergeT_Pass_${pn}_TC${tc}.csv
echo '"arc_length"','"THNONLI2TEMP"' >> $pathToHere/mergeT_Pass_${pn}_TC${tc}.csv

### Run for each sim timestep #####
###################################


sed -i "s/fileToRead=.*/fileToRead=$tc/g" createCSV.py
sed -i "s/passToRead=.*/passToRead=$pn/g" createCSV.py
python3 $pathToHere/createCSV.py

unset tcNumber
###################################
###################################

done

##########################################
##########################################
unset passNumber
done

###############################################
###############################################

#unset pathToSalome
#unset pathToHere
ls -ltr
