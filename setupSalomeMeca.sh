#!/bin/bash

######################################
# Author: Jefri Draup                #
# Email: jefri.draup@edfenergy.com   #
######################################


ask_where_to_fetch_salome=$(zenity  --list  --text "Default locations: Where to fetch Salome_Meca version?" --checklist  --column "Pick" --column "options" FALSE "$HOME/" TRUE "$HOME/salome_meca" FALSE "/opt/" FALSE "/opt/aster/bin" FALSE "/media/$USER/"  --separator="*    ")
echo $ask_where_to_fetch_salome
        

ADD_FOLDERS=""
while  zenity --question --text="Add A new location to find Salome_Meca on your machine?" 
do
   ADD_FOLDER=`zenity --file-selection   --directory   --title="Select the location"`
   ADD_FOLDERS=$( echo "$ADD_FOLDERS     $ADD_FOLDER" )
   echo $ADD_FOLDERS
done

search_salome=$( find    $ADD_FOLDERS  $ask_where_to_fetch_salome -name  appli_V* -type d )
echo $search_salome



search_salome=$(find    $ADD_FOLDERS  $ask_where_to_fetch_salome -name  appli_V* -type d)
compt_salome=0
list_salome_meca=()

for d in $search_salome; do
	compt_salome=`expr $compt_salome + 1`
	echo "Salome_meca Research Result: "$compt_salome "-->" $d
	if [ $compt_salome == 1 ] 
	then

#       echo $d > tmpSearchSalome &&  testSalome=$(awk '{print $NF}' FS='/' tmpSearchSalome)
		echo $d > tmpSearchSalome 
	else
#       echo $d >> tmpSearchSalome &&  testSalome=$(awk '{print $NF}' FS='/' tmpSearchSalome)
		echo $d >> tmpSearchSalome 
	fi
	list_salome_meca+=($d)
done

#   echo $compt_salome

#### Sereral versions of salome found
if [ $compt_salome -gt 1 ]
then 
	echo $compt_salome " versions of installed salome_meca have been found on your machine"
	echo
	echo "-------------------------------"
	echo "LIST OF INSTALLED SALOME_MECA :"
	echo ${list_salome_meca[@]}
	echo "-------------------------------"
		linenumber=$(awk '{print NR};1' tmpSearchSalome | zenity --list --column="Version" \
	--column="Salome_meca 2019 is the current pre-requisite" --text="Select version " \
	--title="Salome_meca versions found on your Computer" --hide-column=1)
		linecontent=$(sed ${linenumber}'!d;q' tmpSearchSalome)
		
	
	echo $linecontent
	
	
	
	linecontent=$(sed ${linenumber}'!d;q' tmpSearchSalome)

	search_salome=$linecontent
fi
#### 1 version of salome found
if [ $compt_salome == 1 ]
then
	search_salome=${list_salome_meca[0]}

	echo $compt_salome " version of installed salome_meca has been found"
	echo "-------------------------------"
	echo "INSTALLED SALOME_MECA :"
		echo $search_salome
	echo "-------------------------------"
fi
echo "search_salome" $search_salome
echo $search_salome > tmpSearchSalome &&  testSalome=$(awk '{print $NF}' FS='/' tmpSearchSalome)

#### No version of salome
#---------------------------------
if [ $compt_salome == 0 ]
then 
	zenity --warning --text="No Version of Salome_meca has been found on your computer"
	#if zenity --question --text="Do you want to install $proposedSalome_Version";
	#then
	#	cd $INSTALLATION_PATH
	#	Salome_Archive=$proposedSalome_Version'.tgz'  
	#	tar -xvf $Salome_Archive
	#	search_salome_run=$(find -name  *.run)
	#	echo $search_salome_run
	#	chmod 777 $search_salome_run
	#	$search_salome_run
	#	rm $search_salome_run
	#	cd $GRAPHITE_WORKBENCHROOT
	#	search_salome=$(find $HOME/* -name  appli_V* -type d)
	#else

		zenity --info --text ="Without salome_meca you CAN'T use the WORBKENCH.\n Please install salome_meca 2019 from https://www.code-aster.org/spip.php?article303"
	#	exit 32
	#fi
fi

rm -rf user.config
echo export USER_WELDWB_pathToSalome="'"$search_salome"'" >> user.config
echo export USER_WELDWB_pathToHere="$""("" pwd "")" >> user.config
echo export USER_WELDWB_srcDir="\$USER_WELDWB_pathToHere" >> user.config

./modifyUser.config.sh
./modifyExportPath.sh

