###################################
# Author: Jefri Draup
# Email: jefri.draup@edfenergy.com
###################################
import matplotlib.pyplot as plt
import math
import numpy as np
import SSPT
import os
import sys
# print("sys args are:",sys.argv)
# print(sys.argv[2])
# print(type(sys.argv[2]))
# s=input('--->')
# D = os.getenv("USER_INP_GS")
# print(D)
# #CR = os.getenv('USER_INP_coolingPlates').split(' ')
# #os.getenv('mdcList').split(',')
#print("print from python",print("sys args are:",sys.argv," with type",type(CR),type(CR[0]),type(CR[1])))
print('============== PROGRAM STARTED ==============')

print('=== Generating new CCT ===')
	
print('=== Obtaining material properties ===')

##########################################################################
# DO NOT ALTER! - basicBatch.sh modifies these parameters automatically
##########################################################################
#Transformation start/end limits
trans_start = 0.01
trans_fin = 0.99
#<<<<<<< HEAD
print(os.getenv('USER_INP_GS'))
D = float(os.getenv('USER_INP_GS'))
#=======
#D = os.getenv(USER_INP_GS)
#>>>>>>> e55cf88b2cf7ba4243818ce5abb8911293e1ad0c
G = SSPT.ASTM_Grain(D)  #G=8.3#<-------------- USED in Li et al. and Hamelin et al.
grainGrowthMethod = os.getenv('USER_INP_grainGrowthMethod')
material = os.getenv('USER_INP_material')

if material == 'USER':
	inputComp = sys.argv[2].strip('()[]')
	inputComp = inputComp.split(',')
	inputComposition=[float(i) for i in inputComp]
	#s=input('--> ')
else:
	inputComposition = "0"
ae13Choice = os.getenv('USER_INP_ae13CHOICE')
# D=17.9 #15.;#micron grain size used by Yongle in Jomimy benchmark
# G = SSPT.ASTM_Grain(D)  #G=8.3#<-------------- USED in Li et al. and Hamelin et al.
# grainGrowthMethod='CONSTANT'
# material='SA508'
# ae13Choice='Grange'
##########################################################################


	

##########################################################################
# DO NOT ALTER - Autocomputation of key temperatures
##########################################################################
composition = SSPT.setComposition(material,inputComposition)
#s=input('--> ')
print(type(composition))
print(composition)
#s=input('--> ')
AE1,AE3 = SSPT.Ae13Temperature(composition,ae13Choice)
Ms = SSPT.calcMs(composition)
Bs = SSPT.calcBs(composition)

########### Set the cooling curve start/end temperature & fixed cooling rates

T_aust = float(os.getenv('USER_INP_T_aust')) #Celsius
T_end = float(os.getenv('USER_INP_T_end')) #Celsius
#T_aust = 1000. #Celsius
#T_end = 20. #Celsius
CR=[]
itemstoclean=sys.argv[1].strip('()[]')
columns = itemstoclean.split(',')
print(type(columns))
for i in range(0,len(columns)):
	print(type(columns[i]))
	CR.append(float(columns[i]))
	
#s = input('--> ')  


#CR = [0.01, 0.1,  1.,10.,  50.,100., 200., 300., 400., ] #BENCHMARK THIEN
#CR = [0.05, 0.1,  0.15,0.2,  0.3,0.5,1.,1.5,2.,3.,4.,5.,6.,7.,8.,9.,10.,12.,15.,18.,20.,25.,30.,40.,50.,60.,80.,100.,400., ] #BENCHMARK EDF
logCR = []
for i in CR:
	logCR.append(math.log(i,10))

print('=== Calculating initiation times for the formation of each phase for every cooling rate ===')
########### Calculate start times for each phase for each cooling rate requested
CCT_t_B=[]
CCT_T_B=[]
CCT_t_F=[]
CCT_T_F=[]
CCT_t_P=[]
CCT_T_P=[]
CCT_t_M=[]
CCT_T_M=[]


