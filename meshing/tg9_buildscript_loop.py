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
#Base plate (parent)
l = 125 #Base plate length
h = 50 #Base plate height
th = 6 #Base plate thickness -------------------> Only works with even integer
refine = 0.8*h #Amount of plateheight that is not refined

#Weld pasess
p = 5 #Number of passes, p
pl = 100 #Weld pass length
ph = 4 #Weld pass height
pth = 6 #Weld pass thickness -------------------> Only works with even integer

geompy = geomBuilder.New()

O = geompy.MakeVertex(0, 0, 0)
OX = geompy.MakeVectorDXDYDZ(1, 0, 0)
OY = geompy.MakeVectorDXDYDZ(0, 1, 0)
OZ = geompy.MakeVectorDXDYDZ(0, 0, 1)


#Base plate (parent)
A = geompy.MakeVertex(0, 0, 0)
B = geompy.MakeVertex(0, 0, h)
C = geompy.MakeVertex(l, 0, h)
D = geompy.MakeVertex(l, 0, 0)
Mesh1 = geompy.MakeVertex(0, 0, refine)
Mesh2 = geompy.MakeVertex(l, 0, refine)

AB = geompy.MakeLineTwoPnt(A, Mesh1)
BC = geompy.MakeLineTwoPnt(B, C)
CD = geompy.MakeLineTwoPnt(Mesh2, D)
AD = geompy.MakeLineTwoPnt(A, D)

AB1 = geompy.MakeLineTwoPnt(Mesh1, B)
CD1 = geompy.MakeLineTwoPnt(C, Mesh2)
Mesh_Line = geompy.MakeLineTwoPnt(Mesh1, Mesh2)
Side_Refine = geompy.MakeCompound([AB1, CD1])
Side = geompy.MakeCompound([AB, CD])
Parent_ = geompy.MakeFaceWires([AB, AB1, BC, CD1, CD, AD], 1)
Parent_extrude = geompy.MakePrismVecH2Ways(Parent_, OY, (th/2))


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
geompy.addToStudy( Mesh1, 'Mesh1' )
geompy.addToStudy( Mesh2, 'Mesh2' )
geompy.addToStudy( AB1, 'AB1' )
geompy.addToStudy( CD1, 'CD1' )
geompy.addToStudy(Mesh_Line, 'Mesh_Line')
geompy.addToStudy(Side_Refine, 'Side_Refine')
geompy.addToStudy(Side, 'Side')
geompy.addToStudy( Parent_, 'Parent_' )
geompy.addToStudy( Parent_extrude, 'Parent_extrude' )

#Weld pasess
w1 = (0.5*l)-(0.5*pl) #Weld pass start
w2 = (0.5*l)+(0.5*pl) #Weld pass end

p_line=[]
p_line_l=[]
p_line_r=[]
p_face=[]
p_extrude=[]

W0L = geompy.MakeVertex(w1, 0, h)
W0R = geompy.MakeVertex(w2, 0, h)
geompy.addToStudy(W0L,'W0L')
geompy.addToStudy(W0R,'W0R')
passl = [W0L]
passr = [W0R]

