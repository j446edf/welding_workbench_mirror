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


#Base plate (Parent)
A = geompy.MakeVertex(0, 0, 0)
B = geompy.MakeVertex(0, 0, h)
C = geompy.MakeVertex(l, 0, h)
D = geompy.MakeVertex(l, 0, 0)
#Mesh1 = geompy.MakeVertex(0, 0, refine)
#Mesh2 = geompy.MakeVertex(l, 0, refine)

AB = geompy.MakeLineTwoPnt(A, B)
BC = geompy.MakeLineTwoPnt(B, C)
CD = geompy.MakeLineTwoPnt(C, D)
AD = geompy.MakeLineTwoPnt(A, D)

#AB1 = geompy.MakeLineTwoPnt(Mesh1, B)
#CD1 = geompy.MakeLineTwoPnt(C, Mesh2)
#Mesh_Line = geompy.MakeLineTwoPnt(Mesh1, Mesh2)
#Side_Refine = geompy.MakeCompound([AB1, CD1])
Side = geompy.MakeCompound([AB, CD])

geompy.addToStudy( O, 'O' )
geompy.addToStudy( OX, 'OX' )
geompy.addToStudy( OY, 'OY' )
geompy.addToStudy( OZ, 'OZ' )
geompy.addToStudy( A, 'A' )
geompy.addToStudy( B, 'B' )
geompy.addToStudy( C, 'C' )
geompy.addToStudy( D, 'D' )
geompy.addToStudy( AB, 'AB' )
geompy.addToStudy( BC, 'BC' )
geompy.addToStudy( CD, 'CD' )
geompy.addToStudy( AD, 'AD' )
#geompy.addToStudy( Mesh1, 'Mesh1' )
#geompy.addToStudy( Mesh2, 'Mesh2' )
#geompy.addToStudy( AB1, 'AB1' )
#geompy.addToStudy( CD1, 'CD1' )
#geompy.addToStudy(Mesh_Line, 'Mesh_Line')
#geompy.addToStudy(Side_Refine, 'Side_Refine')
geompy.addToStudy(Side, 'Side')


#Weld pasess
w1 = (0.5*l)-(0.5*pl) #Weld pass start
w2 = (0.5*l)+(0.5*pl) #Weld pass end

W0L = geompy.MakeVertex(w1, 0, h)
W0R = geompy.MakeVertex(w2, 0, h)
W1L = geompy.MakeVertex(w1, 0, h+ph)
W1R = geompy.MakeVertex(w2, 0, h+ph)
Weld_Base = geompy.MakeLineTwoPnt(W0L, W0R)
WeldL = geompy.MakeLineTwoPnt(W1L, W0L)
WeldR = geompy.MakeLineTwoPnt(W0R, W1R)
Weld_Top = geompy.MakeLineTwoPnt(W1R, W1L)
Weld_Side = geompy.MakeCompound([WeldL, WeldR])
Weld_Across = geompy.MakeCompound([Weld_Base, Weld_Top])
Weld = geompy.MakeFaceWires([Weld_Base, WeldL, WeldR, Weld_Top], 1)
#Surf_L = geompy.MakeLineTwoPnt(B, W0L)
#Surf_R = geompy.MakeLineTwoPnt(W0R, C)
#Edge_Extra = geompy.MakeCompound([Surf_L, Surf_R])
#Refined_Plate = geompy.MakeFaceWires([AB1, Surf_L, Weld_Base, Surf_R, CD1, Mesh_Line], 1)
#Plate = geompy.MakeFaceWires([AB, Mesh_Line, CD, AD], 1)
#Parent = geompy.MakeCompound([Refined_Plate, Plate])
Parent = geompy.MakeFaceWires([AB, BC, CD, AD], 1)
Parent_extrude = geompy.MakePrismVecH2Ways(Parent, OY, (th/2))
Weld_extrude = geompy.MakePrismVecH2Ways(Weld, OY, (th/2))

