#!/usr/bin/env python

###
### This file is generated automatically by SALOME v9.3.0 with dump python functionality
###

import os,sys
import salome

salome.salome_init()
theStudy = salome.myStudy                      #2018
import salome_notebook
notebook = salome_notebook.NoteBook()
sys.path.insert(0, r'/home/talha/Documents')

###
### GEOM component
###

import GEOM
from salome.geom import geomBuilder
import math
import SALOMEDS

#Inputs
#Base plate (Full)
l = 250 #Base plate length
h = 70 #Base plate height
th = 10 #Base plate thickness

#Weld pasess
pl = 250 #Weld pass length
ph = 8 #Weld pass height
pth = 10 #Weld pass thickness

geompy = geomBuilder.New()

O = geompy.MakeVertex(0, 0, 0)
OX = geompy.MakeVectorDXDYDZ(1, 0, 0)
OY = geompy.MakeVectorDXDYDZ(0, 1, 0)
OZ = geompy.MakeVectorDXDYDZ(0, 0, 1)


A = geompy.MakeVertex(-th/2, 0, 0)
B = geompy.MakeVertex(-th/2, h, 0)
C = geompy.MakeVertex(th/2, h, 0)
D = geompy.MakeVertex(th/2, 0, 0)

W1 = geompy.MakeVertex(-th/2, h+ph, 0)
W2 = geompy.MakeVertex(-(th/3), (h+ph)+(2*th/12), 0)
W3 = geompy.MakeVertex(0, (h+ph)+(th/4), 0)
W4 = geompy.MakeVertex((th/3), (h+ph)+(2*th/12), 0)
W5 = geompy.MakeVertex(th/2, h+ph, 0)

AB = geompy.MakeLineTwoPnt(A, B)
BC = geompy.MakeLineTwoPnt(B, C)
CD = geompy.MakeLineTwoPnt(C, D)
AD = geompy.MakeLineTwoPnt(A, D)
Side = geompy.MakeCompound([AB, CD])
Weld_L = geompy.MakeLineTwoPnt(B, W1)
Weld_R = geompy.MakeLineTwoPnt(C, W5)
Arc_1 = geompy.MakeArc(W1, W2, W3)
Arc_2 = geompy.MakeArc(W3, W4, W5)
Weld_Top = geompy.MakeCompound([Arc_1, Arc_2])
Weld_Across = geompy.MakeCompound([BC, Weld_Top])
Weld_Side = geompy.MakeCompound([Weld_L, Weld_R])
Parent = geompy.MakeFaceWires([AB, BC, CD, AD], 1)
Weld = geompy.MakeFaceWires([BC, Weld_L, Arc_1, Arc_2, Weld_R], 1)

Parent_extrude = geompy.MakePrismVecH2Ways(Parent, OZ, (l/2))
Weld_extrude = geompy.MakePrismVecH2Ways(Weld, OZ, (l/2))

geompy.addToStudy( O, 'O' )
geompy.addToStudy( OX, 'OX' )
geompy.addToStudy( OY, 'OY' )
geompy.addToStudy( OZ, 'OZ' )
geompy.addToStudy( A, 'A' )
geompy.addToStudy( B, 'B' )
geompy.addToStudy( C, 'C' )
geompy.addToStudy( D, 'D' )
geompy.addToStudy( W1, 'W1' )
geompy.addToStudy( W2, 'W2' )
geompy.addToStudy( W3, 'W3' )
geompy.addToStudy( AB, 'AB' )
geompy.addToStudy( BC, 'BC' )
geompy.addToStudy( CD, 'CD' )
geompy.addToStudy( AD, 'AD' )
geompy.addToStudy(Side, 'Side')
geompy.addToStudy( Arc_1, 'Arc_1' )
geompy.addToStudy( Arc_2, 'Arc_2' )
geompy.addToStudy( Weld_Top, 'Weld_Top' )
geompy.addToStudy( Weld_Side, 'Weld_Side' )
geompy.addToStudy( Weld_Across, 'Weld_Across' )
geompy.addToStudy( Parent, 'Parent' )
geompy.addToStudy( Weld, 'Weld' )
geompy.addToStudy( Parent_extrude, 'Parent_extrude' )
geompy.addToStudy( Weld_extrude, 'Weld_extrude' )


Full = geompy.MakePartition([Parent, Weld], [], [], [], geompy.ShapeType["FACE"], 0, [], 0)
geompy.addToStudy( Full, 'Full' )

geompy.addToStudyInFather(Full, Weld, 'Weld')
geompy.addToStudyInFather(Full, Parent, 'Parent' )

