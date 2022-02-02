# USER input position-time pf weld torch

#[t,x,y,z]
import numpy as np



def getBCS(xi,tableData):
    '''
    Takes a table of data, tableData, and returns the interpolated values, yi, for given ordinate values, xi
    '''
    
    rowz,colz = tableData.shape
    rowzi = len(xi)
    tabVars = np.zeros([rowzi,colz])
    for i in range(1,colz):
        yi = np.interp(xi,tableData[:,0],tableData[:,i])
        #print(yi)
        tabVars[:,i] = yi
        
    #yi = np.interp(xi,tableData[:,0],tableData[:,1])
    #return yi
    return tabVars

def getDisplacement(vel_torch,HS0):
	'''
	Takes the velocity BCs and calculates the displacement BCs. Input the [t,V] data and output the [t,X] data. Displacement obtained by integrating velocity using trapezium rule.
	'''
	rowz,colz = vel_torch.shape
	disp_torch = np.zeros((rowz,colz))
	for j in range(1,colz):
		A_total=HS0[j-1]
		disp_torch[0][j] = A_total
		for i in range(1,rowz):
			dt = vel_torch[i][0] - vel_torch[i-1][0]
			dA=0.5*(vel_torch[i][j] + vel_torch[i-1][j])*dt
			A_total+=dA
			disp_torch[i][0] = vel_torch[i][0]
			disp_torch[i][j] = A_total
	return disp_torch


def getDeltaS(path_torch):
	'''
	Calculates the torch curvilinear displacement increments from the input path
	'''
	rowz,colz = path_torch.shape
	dS_torch = np.zeros((rowz,1))
	for i in range(0,rowz):
		if i == 0:
			dS_torch[i] = 0.
		else:
			dS_torch[i] = np.linalg.norm(path_torch[i] - path_torch[i-1])
	return dS_torch
	
def getCumS(dS_torch):
	'''
	Calculates the torch curvilinear displacement from the curvilinear displacement increments 
	'''
	rowz,colz = dS_torch.shape
	S_torch = np.zeros((rowz,colz))
	for i in range(0,rowz):
		if i == 0:
			S_torch[i] = dS_torch[i]
		else:
			S_torch[i] = dS_torch[i] + S_torch[i-1]
	return S_torch

def getMaxdSdt(vel_torch):
	'''
	Calculates maximum velocity of torch
	'''
	rowz,colz = vel_torch.shape
	dsdt = np.zeros((rowz,1))
	for i in range(0,rowz):
		dsdt[i] = np.linalg.norm(vel_torch[i][1:])
	max_dsdt=max(dsdt)
	return max_dsdt[0]

def getS_dsdt(dsdt_torch):
	'''
	Calculates the curvilinear displacement time history
	'''
	rowz,colz = dsdt_torch.shape
	Areas = np.zeros((rowz,colz))
	Area = 0.
	for i in range(1,rowz):
		dArea = 0.5 * (dsdt_torch[i-1][1] + dsdt_torch[i][1]) * (dsdt_torch[i][0] - dsdt_torch[i-1][0])
		Area+=dArea
		Areas[i][1] = Area
		Areas[i][0] = dsdt_torch[i][0]
	
	return Areas

def setTimesPath(S_torch,S_dsdt_torch):
	'''
	Interpolates the time base that satisfies the ds_dt profile and the path profile
	'''
	xp=S_dsdt_torch[:,0]
	yp=S_dsdt_torch[:,1]
	y=S_torch[:,0]
	x=np.interp(y,yp,xp)
	rowz,colz = S_torch.shape
	S_t_torch = np.zeros((rowz,2))
	for i in range(0,rowz):
		S_t_torch[i][0] = x[i] 
		S_t_torch[i][1] = S_torch[i][0]
	return S_t_torch
#############################
# Confirmed Functions
#############################
def getDirection(path_torch,dir_0):
	'''
	Calculates the tangential directions from the input path
	'''
	rowz,colz = path_torch.shape
	direction_torch = np.zeros((rowz,colz))
	for i in range(0,rowz):
		if i == 0:
			direction_torch[i] = dir_0
		else:
			if i == (rowz-1):
				direction_torch[i] = direction_torch[i-1]
			else:
				direction_torch[i] = path_torch[i] - path_torch[i-1]