geompy.addToStudy(W0L,'W0L')
geompy.addToStudy(W0R,'W0R')
geompy.addToStudy(W1L,'W1L')
geompy.addToStudy(W1R,'W1R')
geompy.addToStudy( Weld_Base, 'Weld_Base' )
geompy.addToStudy( WeldL, 'WeldL' )
geompy.addToStudy( WeldR, 'WeldR' )
geompy.addToStudy( Weld_Top, 'Weld_Top' )
geompy.addToStudy( Weld_Side, 'Weld_Side' )
geompy.addToStudy( Weld_Across, 'Weld_Across' )
#geompy.addToStudy( Surf_L, 'Surf_L' )
#geompy.addToStudy( Surf_R, 'Surf_R' )
#geompy.addToStudy( Edge_Extra, 'Edge_Extra')
#geompy.addToStudy( Refined_Plate, 'Refined_Plate' )
#geompy.addToStudy( Plate, 'Plate' )
geompy.addToStudy( Parent, 'Parent' )
geompy.addToStudy( Weld, 'Weld' )
geompy.addToStudy( Parent_extrude, 'Parent_extrude' )
geompy.addToStudy( Weld_extrude, 'Weld_extrude' )


Full = geompy.MakePartition([Parent, Weld], [], [], [], geompy.ShapeType["FACE"], 0, [], 0)
geompy.addToStudy( Full, 'Full' )


#geompy.addToStudyInFather(Full, Plate, 'Plate')
#geompy.addToStudyInFather(Full, Refined_Plate, 'Refined_Plate')
geompy.addToStudyInFather(Full, Weld, 'Weld')
geompy.addToStudyInFather(Full, Parent, 'Parent' )



#Groups for meshing
#Edge_Refine = geompy.GetInPlace(Full, Mesh_Line)
#Edge_Side_Refine = geompy.GetInPlace(Full, Side_Refine)
Edge_Bottom = geompy.GetInPlace(Full, AD)
#Edge_Extra_Top = geompy.GetInPlace(Full, Edge_Extra)
Edge_Side = geompy.GetInPlace(Full, Side)

Edge_Weld_Across = geompy.GetInPlace(Full, Weld_Across)
Edge_Weld_Side = geompy.GetInPlace(Full, Weld_Side)

#geompy.addToStudyInFather( Full, Edge_Refine, 'Edge_Refine')
#geompy.addToStudyInFather( Full, Edge_Side_Refine, 'Edge_Side_Refine')
geompy.addToStudyInFather( Full, Edge_Bottom, 'Edge_Bottom')
#geompy.addToStudyInFather( Full, Edge_Extra_Top, 'Edge_Extra_Top')
geompy.addToStudyInFather( Full, Edge_Side, 'Edge_Side')

geompy.addToStudyInFather( Full, Edge_Weld_Across, 'Edge_Weld_Across')
geompy.addToStudyInFather( Full, Edge_Weld_Side, 'Edge_Weld_Side')

#Groups for Computations(weld, Full, conduction, convection, radiation)
#Geometry for mesh groups
#Base plate base Surface
th1 = th/2
th2 = -th/2
A1 = geompy.MakeVertex(0, th1, 0)
A2 = geompy.MakeVertex(0, th2, 0)
D2 = geompy.MakeVertex(l, th2, 0)
D1 = geompy.MakeVertex(l, th1, 0)
A3D = geompy.MakeLineTwoPnt(A1, A2)
AD3D_1 = geompy.MakeLineTwoPnt(A1, D1)
D3D = geompy.MakeLineTwoPnt(D1, D2)
AD3D_2 = geompy.MakeLineTwoPnt(A2, D2)
Base_Face = geompy.MakeFaceWires([A3D, AD3D_1, D3D, AD3D_2], 1)
geompy.addToStudy( Base_Face, 'Base_Face' )