Weld_Base = geompy.MakeLineTwoPnt(passl[0], passr[0])
geompy.addToStudy(Weld_Base, 'Weld_Base' )
p_line = [Weld_Base]
geompy.addToStudy(p_line[0], 'Pass_Bottom' )
for i in range(p):
	wh = ph*(i+1)
	passl.append(geompy.MakeVertex(w1, 0, h+wh))
	#exec('passl'+str(i) = geompy.MakeVertex(w1, 0, h+wh))
	passr.append(geompy.MakeVertex(w2, 0, h+wh))
	geompy.addToStudy(passl[i+1], 'W'+str(i+1)+'L')
	geompy.addToStudy(passr[i+1], 'W'+str(i+1)+'R')

	p_line_l.append(geompy.MakeLineTwoPnt(passl[i], passl[i+1]))
	p_line_r.append(geompy.MakeLineTwoPnt(passr[i], passr[i+1]))
	p_line.append(geompy.MakeLineTwoPnt(passl[i+1], passr[i+1]))
	geompy.addToStudy(p_line_l[i], 'Pass'+str(i+1)+'_L')
	geompy.addToStudy(p_line_r[i], 'Pass'+str(i+1)+'_R')
	#Weld_Side = geompy.MakeCompound([p_line_l[i], p_line_r[i]])
	geompy.addToStudy(p_line[i+1], 'Pass'+str(i+1)+'_Top')

	p_face.append(geompy.MakeFaceWires([p_line[i], p_line_l[i], p_line_r[i], p_line[i+1]], 1))
	geompy.addToStudy(p_face[i], 'Pass'+str(i+1))

	weld_left = geompy.MakeLineTwoPnt(passl[0], passl[i+1])
	weld_right = geompy.MakeLineTwoPnt(passr[0], passr[i+1])
	weld_full = geompy.MakeFaceWires([p_line[0], weld_left, p_line[i+1], weld_right], 1)
	p_extrude.append(geompy.MakePrismVecH2Ways(weld_full, OY, (pth/2)))
	geompy.addToStudy(p_extrude[i], 'Pass'+str(i+1)+'_extrude')

Weld_Top = geompy.MakeLineTwoPnt(passl[p], passr[p])
Weld_Across = geompy.MakeCompound(p_line)
geompy.addToStudy(Weld_Top, 'Weld_Top' )
geompy.addToStudy(Weld_Across, 'Weld_Across' )

Weld_L = geompy.MakeLineTwoPnt(passl[0], passl[p])
Weld_R = geompy.MakeLineTwoPnt(passr[0], passr[p])
#Weld_L = geompy.MakeCompound([p_line_l[:]])
#Weld_R = geompy.MakeCompound([p_line_r[:]])
Weld_Side = geompy.MakeCompound([Weld_L, Weld_R])
#Weld_Side = geompy.MakeCompound([p_line_l[0], p_line_r[0]])

geompy.addToStudy( Weld_L, 'Weld_L' )
geompy.addToStudy( Weld_R, 'Weld_R' )
geompy.addToStudy(Weld_Side, 'Weld_Side')

Surf_L = geompy.MakeLineTwoPnt(B, passl[0])
Surf_R = geompy.MakeLineTwoPnt(passr[0], C)
Edge_Extra = geompy.MakeCompound([Surf_L, Surf_R])
geompy.addToStudy( Surf_L, 'Surf_L' )
geompy.addToStudy( Surf_R, 'Surf_R' )
geompy.addToStudy(Edge_Extra, 'Edge_Extra')

'''
#Base Surface
pth1 = pth/2
pth2 = -pth/2
wa = geompy.MakeVertex(w1, pth1, h)
wb = geompy.MakeVertex(w1, pth2, h)
wc = geompy.MakeVertex(w2, pth2, h)
wd = geompy.MakeVertex(w2, pth1, h)
wab = geompy.MakeLineTwoPnt(wa, wb)
wbc = geompy.MakeLineTwoPnt(wb, wc)
wcd = geompy.MakeLineTwoPnt(wc, wd)
wad = geompy.MakeLineTwoPnt(wa, wd)
Weld_Base_Face = geompy.MakeFaceWires
'''

Refined_Plate = geompy.MakeFaceWires([AB1, Surf_L, Weld_Base, Surf_R, CD1, Mesh_Line], 1)
Plate = geompy.MakeFaceWires([AB, Mesh_Line, CD, AD], 1)
Parent_Area = geompy.MakeCompound([Refined_Plate, Plate])
geompy.addToStudy( Refined_Plate, 'Refined_Plate' )
geompy.addToStudy( Plate, 'Plate' )
geompy.addToStudy( Parent_Area, 'Parent_Area' )
#Face_ = geompy.MakeFaceWires([AB, AB1, Surf_L, Weld_L, Weld_Top, Weld_R, Surf_R, CD1, CD, AD], 1)
#geompy.addToStudy(Parent_, 'Parent_Area')
PartitionObjects = [Parent_Area]
#PartitionObjects = [Base_Plate]
Parent = geompy.MakePartition([Parent_], PartitionObjects, [], [], geompy.ShapeType["FACE"], 0, [], 0)
geompy.addToStudy( Parent, 'Parent' )
PartitionObjects = geompy.ExtractShapes(Parent, geompy.ShapeType["FACE"], True)
geompy.addToStudyInFather(Parent, PartitionObjects[0], 'Parent_1')
geompy.addToStudyInFather(Parent, PartitionObjects[1], 'Parent_2')