# Calculate CCT Ferrite Start	
for i in range(0,len(logCR)):
	coolingRate = 10.**logCR[i]
	
	#Initialise calculation parameters
	D_vary = D # takes in micron
	int_time = 0. # s
	dt = 1./coolingRate
	sum_dt_dtau = 0.
	X_nuc = 0.01
	sumVar=0.
	print (type(D_vary))
	print (type(dt))
	print (type(grainGrowthMethod))
	print (type(AE3))
	
	while sum_dt_dtau < 1.:
		T_eq = SSPT.eqIsodT(int_time,dt,coolingRate,T_aust) # C
		print (type(T_eq))
		D_vary+= SSPT.calc_dD(D_vary,T_eq,dt,grainGrowthMethod,AE3)
		print (type(D_vary))
		print (D_vary)
		#D_vary,sumVar = SSPT.calc_D_Ikawa(D,dt,T_eq,sumVar)
		G_vary = SSPT.ASTM_Grain(D_vary)
		if T_eq <=Ms:#Bs:
			break
		if T_eq <= AE3:
			tauF_Tnow = SSPT.calcTauF(X_nuc,T_eq,AE3,G_vary,composition)
		else:
			tauF_Tnow = 10.**6.
		dt_tauF_Tnow = dt/tauF_Tnow
		sum_dt_dtau+=dt_tauF_Tnow
		int_time+= dt
	
	#Create 
	time_end = (T_aust - T_end)/coolingRate
	steps = math.ceil(time_end/dt)
	
	#Check solution
	if sum_dt_dtau < 1.:
		CCT_t_F.append(time_end)
		CCT_T_F.append(T_end)
	else:
		CCT_t_F.append(int_time)
		CCT_T_F.append(T_eq)

# Calculate CCT Pearlite Start	
for i in range(0,len(logCR)):
	coolingRate = 10.**logCR[i]
	
	#Initialise calculation parameters
	D_vary = D
	int_time = 0. # s
	dt = 1./coolingRate
	sum_dt_dtau = 0.
	X_nuc = 0.01
	sumVar=0.
	while sum_dt_dtau < 1.:
		T_eq = SSPT.eqIsodT(int_time,dt,coolingRate,T_aust) # C
		D_vary+= SSPT.calc_dD(D_vary,T_eq,dt,grainGrowthMethod,AE3)
		#D_vary,sumVar = SSPT.calc_D_Ikawa(D,dt,T_eq,sumVar)
		G_vary = SSPT.ASTM_Grain(D_vary)
		if T_eq <=Ms:#Bs:
			break
		if T_eq <= AE1:
			tauP_Tnow = SSPT.calcTauP(X_nuc,T_eq,AE1,G_vary,composition)
		else:
			tauP_Tnow = 10.**6.
		dt_tauP_Tnow = dt/tauP_Tnow
		sum_dt_dtau+=dt_tauP_Tnow
		int_time+= dt
	
	#Create 
	time_end = (T_aust - T_end)/coolingRate
	steps = math.ceil(time_end/dt)
	
	#Check solution
	if sum_dt_dtau < 1.:
		CCT_t_P.append(time_end)
		CCT_T_P.append(T_end)
	else:
		CCT_t_P.append(int_time)
		CCT_T_P.append(T_eq)


# Calculate CCT Bainite Start	
for i in range(0,len(logCR)):
	coolingRate = 10.**logCR[i]
	
	#Initialise calculation parameters
	D_vary = D
	int_time = 0. # s
	dt = 1./coolingRate
	sum_dt_dtau = 0.
	X_nuc = 0.01
	sumVar=0.
	while sum_dt_dtau < 1.:
		T_eq = SSPT.eqIsodT(int_time,dt,coolingRate,T_aust) # C
		D_vary+= SSPT.calc_dD(D_vary,T_eq,dt,grainGrowthMethod,AE3)
		#D_vary,sumVar = SSPT.calc_D_Ikawa(D,dt,T_eq,sumVar)
		G_vary = SSPT.ASTM_Grain(D_vary)
		if T_eq <=Ms:
			break
		if T_eq <= Bs:
			tauB_Tnow = SSPT.calcTauB(X_nuc,T_eq,G_vary,composition)
		else:
			tauB_Tnow = 10.**6.
		dt_tauB_Tnow = dt/tauB_Tnow
		sum_dt_dtau+=dt_tauB_Tnow
		int_time+= dt
	
	#Create 
	time_end = (T_aust - T_end)/coolingRate
	steps = math.ceil(time_end/dt)
	
	#Check solution
	if sum_dt_dtau < 1.:
		CCT_t_B.append(time_end)
		CCT_T_B.append(T_end)
	else:
		CCT_t_B.append(int_time)
		CCT_T_B.append(T_eq)
		
# Calculate CCT Martensite Start	
for i in range(0,len(logCR)):
	coolingRate = 10.**logCR[i]
	
	#Initialise calculation parameters
	int_time = 0. # s
	dt = 1./coolingRate
	time_end = (T_aust - T_end)/coolingRate
	steps = math.ceil(time_end/dt)
	
	if coolingRate < 15.:#<---------------Cooling rates less than 15C/s WE could delete this?
		CCT_t_M.append(time_end)
		CCT_T_M.append(T_eq)
	else:
		while int_time < time_end:
			T_eq = SSPT.eqIsodT(int_time,dt,coolingRate,T_aust) # C
			int_time+= dt
			if T_eq <= Ms:
				break
		if int_time > time_end:
			CCT_t_M.append(time_end)
			CCT_T_M.append(T_end)
		else:
			CCT_t_M.append(int_time)
			CCT_T_M.append(T_eq)
	