Edge_Base = geompy.GetInPlace(Full, AD)
Edge_Side = geompy.GetInPlace(Full, Side)
Edge_Weld_Base = geompy.GetInPlace(Full, Weld_Across)
Edge_Weld_Side = geompy.GetInPlace(Full, Weld_Side)

geompy.addToStudyInFather( Full, Edge_Base, 'Edge_Base')
geompy.addToStudyInFather( Full, Edge_Side, 'Edge_Side')
geompy.addToStudyInFather( Full, Edge_Weld_Base, 'Edge_Weld_Base')
geompy.addToStudyInFather( Full, Edge_Weld_Side, 'Edge_Weld_Side')

#Groups for Computations(weld, Full, conduction, convection, radiation)
#Geometry for mesh groups
#Base plate base Surface
A1 = geompy.MakeVertex(-th/2, 0, -l/2)
A2 = geompy.MakeVertex(-th/2, 0, l/2)
D2 = geompy.MakeVertex(th/2, 0, l/2)
D1 = geompy.MakeVertex(th/2, 0, -l/2)
AA = geompy.MakeLineTwoPnt(A1, A2)
AD_1 = geompy.MakeLineTwoPnt(A1, D1)
DD = geompy.MakeLineTwoPnt(D1, D2)
AD_2 = geompy.MakeLineTwoPnt(A2, D2)
Base_Face = geompy.MakeFaceWires([AA, AD_1, DD, AD_2], 1)
geompy.addToStudy( Base_Face, 'Base_Face' )

# Upstream/Downstream
Upstream = geompy.MakeTranslationVectorDistance(Parent, OZ, -l/2)
Downstream = geompy.MakeTranslationVectorDistance(Parent, OZ, l/2)
geompy.addToStudy( Upstream, 'Upstream' )
geompy.addToStudy( Downstream, 'Downstream' )



###
### END GEOM component
###


###
### SMESH component
###

import  SMESH, SALOMEDS
from salome.smesh import smeshBuilder

from salome.StdMeshers import StdMeshersBuilder
smesh = smeshBuilder.New()

# Meshing parameters
Mesh_Weld = smesh.Mesh(Full)
Quadrangle_2D = Mesh_Weld.Quadrangle(algo=smeshBuilder.QUADRANGLE)
Quadrangle_Parameters_WELD = Quadrangle_2D.QuadrangleParameters(StdMeshersBuilder.QUAD_REDUCED,0,[],[])


def round_up_to_even(f):
    return math.ceil(f / 2.) * 2

######## User Inputs Meshing ########
#Weld
Mesh_a = 8 #Number of elements along Weld width
Mesh_b = 8 #Number of elements along weld height

#Base plate
Mesh_c = 6 #Number of elements along base plate width (bottom edge)
Mesh_d = 30 #Number of elements along base plate height
D_d = [ 0, 0.5, 0.3, 1, 0.5, 3, 0.7, 1, 1, 0.5 ] # Density distribution [x1, density1, x2, density2, x3, density3, ...] (x from 0 to 1)
# change density distribution for refinement at top of base plate

Mesh_a_corrected = round_up_to_even(Mesh_a)
Mesh_c_corrected = round_up_to_even(Mesh_c)

# weld meshing
#########################
Regular_1D = Mesh_Weld.Segment(geom=Edge_Weld_Base)
Number_of_Segments_Weld_Base = Regular_1D.NumberOfSegments(Mesh_a_corrected,None,[])

Regular_1D_1 = Mesh_Weld.Segment(geom=Edge_Weld_Side)
Number_of_Segments_Weld_Side = Regular_1D_1.NumberOfSegments(Mesh_b,None,[])


#Parent meshing
#########################
#Horizontal edges
Regular_1D_2 = Mesh_Weld.Segment(geom=Edge_Base)
Number_of_Segments_Base = Regular_1D_2.NumberOfSegments(Mesh_c_corrected,None,[])

Regular_1D_3 = Mesh_Weld.Segment(geom=Edge_Side)
Number_of_Segments_Side = Regular_1D_3.NumberOfSegments(Mesh_d,None,[])



# weld sub-meshing
Sub_mesh = Regular_1D.GetSubMesh()
Sub_mesh_A = Regular_1D_1.GetSubMesh()
Sub_mesh_B = Regular_1D_2.GetSubMesh()
Sub_mesh_C = Regular_1D_3.GetSubMesh()

isDone = Mesh_Weld.Compute()