Weld_Area = geompy.MakeFaceWires([Weld_L, Weld_Top, Weld_R, Weld_Base], 1)
geompy.addToStudy(Weld_Area, 'Weld_Area')
PartitionObjects_1 = []
for i in range(p):
	PartitionObjects_1.append(p_face[i])
Weld = geompy.MakePartition([Weld_Area], PartitionObjects_1, [], [], geompy.ShapeType["FACE"], 0, [], 0)
geompy.addToStudy( Weld, 'Weld' )
PartitionObjects_1 = geompy.ExtractShapes(Weld, geompy.ShapeType["FACE"], True)
for i in range(p):
	geompy.addToStudyInFather(Weld, PartitionObjects_1[i], 'Pass_'+str(i+1))


#Groups for meshing
Edge_Refine = geompy.GetInPlace(Parent, Mesh_Line)
Edge_Side_Refine = geompy.GetInPlace(Parent, Side_Refine)
Edge_Bottom = geompy.GetInPlace(Parent, AD)
Edge_Extra_Top = geompy.GetInPlace(Parent, Edge_Extra)
Edge_Side = geompy.GetInPlace(Parent, Side)
#Edge_Weld_Top = geompy.GetInPlace(Full, Weld_Top)
Edge_Top = geompy.GetInPlace(Parent, Weld_Base)

Edge_Weld_Across = geompy.GetInPlace(Weld, Weld_Across)
Edge_Weld_Side = geompy.GetInPlace(Weld, Weld_Side)


geompy.addToStudyInFather( Parent, Edge_Refine, 'Edge_Refine')
geompy.addToStudyInFather( Parent, Edge_Side_Refine, 'Edge_Side_Refine')
geompy.addToStudyInFather( Parent, Edge_Bottom, 'Edge_Bottom')
geompy.addToStudyInFather( Parent, Edge_Extra_Top, 'Edge_Extra_Top')
geompy.addToStudyInFather( Parent, Edge_Side, 'Edge_Side')
#geompy.addToStudyInFather( Full, Edge_Weld_Top, 'Edge_Weld_Top')
geompy.addToStudyInFather( Parent, Edge_Top, 'Edge_Top')

geompy.addToStudyInFather( Weld, Edge_Weld_Across, 'Edge_Weld_Across')
geompy.addToStudyInFather( Weld, Edge_Weld_Side, 'Edge_Weld_Side')


#Groups for Computations(weld, parent, conduction, convection, radiation)






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



# weld meshing parameters

Mesh_parent = smesh.Mesh(Parent)
Quadrangle_2D = Mesh_parent.Quadrangle(algo=smeshBuilder.QUADRANGLE)
Quadrangle_Parameters_parent = Quadrangle_2D.QuadrangleParameters(StdMeshersBuilder.QUAD_REDUCED,0,[],[])

Mesh_fullpass = smesh.Mesh(Weld)
Quadrangle_2D_1 = Mesh_fullpass.Quadrangle(algo=smeshBuilder.QUADRANGLE)
Quadrangle_Parameters_WELD = Quadrangle_2D_1.QuadrangleParameters(StdMeshersBuilder.QUAD_REDUCED,0,[],[])

a = pl
b = ph*p
c = l
d = int((c-a)/2)
e = int(c/6)
f = int(0.2*h)
g = int((0.8*h)/4)



### Meshing Parameters

#Weld zone segments
Regular_1D = Mesh_fullpass.Segment(geom=Edge_Weld_Across)
Number_of_Segments_Weld_Across = Regular_1D.NumberOfSegments(100,None,[])

Regular_1D_1 = Mesh_fullpass.Segment(geom=Edge_Weld_Side)
Number_of_Segments_Weld_Edge = Regular_1D_1.NumberOfSegments(4,None,[])