print('Ferrite start time ',CCT_t_F)
print('Pearlite start time ',CCT_t_P)
print('Bainte start time ',CCT_t_B)
print('Martensite start time ',CCT_t_M)

print('=== Calculating phase formation histories for each phase ===')
########### Go through Each cooling curve and calculate X(T) and T(t)

g = open('CCT.66','w')
g.close()
g = open('Phase_hist.txt','w')
g.close()
f = open('CCT.66','a')
g = open('Phase_hist.txt','a')
line = 'TRC_HAM=DEFI_TRC(HIST_EXP=(\n'
f.write(line)

for i in range(0,len(logCR)):
	#Initialise Calculation
	D_vary = D
	coolingRate = 10.**logCR[i]
	int_time = 0. # s
	dt = 1./coolingRate
	time_end = (T_aust - T_end)/coolingRate
	steps = math.ceil(time_end/dt)
	
	t_hist=[]
	T_hist=[]
	X_Ferrite=[]
	X_Pearlite=[]
	X_Bainite=[]
	X_Martensite=[]
	X_Austenite=[]
	aust=[D_vary]
	
	sum_dt_dtauF = 0.
	sum_dt_dtauP = 0.
	sum_dt_dtauB = 0.
	sum_dX_Mart = 0.
	sumVar=0.
	## Capture Phase formation
	while int_time < time_end:
		t_hist.append(int_time)
		T_eq = SSPT.eqIsodT(int_time,dt,coolingRate,T_aust)
		D_vary+= SSPT.calc_dD(D_vary,T_eq,dt,grainGrowthMethod,AE3)
		#D_vary,sumVar = SSPT.calc_D_Ikawa(D,dt,T_eq,sumVar)
		aust.append(D_vary)
		G_vary = SSPT.ASTM_Grain(D_vary)
		print("ASTM_G = ",G_vary)
		T_hist.append(T_eq)
		
		#Ferritic Phase capture
		if int_time >= CCT_t_F[i]:
			tauF_Tnow = SSPT.calcTauF(1.0,T_eq,AE3,G_vary,composition) - SSPT.calcTauF(0.01,T_eq,AE3,G_vary,composition)
			dt_tauF_Tnow = dt/tauF_Tnow
			sum_dt_dtauF+=dt_tauF_Tnow
			if sum_dt_dtauF >=1.:
				X_Ferrite.append(1.)
			else:
				X_Ferrite.append(sum_dt_dtauF)
		else:
			X_Ferrite.append(0.)
			
		#Check on phase distributions after ferritic calculation	
		if X_Ferrite[-1] >= 1.:
			X_Ferrite[-1] = 1.
			X_Pearlite[-1] = 0.
			X_Bainite[-1] = 0.
			X_Martensite[-1] = 0.
			break	
			
		#Pearlitic Phase capture
		if int_time >= CCT_t_P[i]:
			tauP_Tnow = SSPT.calcTauP(1.0,T_eq,AE1,G_vary,composition) - SSPT.calcTauP(0.01,T_eq,AE1,G_vary,composition)
			dt_tauP_Tnow = dt/tauP_Tnow
			sum_dt_dtauP+=dt_tauP_Tnow
			if sum_dt_dtauP >=1.:
				X_Pearlite.append(1.)
			else:
				X_Pearlite.append(sum_dt_dtauP)
		else:
			X_Pearlite.append(0.)

		#Check on phase distributions after ferritic and pearlitic calculation
		if X_Ferrite[-1] + X_Pearlite[-1] >= 1.:
			X_Ferrite[-1] = X_Ferrite[-1]
			X_Pearlite[-1] = 1.-X_Ferrite[-1]
			X_Bainite[-1] = 0.
			X_Martensite[-1] =0.
			break	
		
		#Bainitic Phase capture
		if int_time >= CCT_t_B[i]:
			tauB_Tnow = SSPT.calcTauB(1.,T_eq,G_vary,composition) - SSPT.calcTauB(0.01,T_eq,G_vary,composition)
			dt_tauB_Tnow = dt/tauB_Tnow
			sum_dt_dtauB+=dt_tauB_Tnow
			if sum_dt_dtauB >=1.:
				X_Bainite.append(1.)
			else:
				X_Bainite.append(sum_dt_dtauB)
		else:
			X_Bainite.append(0.)
		
		#Check on phase distributions after ferritic and pearlitic and bainitic calculation
		if X_Ferrite[-1] + X_Pearlite[-1] + X_Bainite[-1] > 1.:
			X_Ferrite[-1] = X_Ferrite[-1]
			X_Pearlite[-1] = X_Pearlite[-1]
			X_Bainite[-1] = 1.-X_Ferrite[-1]-X_Pearlite[-1]
			X_Martensite[-1] = 0.
			break		
		
		#Martensitic Phase capture - NOTE COMMENTED LINES HERE ARE BASED SOLELY ON X_M inferred from T or calculated assuming dXdt but both give same result
		if int_time >= CCT_t_M[i]:
			
			X_M = SSPT.calcdX_M(T_eq,Ms)
			#dX_M = SSPT.calcdX_M_dt(T_eq,Ms,coolingRate,dt)
			#sum_dX_Mart+= dX_M
			
			#if sum_dX_Mart >=1.:
			if X_M >=1.:
				X_Martensite.append(1.)
			else:
				X_Martensite.append(X_M)
				#X_Martensite.append(sum_dX_Mart)
		else:
			X_Martensite.append(0.)
		
		#Check on phase distributions after ferritic and pearlitic and bainitic calculation
		if X_Ferrite[-1] + X_Pearlite[-1] + X_Bainite[-1] + X_Martensite[-1] > 1.:
			X_Ferrite[-1] = X_Ferrite[-1]
			X_Pearlite[-1] = X_Pearlite[-1]
			X_Bainite[-1] = X_Bainite[-1]
			X_Martensite[-1] = 1.-X_Ferrite[-1]-X_Pearlite[-1]-X_Bainite[-1]
			break	
		
		#Extract Retained Austenite phase fraction
		X_Austenite.append(1. - (X_Ferrite[-1] + X_Pearlite[-1] + X_Bainite[-1] + X_Martensite[-1]))
		
		#Step forward integration time	
		int_time+= dt
	##############END OF INTEGRATION IN LOOP
	
	if int_time < time_end:
		X_Ferrite.append(X_Ferrite[-1])
		X_Pearlite.append(X_Pearlite[-1])
		X_Bainite.append(X_Bainite[-1])
		X_Martensite.append(X_Martensite[-1])
		X_Austenite.append(1. - (X_Ferrite[-1] + X_Pearlite[-1] + X_Bainite[-1] + X_Martensite[-1]))
		T_hist.append(T_end)
		t_hist.append(time_end)

	if T_hist[-1] >= T_end:
		X_Ferrite.append(X_Ferrite[-1])
		X_Pearlite.append(X_Pearlite[-1])
		X_Bainite.append(X_Bainite[-1])
		X_Martensite.append(X_Martensite[-1])
		X_Austenite.append(1. - (X_Ferrite[-1] + X_Pearlite[-1] + X_Bainite[-1] + X_Martensite[-1]))
		T_hist.append(T_end)
		t_hist.append(time_end)	
	
	print('=== Printing Phase history ===')
	############## Print out Phase history for this cooling rate
	lineg = '#CoolinRate -'+str(coolingRate)+' (C/s), Time (s), Temp (C), X_Ferrite, X_Pearlite, X_Bainite, X_Martensite, Aust_D, X_Austenite, \n'
	g.write(lineg)
	line = '    _F(VALE = (\n        -'+str(coolingRate)+', '+str(D)+'e-6, 0., 0.,\n        0., 0., 0., 0.,\n'
	f.write(line)
	for i in range(0,min(len(t_hist),len(T_hist),len(X_Ferrite),len(X_Pearlite),len(X_Bainite),len(X_Martensite),len(aust),len(X_Austenite),)):
		lineg = str(t_hist[i])+', '+str(T_hist[i])+', '+str(X_Ferrite[i])+', '+str(X_Pearlite[i])+', '+str(X_Bainite[i])+', '+str(X_Martensite[i])+', '+str(aust[i])+', '+str(X_Austenite[i])+'\n'
		line = '        '+str(X_Ferrite[i])+', '+str(X_Pearlite[i])+', '+str(X_Bainite[i])+', '+str(T_hist[i])+',\n'
		f.write(line)
		g.write(lineg)
	line = '    ,),),\n'
	f.write(line)
	lineg = '    NEXT\n'
	g.write(lineg)	
line = '),\nTEMP_MS=_F( SEUIL=0.38,\n    AKM=-30.791,\n    BKM=11.7,\n    TPLM=-0.5,),\n    GRAIN_AUST=_F(DREF = '+str(D)+'E-6,\n    A = 11200.),);\n'
f.write(line)

f.close()
g.close()
#s = input('--> ')  

print('============== PROGRAM ENDED ==============')