#translate, extrude, concatenate & mirror mesh
Fine_mm =1 #element length in fine zone
Fine_l = 10 #distance from centre in z of end of fine zone (0 < Fine_l < l/2)
Fine = int(Fine_l/Fine_mm)

Coarse1_mm = 2 #element length in first coarse zone
Coarse1_l = 60 #distance from centre in z of end of first coarse zone(Fine_l < Coarse1_l < l/2
Coarse1 = int((Coarse1_l-Fine_l)/Coarse1_mm)

Coarse2_mm = 5 #element length in second coarse zone (up to end of weld)
Coarse2 = int(((l/2)-Coarse1_l)/Coarse2_mm)

Mesh_WELD_translated = Mesh_Weld.TranslateObjectMakeMesh( Mesh_Weld, [ 0, 0, Fine_l ], 1, 'Mesh_WELD_translated' )
Mesh_WELD_translated_2 = Mesh_Weld.TranslateObjectMakeMesh( Mesh_Weld, [ 0, 0, Coarse1_l ], 1, 'Mesh_WELD_translated' )
Mesh_Weld.ExtrusionSweepObjects( [ Mesh_Weld ], [ Mesh_Weld ], [ Mesh_Weld ], [ 0, 0, Fine_mm ], Fine, 1 )
Mesh_WELD_translated.ExtrusionSweepObjects( [ Mesh_WELD_translated ], [ Mesh_WELD_translated ], [ Mesh_WELD_translated ], [ 0, 0, Coarse1_mm ], Coarse1, 1 )
Mesh_WELD_translated_2.ExtrusionSweepObjects( [ Mesh_WELD_translated_2 ], [ Mesh_WELD_translated_2 ], [ Mesh_WELD_translated_2 ], [ 0, 0, Coarse2_mm ], Coarse2, 1 )
Mesh_WELDSym = smesh.Concatenate([Mesh_Weld.GetMesh(),Mesh_WELD_translated.GetMesh(),Mesh_WELD_translated_2.GetMesh()], 1, 1, 1e-05, False, name='Mesh_WELDSym')
Mesh_WELDSymMirr = Mesh_WELDSym.MirrorObjectMakeMesh(Mesh_WELDSym,geompy.MakePlane(O,OZ,100.),SMESH.SMESH_MeshEditor.PLANE, 1 ,'Mesh_WELDSymMirr')
Mesh_Weld_3D = smesh.Concatenate([Mesh_WELDSym.GetMesh(),Mesh_WELDSymMirr.GetMesh()], 1, 1, 1e-05, False, name='Mesh_Weld_3D')

isDone = Mesh_Weld_3D.Compute()



# Groups for steadystate/non-linear computations
# Parent
aCriteria = []
aCriterion = smesh.GetCriterion(SMESH.VOLUME,SMESH.FT_BelongToGeom,SMESH.FT_Undefined,Parent_extrude,SMESH.FT_Undefined,1e-7)
aCriteria.append(aCriterion)
aFilter = smesh.GetFilterFromCriteria(aCriteria)
aFilter.SetMesh(Mesh_Weld_3D.GetMesh())
Group_parent = Mesh_Weld_3D.GroupOnFilter( SMESH.VOLUME, 'Group_parent', aFilter )

# Weld
aCriteria = []
aCriterion = smesh.GetCriterion(SMESH.VOLUME,SMESH.FT_BelongToGeom,SMESH.FT_Undefined,Weld_extrude,SMESH.FT_Undefined,1e-7)
aCriteria.append(aCriterion)
aFilter = smesh.GetFilterFromCriteria(aCriteria)
aFilter.SetMesh(Mesh_Weld_3D.GetMesh())
Group_weld = Mesh_Weld_3D.GroupOnFilter( SMESH.VOLUME, 'Group_weld', aFilter )

#Group_All
aCriteria = []
aCriterion = smesh.GetCriterion(SMESH.VOLUME,SMESH.FT_BelongToMeshGroup,SMESH.FT_Undefined,Group_weld,SMESH.FT_Undefined,SMESH.FT_LogicalOR)
aCriteria.append(aCriterion)
aCriterion = smesh.GetCriterion(SMESH.VOLUME,SMESH.FT_BelongToMeshGroup,SMESH.FT_Undefined,Group_parent)
aCriteria.append(aCriterion)
aFilter = smesh.GetFilterFromCriteria(aCriteria)
aFilter.SetMesh(Mesh_Weld_3D.GetMesh())
Group_Of_All_Volumes = Mesh_Weld_3D.GroupOnFilter( SMESH.VOLUME, 'Group_Of_All_Volumes', aFilter )