#		if i == (rowz-1):
#			direction_torch[i] = direction_torch[i-1]
#		else:
#			direction_torch[i] = path_torch[i+1] - path_torch[i]
	return direction_torch


def getNormals(direction_torch,norm_0):
	'''
	Calculates the normal directions from the tangent and norm0.
	Normal to path of weld torch AND normal to Direction of weld torch
	'''
	rowz,colz = direction_torch.shape
	normals_torch = np.zeros((rowz,colz))
	for i in range(0,rowz):
		if i == 0:
			normals_torch[i] = norm_0
		else:
			if i == (rowz - 1):
				normals_torch[i] = normals_torch[i-1]
			else:
				normals_torch[i] = np.cross(direction_torch[i],direction_torch[i-1])
	return normals_torch
	
def getPathNormals(direction_torch,normals_torch):
	'''
	Calculates the normal directions from the tangent and norm0.
	Normal to path of weld torch BUT parallel to Direction of weld torch
	Inverse gradient of directions, i.e. direction m from y = mx +c then normal = 1/m
	'''
	rowz,colz = direction_torch.shape
	pathNormals_torch = np.zeros((rowz,colz))
	for i in range(0,rowz):
		#print(np.array(direction_torch[i]))
		#print(np.array(normals_torch[i]))
		#print(np.cross(np.array(normals_torch[i]),np.array(direction_torch[i])))
		pathNormals_torch[i] = np.cross(direction_torch[i],normals_torch[i])
	return pathNormals_torch
	
def getTangentNormals(direction_torch,pathNormals_torch):
	'''
	Calculates the normal directions from the tangent and norm0.
	Normal to path of weld torch BUT parallel to Direction of weld torch
	Inverse gradient of directions, i.e. direction m from y = mx +c then normal = 1/m
	'''
	rowz,colz = direction_torch.shape
	normals_torch = np.zeros((rowz,colz))
	for i in range(0,rowz):
		#print(np.array(direction_torch[i]))
		#print(np.array(normals_torch[i]))
		#print(np.cross(np.array(normals_torch[i]),np.array(direction_torch[i])))
		normals_torch[i] = np.cross(direction_torch[i],pathNormals_torch[i])
	return normals_torch
#############################
weldLength=100.
v_nom = 1.67 #1.42
t_on=1.
t_dwell=4.
t_rampUp=6.51
t_rampDown=t_rampUp + ((weldLength-(0.5*(t_rampUp - t_dwell)*v_nom))/v_nom)
t_dwell2=t_rampDown+0.01
t_off=t_dwell2+0.01
t_cool=np.round(t_off+1.)

HSX0=0
HSY0=23.5
HSZ0=-50
HS0=[HSX0,HSY0,HSZ0]

# linear velocity of torch (special case)
vel_torch=np.array([[0.,0.,0.,0.],#Start
			[t_on,0.,0.,0.],#beam on
			[t_dwell,0.,0.,0.],#Dwell
			[t_rampUp,0.,0.,v_nom],#Ramp up
			[t_rampDown,0.,0.,v_nom],#Ramp down
			[t_dwell2,0.,0.,0.],#Dwell2
			[t_off,0.,0.,0.],#beam off
			[t_cool,0.,0.,0.],])#cooling phase begins


######################################################
# USER INPUTS
######################################################

# ds/dt of torch
dsdt_torch=np.array([[0.,0.],#Start
			[t_on,0.],#beam on
			[t_dwell,0.],#Dwell
			[t_rampUp,v_nom],#Ramp up
			[t_rampDown,v_nom],#Ramp down
			[t_dwell2,0.],#Dwell2
			[t_off,0.],#beam off
			[t_cool,0.],])#cooling phase begins

# Torch Path
'''
path_torch=np.array([[0.,0.,0.],#Start
			[0.5,0.5,0.],#beam on
			[1.,0.,0.],#Dwell
			[0.5,-1.,0],#Ramp up
			[0.,0.,0],])#cooling phase begins
'''
# Define a circular path on a plate
circSegs=20
path_torch=np.zeros([circSegs,3])
pathNormals_torch=np.zeros([circSegs,3])
circ_rad=weldLength/2./np.pi
for i in range(0,(circSegs)):
	theta = (i/(circSegs))*2*np.pi
	path_torch[i,0] = circ_rad*np.sin(theta) + circ_rad
	path_torch[i,1] = circ_rad*np.cos(theta)
	path_torch[i,2] = 0.
	pathNormals_torch[i,0]=0.
	pathNormals_torch[i,1]=0.
	pathNormals_torch[i,2]=1.