#Parent segments
#Horizontal edges
Regular_1D_2 = Mesh_parent.Segment(geom=Edge_Refine)
Number_of_Segments_Fine = Regular_1D_2.NumberOfSegments(120,None,[])

Regular_1D_3 = Mesh_parent.Segment(geom=Edge_Top)
Number_of_Segments_Top = Regular_1D_3.NumberOfSegments(100,None,[])

Regular_1D_4 = Mesh_parent.Segment(geom=Edge_Extra_Top)
Number_of_Segments_Extra_Top = Regular_1D_4.NumberOfSegments(10,None,[])

Regular_1D_5 = Mesh_parent.Segment(geom=Edge_Bottom)
Number_of_Segments_Bottom = Regular_1D_5.NumberOfSegments(20,None,[])

#Vertical Edges
Regular_1D_6 = Mesh_parent.Segment(geom=Edge_Side_Refine)
Number_of_Segments_Fine_Side = Regular_1D_6.NumberOfSegments(10,None,[])

Regular_1D_7 = Mesh_parent.Segment(geom=Edge_Side)
Number_of_Segments_Side = Regular_1D_7.NumberOfSegments(10,None,[])

# weld sub-meshing
Sub_mesh_A = Regular_1D.GetSubMesh()
Sub_mesh_B = Regular_1D_1.GetSubMesh()
Sub_mesh_C = Regular_1D_2.GetSubMesh()
Sub_mesh_D = Regular_1D_3.GetSubMesh()
Sub_mesh_E = Regular_1D_4.GetSubMesh()
Sub_mesh_F = Regular_1D_5.GetSubMesh()
Sub_mesh_G = Regular_1D_6.GetSubMesh()
Sub_mesh_H = Regular_1D_7.GetSubMesh()

isDone = Mesh_fullpass.Compute()
isDone = Mesh_parent.Compute()


HalfWidth = int((th/2))
### Extruding and mirroring parent mesh
Mesh_parent.ExtrusionSweepObjects( [ Mesh_parent ], [ Mesh_parent ], [ Mesh_parent ], [ 0, 1, 0 ], HalfWidth, 1, [  ], 0, [  ], [  ], 1 )
Mesh_parentMirr = Mesh_parent.MirrorObjectMakeMesh(Mesh_parent,geompy.MakePlane(O,OY,100.),SMESH.SMESH_MeshEditor.PLANE, 1 ,'Mesh_parentMirr')
Mesh_parent_3D = smesh.Concatenate([Mesh_parent.GetMesh(),Mesh_parentMirr.GetMesh()], 1, 1, 1e-05, False, name='Parent')



### Extracting pass meshes
Mesh_fullpass = Mesh_fullpass.TranslateObjectMakeMesh( Mesh_fullpass, [ 0, 0, 0 ], 1, 'Mesh_'+str(p)+'pass' )
Mesh_Pass = [Mesh_fullpass]
for i in range(p-1):
	theMesh = Mesh_Pass[i]
	theFace = p_face[(p-1)-i]
	Mesh_Pass.append(theMesh.TranslateObjectMakeMesh( theMesh, [ 0, 0, 0 ], 1, 'Mesh_'+str((p-1)-i)+'pass' ))
	aCriteria = []
	aCriterion = smesh.GetCriterion(SMESH.ALL,SMESH.FT_BelongToGeom,SMESH.FT_Undefined,theFace)
	aCriteria.append(aCriterion)
	theMesh=Mesh_Pass[i+1]
	removeEls = theMesh.MakeGroupByCriteria( "remove Pass", aCriteria ).GetIDs()
	isDone = theMesh.RemoveElements( removeEls )
	nbRemoved = theMesh.RemoveOrphanNodes()

### Extruding and mirroring pass meshes
Mesh_Mirr = []
Meshpass3D = []
Pass_HalfWidth = int((pth/2))
for i in range(p):
	theMesh = Mesh_Pass[i]
	theMesh.ExtrusionSweepObjects( [ theMesh ], [ theMesh ], [ theMesh ], [ 0, 1, 0 ], Pass_HalfWidth, 1, [  ], 0, [  ], [  ], 1 )
	Mesh_Mirr.append(theMesh.MirrorObjectMakeMesh(theMesh,geompy.MakePlane(O,OY,100.),SMESH.SMESH_MeshEditor.PLANE, 1 ,'Mesh_'+str(p-i)+'pass_Mirr'))
	theMesh_Mirr = Mesh_Mirr[i]
	Meshpass3D.append(smesh.Concatenate([theMesh.GetMesh(),theMesh_Mirr.GetMesh()], 1, 1, 1e-05, False, name='Pass_'+str(p-i)))