#Group_Conduction
aCriteria = []
aCriterion = smesh.GetCriterion(SMESH.FACE,SMESH.FT_BelongToGeom,SMESH.FT_Undefined,Base_Face,SMESH.FT_Undefined)
aCriteria.append(aCriterion)
aFilter = smesh.GetFilterFromCriteria(aCriteria)
aFilter.SetMesh(Mesh_Weld_3D.GetMesh())
Group_conduction = Mesh_Weld_3D.GroupOnFilter( SMESH.FACE, 'Group_conduction', aFilter )

#Group_Convection
aCriteria = []
aCriterion = smesh.GetCriterion(SMESH.FACE,SMESH.FT_FreeFaces,SMESH.FT_Undefined,0,SMESH.FT_Undefined,SMESH.FT_LogicalAND)
aCriteria.append(aCriterion)
aCriterion = smesh.GetCriterion(SMESH.FACE,SMESH.FT_BelongToGeom,SMESH.FT_Undefined,Base_Face,SMESH.FT_LogicalNOT)
aCriteria.append(aCriterion)
aFilter = smesh.GetFilterFromCriteria(aCriteria)
aFilter.SetMesh(Mesh_Weld_3D.GetMesh())
Group_convection = Mesh_Weld_3D.GroupOnFilter( SMESH.FACE, 'Group_convection', aFilter )

#Group_Radiation
aCriteria = []
aCriterion = smesh.GetCriterion(SMESH.FACE,SMESH.FT_FreeFaces,SMESH.FT_Undefined,0,SMESH.FT_Undefined,SMESH.FT_LogicalAND)
aCriteria.append(aCriterion)
aCriterion = smesh.GetCriterion(SMESH.FACE,SMESH.FT_BelongToGeom,SMESH.FT_Undefined,Base_Face,SMESH.FT_LogicalNOT)
aCriteria.append(aCriterion)
aFilter = smesh.GetFilterFromCriteria(aCriteria)
aFilter.SetMesh(Mesh_Weld_3D.GetMesh())
Group_radiation = Mesh_Weld_3D.GroupOnFilter( SMESH.FACE, 'Group_radiation', aFilter )

#Group_Upstream
aCriteria = []
aCriterion = smesh.GetCriterion(SMESH.FACE,SMESH.FT_BelongToGeom,SMESH.FT_Undefined,Upstream,SMESH.FT_Undefined)
aCriteria.append(aCriterion)
aFilter = smesh.GetFilterFromCriteria(aCriteria)
aFilter.SetMesh(Mesh_Weld_3D.GetMesh())
Group_upstream = Mesh_Weld_3D.GroupOnFilter( SMESH.FACE, 'Group_upstream', aFilter )

#Group_Downstream
aCriteria = []
aCriterion = smesh.GetCriterion(SMESH.FACE,SMESH.FT_BelongToGeom,SMESH.FT_Undefined,Downstream,SMESH.FT_Undefined)
aCriteria.append(aCriterion)
aFilter = smesh.GetFilterFromCriteria(aCriteria)
aFilter.SetMesh(Mesh_Weld_3D.GetMesh())
Group_downstream = Mesh_Weld_3D.GroupOnFilter( SMESH.FACE, 'Group_downstream', aFilter )



smesh.SetName(Number_of_Segments_Weld_Base, 'Number of Segments_Weld_Base')
smesh.SetName(Number_of_Segments_Weld_Side, 'Number of Segments_Weld_Side')
smesh.SetName(Number_of_Segments_Base, 'Number of Segments_Base')
smesh.SetName(Number_of_Segments_Side, 'Number of Segments_Side')

smesh.SetName(Sub_mesh, 'Sub-mesh')
smesh.SetName(Sub_mesh_A, 'Sub-mesh_A')
smesh.SetName(Sub_mesh_B, 'Sub-mesh_B')
smesh.SetName(Sub_mesh_C, 'Sub-mesh_C')

smesh.SetName(Quadrangle_2D.GetAlgorithm(), 'Quadrangle_2D')
smesh.SetName(Regular_1D.GetAlgorithm(), 'Regular_1D')
smesh.SetName(Quadrangle_Parameters_WELD, 'Quadrangle Parameters_WELD')
smesh.SetName(Mesh_Weld.GetMesh(), 'Mesh_Weld')
smesh.SetName(Mesh_Weld_3D.GetMesh(), 'Mesh_Weld_3D')

if salome.sg.hasDesktop():
  salome.sg.updateObjBrowser()