norm_0=np.array([[0.,-10.,0.]])
dir_0=np.array([[1.,0.,0.]])

# Define weld Top directions for a circular path on a plate


######################################################

# Compute direction (tangent) vector from path data

	
direction_torch=getDirection(path_torch,dir_0)

print('path_torch',path_torch)
print('direction_torch',direction_torch)

normals_torch = getTangentNormals(direction_torch,pathNormals_torch)
print('normals_torch',normals_torch)
'''
# Compute nomal vector to the plane of the weld torch path (normal to tangent vector)
normals_torch = getNormals(direction_torch,norm_0)

#print('normals_torch',normals_torch)

# Compute nomal vector from path but parallel to tangent vector 
pathNormals_torch = getPathNormals(direction_torch,normals_torch)
'''
print('pathNormals_torch',pathNormals_torch)

# Compute dS from path data
dS_torch=getDeltaS(path_torch)
print('dS_torch',dS_torch)
s=input('pause me here...')
# Compute S from path data
S_torch=getCumS(dS_torch)
print('S_torch',S_torch)
s=input('pause me here...')
# Compute S from dsdt data
S_dsdt_torch=getS_dsdt(dsdt_torch)
print('S_dsdt_torch',S_dsdt_torch)
print('vel_torch',vel_torch)
s=input('pause me here...')
# Extract times at which path is satisfied by velocity profile
S_t_torch=setTimesPath(S_torch,S_dsdt_torch)
print('S_t_torch',S_t_torch)
s=input('pause me here...')
# Extract out global path/time history_d # <------ USED to set position of torch in global space
rowz,colz = path_torch.shape
path_time_torch = np.zeros((rowz,colz+1))
for i in range(0,rowz):
	for j in range(0,colz+1):
		if j == 0:
			path_time_torch[i][j] = S_t_torch[i][j]
		else:
			path_time_torch[i][j] = path_torch[i][j-1]
print('path_time_torch',path_time_torch)

# Extract out global tangent/time history # <------ USED to set direction of torch in global space
rowz,colz = direction_torch.shape
tangent_time_torch = np.zeros((rowz,colz+1))
for i in range(0,rowz):
	for j in range(0,colz+1):
		if j == 0:
			tangent_time_torch[i][j] = S_t_torch[i][j]
		else:
			tangent_time_torch[i][j] = direction_torch[i][j-1]
print('tangent_time_torch',tangent_time_torch)

# Extract out global normal/time history # <------ USED to set orientation of torch in global space
rowz,colz = normals_torch.shape
normals_time_torch = np.zeros((rowz,colz+1))
for i in range(0,rowz):
	for j in range(0,colz+1):
		if j == 0:
			normals_time_torch[i][j] = S_t_torch[i][j]
		else:
			normals_time_torch[i][j] = normals_torch[i][j-1]
print('normals_time_torch',normals_time_torch)


######
# DATA can be used in a simulation

t=[]
for i in range(0,10):
	t.append(i)
	
print('time steps: ',t)
print('Path_tim:\n',getBCS(t,path_time_torch))
print('Tangent_time:\n',getBCS(t,tangent_time_torch))
print('Normal_time:\n',getBCS(t,normals_time_torch))


print('Interpolating outside of time base, S_t_torch:')
print(S_t_torch)
print('t=',t)
print(getBCS(t,S_t_torch))
'''
# Loop through instances
# At each instance, obtain the current position as well as the tangent and normal directions 
convert [HSX,HSY,HSZ] => [HStau, HSn, HStauxn] # <-heat source position in weld torch coordinates
U = [[1, 0, 0],[0, 1, 0],[0, 0, 1]]
V => Interpolated at the current instance e.g. [[0.1,0.5,0.9],[1.1,0.3,-0.4],[0.1,0.3,0.3]]
[HSX,HSY,HSZ] .U.V' = [HStau, HSn, HStauxn]
# ---> Transform the coordinates of each node in the mesh p(x,y,z) into p(tau,n,tau x n)
p(x,y,z) . U.V' => p(tau,n,tauxn)
# ---> Check the position along the s (forward/behind)
if p(tau) - HStau >= 0:
	Qff
else:
	Qfr
# ---> Compute q from this information
'''