### Groups
# Parent
aCriteria = []
aCriterion = smesh.GetCriterion(SMESH.VOLUME,SMESH.FT_BelongToGeom,SMESH.FT_Undefined,Parent_extrude,SMESH.FT_Undefined,1e-7)
aCriteria.append(aCriterion)
aFilter = smesh.GetFilterFromCriteria(aCriteria)
aFilter.SetMesh(Mesh_parent_3D.GetMesh())
Group_parent = Mesh_parent_3D.GroupOnFilter( SMESH.VOLUME, 'Group_parent', aFilter )
#for i in range(p):
	#theMesh = Mesh3D[i]
	#aFilter.SetMesh(theMesh.GetMesh())
	#Group_parent = theMesh.GroupOnFilter( SMESH.VOLUME, 'Group_parent', aFilter )

for i in range(p):
	theMesh = Meshpass3D[i]
	thePass = p_extrude[p-(i+1)]
	aCriteria = []
	aCriterion = smesh.GetCriterion(SMESH.VOLUME,SMESH.FT_BelongToGeom,SMESH.FT_Undefined,thePass,SMESH.FT_Undefined,1e-7)
	aCriteria.append(aCriterion)
	aFilter = smesh.GetFilterFromCriteria(aCriteria)
	aFilter.SetMesh(theMesh.GetMesh())
	Group_weld = theMesh.GroupOnFilter( SMESH.VOLUME, 'Group_weld', aFilter )



### Concatenating meshes
Mesh3D = []
for i in range(p):
	theMesh = Meshpass3D[i]
	Mesh3D.append(smesh.Concatenate([theMesh.GetMesh(),Mesh_parent_3D.GetMesh()], 1, 1, 1e-05, False, name='Mesh_Pass_'+str(p-i)))

smesh.SetName(Number_of_Segments_Weld_Across, 'Number of Segments Weld Across')
smesh.SetName(Number_of_Segments_Top, 'Number of Segments Top')
#smesh.SetName(Number_of_Segments_Weld_Base, 'Number of Segments Weld Base')
smesh.SetName(Number_of_Segments_Weld_Edge, 'Number of Segments Weld Edge')
smesh.SetName(Number_of_Segments_Fine, 'Number of Segments Fine')
smesh.SetName(Number_of_Segments_Extra_Top, 'Number of Segments Extra Top')
smesh.SetName(Number_of_Segments_Bottom, 'Number of Segments Bottom')
smesh.SetName(Number_of_Segments_Fine_Side, 'Number of Segments Fine Side')
smesh.SetName(Number_of_Segments_Side, 'Number of Segments Side')

smesh.SetName(Sub_mesh_A, 'Sub-mesh_A')
smesh.SetName(Sub_mesh_B, 'Sub-mesh_B')
smesh.SetName(Sub_mesh_C, 'Sub-mesh_C')
smesh.SetName(Sub_mesh_D, 'Sub-mesh_D')
smesh.SetName(Sub_mesh_E, 'Sub-mesh_E')
smesh.SetName(Sub_mesh_F, 'Sub-mesh_F')
smesh.SetName(Sub_mesh_G, 'Sub-mesh_G')
smesh.SetName(Sub_mesh_H, 'Sub-mesh_H')

smesh.SetName(Quadrangle_Parameters_parent, 'Quadrangle Parameters_parent')
smesh.SetName(Quadrangle_Parameters_WELD, 'Quadrangle Parameters_WELD')
smesh.SetName(Mesh_parent.GetMesh(), 'Mesh_parent')
smesh.SetName(Mesh_fullpass.GetMesh(), 'Mesh_fullpass')

if salome.sg.hasDesktop():
  salome.sg.updateObjBrowser()
