#!/usr/bin/env python

###
### This file is generated automatically by SALOME v9.3.0 with dump python functionality
###

import os
import sys
import salome

salome.salome_init()
import salome_notebook
notebook = salome_notebook.NoteBook()

################# USER INPUTS ##############################################
pathToWorkbench=os.getenv('USER_WELDWB_srcDir')
pathToMeshing=pathToWorkbench+'/meshing'
print(pathToMeshing)
TC_LOCS_str=os.getenv('USER_INP_TC_LOCS')
TC_LOCS_strip = TC_LOCS_str.strip('()[]')
TC_LOCS_strip = TC_LOCS_strip.split(',')
TC_LOCS_list=[float(i) for i in TC_LOCS_strip]
no_of_TC=int(float(os.getenv('USER_INP_NO_OF_TC')))
TC_LOCS = []
for i in range(no_of_TC):
	TC = []
	TC = [TC_LOCS_list[3*i], TC_LOCS_list[(3*i)+1], TC_LOCS_list[(3*i)+2]]
	TC_LOCS.append(TC)
print(TC_LOCS)
#TC_LOCS = [[10.,0.,0.],[12.,0.,0.],[15.,0.,0.],[18.,0.,0.],[20.,0.,0.]]

############################################################################

sys.path.insert(0, r''+pathToMeshing)






###
### GEOM component
###

import GEOM
from salome.geom import geomBuilder
import math
import SALOMEDS


geompy = geomBuilder.New()


O = geompy.MakeVertex(0, 0, 0)
OX = geompy.MakeVectorDXDYDZ(1, 0, 0)
OY = geompy.MakeVectorDXDYDZ(0, 1, 0)
OZ = geompy.MakeVectorDXDYDZ(0, 0, 1)


geompy.addToStudy( O, 'O' )
geompy.addToStudy( OX, 'OX' )
geompy.addToStudy( OY, 'OY' )
geompy.addToStudy( OZ, 'OZ' )



TC_VERTS = []
for i in range(0,len(TC_LOCS)):
	TC_VERTS.append(geompy.MakeVertex(TC_LOCS[i][0], TC_LOCS[i][1], TC_LOCS[i][2]))
	geompy.addToStudy( TC_VERTS[i], 'TC_VERTS_'+str(i+1) )


# Cube relative vertices
cube_verts = [[-0.5,0.5,-0.5],[0.5,0.5,-0.5],[0.5,-0.5,-0.5],[-0.5,-0.5,-0.5],[-0.5,0.5,0.5],[0.5,0.5,0.5],[0.5,-0.5,0.5],[-0.5,-0.5,0.5]]

# Loop through TC_LOCS and create cubes
TC_CUBES=[]
for i in range(0,len(TC_LOCS)):
	TC_CUBES.append(geompy.MakeBoxDXDYDZ(1, 1, 1))
	geompy.TranslateDXDYDZ(TC_CUBES[i], TC_LOCS[i][0]-0.5, TC_LOCS[i][1]-0.5, TC_LOCS[i][2]-0.5)
	geompy.addToStudy( TC_CUBES[i], 'TC_CUBES_'+str(i+1) )


###
### SMESH component
###

import  SMESH, SALOMEDS
from salome.smesh import smeshBuilder

smesh = smeshBuilder.New()

TC_MESHES=[]
Regular_1D=[]
Number_of_Segments_1=[]
Quadrangle_2D=[]
Hexa_3D=[]
for i in range(0,len(TC_LOCS)):
	TC_MESHES.append(smesh.Mesh(TC_CUBES[i]))
	Regular_1D.append(TC_MESHES[i].Segment())
	Number_of_Segments_1.append(Regular_1D[i].NumberOfSegments(2))
	Quadrangle_2D.append(TC_MESHES[i].Quadrangle(algo=smeshBuilder.QUADRANGLE))
	Hexa_3D.append(TC_MESHES[i].Hexahedron(algo=smeshBuilder.Hexa))
	isDone = TC_MESHES[i].Compute()
	smesh.SetName(Regular_1D[i].GetAlgorithm(), 'Regular_1D_'+str(i+1))
	smesh.SetName(Hexa_3D[i].GetAlgorithm(), 'Hexa_3D_'+str(i+1))
	smesh.SetName(Quadrangle_2D[i].GetAlgorithm(), 'Quadrangle_2D_'+str(i+1))
	smesh.SetName(Number_of_Segments_1[i], 'Number of Segments_1_'+str(i+1))
	smesh.SetName(TC_MESHES[i].GetMesh(), 'Mesh_'+str(i+1))
	
	
	aCriteria = []
	aCriterion = smesh.GetCriterion(SMESH.NODE,SMESH.FT_BelongToGeom,SMESH.FT_Undefined,TC_VERTS[i])
	aCriteria.append(aCriterion)
	aFilter_1 = smesh.GetFilterFromCriteria(aCriteria)
	aFilter_1.SetMesh(TC_MESHES[i].GetMesh())
	Group_1 = TC_MESHES[i].GroupOnFilter( SMESH.NODE, 'Group_TC', aFilter_1 )


for i in range(0,len(TC_LOCS)):
	try:
		TC_MESHES[i].ExportMED(r''+pathToMeshing+'/TCMESH_'+str(i+1)+'.med',auto_groups=1,minor=40,overwrite=1,meshPart=None,autoDimension=1)
		pass
	except:
		print('ExportMED() failed. Invalid file name?')

if salome.sg.hasDesktop():
  salome.sg.updateObjBrowser()