# Upstream/Downstream
B1 = geompy.MakeVertex(0, th1, h)
B2 = geompy.MakeVertex(0, th2, h)
AB3D_1 = geompy.MakeLineTwoPnt(A1, B1)
B3D = geompy.MakeLineTwoPnt(B1, B2)
AB3D_2 = geompy.MakeLineTwoPnt(A2, B2)
Upstream = geompy.MakeFaceWires([A3D, AB3D_1, B3D, AB3D_2], 1)
Downstream = geompy.MakeTranslationVectorDistance(Upstream, OX, l)
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
Mesh_a = 120 #Number of elements along Weld length
D_d = [ 0, 0.5, 0.3, 1, 0.5, 3, 0.7, 1, 1, 0.5 ] # Density distribution [x1, density1, x2, density2, x3, density3, ...] (x from 0 to 1)
Mesh_b = 6 #Number of elements along weld height

#Base plate
Mesh_c = 40 #Number of elements along base plate length (bottom edge)
Mesh_d = 20 #Number of elements along base plate height

Mesh_a_corrected = round_up_to_even(Mesh_a)
Mesh_c_corrected = round_up_to_even(Mesh_c)



# weld meshing
#########################
Regular_1D = Mesh_Weld.Segment(geom=Edge_Weld_Across)
Number_of_Segments_Weld_Across = Regular_1D.NumberOfSegments(Mesh_a_corrected,None,[])
Number_of_Segments_Weld_Across.SetConversionMode( 1 )
Number_of_Segments_Weld_Across.SetReversedEdges( [] )
#Number_of_Segments_Weld_Across.SetTableFunction( [ 0, 1, 0.4, 2, 0.5, 3, 0.6, 2, 1, 1 ] )
Number_of_Segments_Weld_Across.SetTableFunction( D_d )

Regular_1D_1 = Mesh_Weld.Segment(geom=Edge_Weld_Side)
Number_of_Segments_Weld_Side = Regular_1D_1.NumberOfSegments(Mesh_b,None,[])


#Parent meshing
#########################
#Horizontal edges
Regular_1D_2 = Mesh_Weld.Segment(geom=Edge_Bottom)
Number_of_Segments_Bottom = Regular_1D_2.NumberOfSegments(Mesh_c_corrected,None,[])

Regular_1D_3 = Mesh_Weld.Segment(geom=Edge_Side)
Number_of_Segments_Side = Regular_1D_3.NumberOfSegments(Mesh_d,None,[])



# weld sub-meshing
Sub_mesh = Regular_1D.GetSubMesh()
Sub_mesh_A = Regular_1D_1.GetSubMesh()
Sub_mesh_B = Regular_1D_2.GetSubMesh()
Sub_mesh_C = Regular_1D_3.GetSubMesh()

isDone = Mesh_Weld.Compute()

HalfWidth = int((th/2))
Mesh_Weld.ExtrusionSweepObjects( [ Mesh_Weld ], [ Mesh_Weld ], [ Mesh_Weld ], [ 0, 1, 0 ], HalfWidth, 1, [  ], 0, [  ], [  ], 1 )

Mesh_WeldMirr = Mesh_Weld.MirrorObjectMakeMesh(Mesh_Weld,geompy.MakePlane(O,OY,100.),SMESH.SMESH_MeshEditor.PLANE, 1 ,'Mesh_WeldMirr')

Mesh_Weld_3D = smesh.Concatenate([Mesh_Weld.GetMesh(),Mesh_WeldMirr.GetMesh()], 1, 1, 1e-05, False, name='Mesh_Weld_3D')
isDone = Mesh_Weld_3D.Compute()



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



smesh.SetName(Number_of_Segments_Weld_Across, 'Number of Segments_Weld_Across')
smesh.SetName(Number_of_Segments_Weld_Side, 'Number of Segments_Weld_Side')
smesh.SetName(Number_of_Segments_Bottom, 'Number of Segments_Bottom')
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
