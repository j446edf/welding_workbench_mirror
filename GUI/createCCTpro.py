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

print('=== Plot CCT ===')

##########################################################################
# DO NOT ALTER! - basicBatch.sh modifies these parameters automatically
##########################################################################
#Transformation start/end limits
trans_start = 0.01
trans_fin = 0.99
D = float(os.getenv('USER_INP_GS'))
G = SSPT.ASTM_Grain(D)  #G=8.3#<-------------- USED in Li et al. and Hamelin et al.
grainGrowthMethod = os.getenv('USER_INP_grainGrowthMethod')
material = os.getenv('USER_INP_material')
ae13Choice = os.getenv('USER_INP_ae13CHOICE')
# D=17.9 #15.;#micron grain size used by Yongle in Jomimy benchmark
# G = SSPT.ASTM_Grain(D)  #G=8.3#<-------------- USED in Li et al. and Hamelin et al.
# grainGrowthMethod='CONSTANT'
# material='SA508'
# ae13Choice='Grange'

if material == 'USER':
	inputComp = sys.argv[2].strip('()[]')
	inputComp = inputComp.split(',')
	inputComposition=[float(i) for i in inputComp]

else:
	inputComposition = "0"
##########################################################################
# DO NOT ALTER - Autocomputation of key temperatures
##########################################################################
composition = SSPT.setComposition(material,inputComposition)	
AE1,AE3 = SSPT.Ae13Temperature(composition,ae13Choice)
Ms = SSPT.calcMs(composition)
Bs = SSPT.calcBs(composition)


t_Ms = math.log(((850. - Ms)/15),10)
Mf = Ms - 200.
t_Mf = math.log(((850. - Mf)/15),10)


########### Testing Hamelin method.. 

T_aust = float(os.getenv('USER_INP_T_aust')) #Celsius
#T_aust = 1000. #Celsius


### Set range on cooling rates
cr_high = 10000.
cr_low = 0.0000001

refine = 1
logCR = list(range(int(math.log(cr_low,10))*refine,int(math.log(cr_high,10))*refine))
for i in range(0,len(logCR)):
	logCR[i] = float(logCR[i])/float(refine)

print(logCR)

#Initialise CCT diagram data
CCT_t_B=[]
CCT_T_B=[]
CCT_t_Be=[]
CCT_T_Be=[]
CCT_t_F=[]
CCT_T_F=[]
CCT_t_Fe=[]
CCT_T_Fe=[]
CCT_t_P=[]
CCT_T_P=[]
CCT_t_Pe=[]
CCT_T_Pe=[]

# Calculate CCT Bainite Start	
for i in range(0,len(logCR)):
	coolingRate = 10.**logCR[i]
	
	#Initialise calculation parameters
	D_vary = D # takes in micron
	int_time = 0. # s
	dt = 1./coolingRate
	sum_dt_dtau = 0.
	X_nuc = 0.01
	while sum_dt_dtau < 1.:
		T_eq = SSPT.eqIsodT(int_time,dt,coolingRate,T_aust) # C
		D_vary+= SSPT.calc_dD(D_vary,T_eq,dt,grainGrowthMethod,AE3)#outputs in mm
		G_vary = SSPT.ASTM_Grain(D_vary)
		if T_eq <=Ms:
			break
		if T_eq <= Bs:
			tauB_Tnow = SSPT.calcTauB(X_nuc,T_eq,G_vary,composition)
		else:
			tauB_Tnow = 10.**9.
		dt_tauB_Tnow = dt/tauB_Tnow
		sum_dt_dtau+=dt_tauB_Tnow
		int_time+= dt
	
	#Check solution
	if T_eq < Ms:
		CCT_T_B.append(Ms)	
		print(CCT_T_B)
		CCT_t_B.append(math.log(int_time,10))
		print(CCT_t_B)
	elif T_eq < Bs:
		CCT_T_B.append(T_eq)
		CCT_t_B.append(math.log(int_time,10))
	else:
		CCT_T_B.append(Bs)
		CCT_t_B.append(math.log(int_time,10))
print(CCT_t_B,CCT_T_B)

# Calculate CCT Bainite end	
for i in range(0,len(logCR)):
	coolingRate = 10.**logCR[i]
	
	#Initialise calculation parameters
	D_vary = D
	int_time = 0. # s
	dt = 1./coolingRate
	sum_dt_dtau = 0.
	X_nuc = 0.999
	while sum_dt_dtau < 1.:
		T_eq = SSPT.eqIsodT(int_time,dt,coolingRate,T_aust) # C
		D_vary+= SSPT.calc_dD(D_vary,T_eq,dt,grainGrowthMethod,AE3)#outputs in mm
		G_vary = SSPT.ASTM_Grain(D_vary)
		if T_eq <=Ms:
			break
		if T_eq <= Bs:
			tauB_Tnow = SSPT.calcTauB(X_nuc,T_eq,G_vary,composition)
		else:
			tauB_Tnow = 10.**9.
		dt_tauB_Tnow = dt/tauB_Tnow
		sum_dt_dtau+=dt_tauB_Tnow
		int_time+= dt
	
	#Check solution
	if T_eq < Ms:
		CCT_T_Be.append(Ms)	
		CCT_t_Be.append(math.log(int_time,10))
	elif T_eq < Bs:
		CCT_T_Be.append(T_eq)
		CCT_t_Be.append(math.log(int_time,10))
	else:
		CCT_T_Be.append(Bs)
		CCT_t_Be.append(math.log(int_time,10))
print(CCT_t_Be,CCT_T_Be)


# Calculate CCT Ferrite Start	
for i in range(0,len(logCR)):
	coolingRate = 10.**logCR[i]
	
	#Initialise calculation parameters
	D_vary = D
	int_time = 0. # s
	dt = 1./coolingRate
	sum_dt_dtau = 0.
	X_nuc = 0.01
	while sum_dt_dtau < 1.:
		T_eq = SSPT.eqIsodT(int_time,dt,coolingRate,T_aust) # C
		D_vary+= SSPT.calc_dD(D_vary,T_eq,dt,grainGrowthMethod,AE3)#outputs in mm
		G_vary = SSPT.ASTM_Grain(D_vary)
		if T_eq <=Ms:#Bs:
			break
		if T_eq <= AE3:
			tauF_Tnow = SSPT.calcTauF(X_nuc,T_eq,AE3,G_vary,composition)
		else:
			tauF_Tnow = 10.**9.
		dt_tauF_Tnow = dt/tauF_Tnow
		sum_dt_dtau+=dt_tauF_Tnow
		int_time+= dt
	
	#Check solution
	if T_eq < Ms:#Bs:
		CCT_T_F.append(Ms)#Bs)	
		CCT_t_F.append(math.log(int_time,10))
	elif T_eq < AE3:
		CCT_T_F.append(T_eq)
		CCT_t_F.append(math.log(int_time,10))
	else:
		CCT_T_F.append(AE3)
		CCT_t_F.append(math.log(int_time,10))
print(CCT_t_F,CCT_T_F)

# Calculate CCT Ferrite end	
for i in range(0,len(logCR)):
	coolingRate = 10.**logCR[i]
	
	#Initialise calculation parameters
	D_vary = D
	int_time = 0. # s
	dt = 1./coolingRate
	sum_dt_dtau = 0.
	X_nuc = 0.999
	while sum_dt_dtau < 1.:
		T_eq = SSPT.eqIsodT(int_time,dt,coolingRate,T_aust) # C
		D_vary+= SSPT.calc_dD(D_vary,T_eq,dt,grainGrowthMethod,AE3)#outputs in mm
		G_vary = SSPT.ASTM_Grain(D_vary)		
		if T_eq <=Ms:#Bs:
			break
		if T_eq <= AE3:
			tauF_Tnow = SSPT.calcTauF(X_nuc,T_eq,AE3,G_vary,composition)
		else:
			tauF_Tnow = 10.**9.
		dt_tauF_Tnow = dt/tauF_Tnow
		sum_dt_dtau+=dt_tauF_Tnow
		int_time+= dt
	
	#Check solution
	if T_eq < Ms:#Bs:
		CCT_T_Fe.append(Ms)#Bs)
		CCT_t_Fe.append(math.log(int_time,10))
	elif T_eq < AE3:
		CCT_T_Fe.append(T_eq)
		CCT_t_Fe.append(math.log(int_time,10))
	else:
		CCT_T_Fe.append(AE3)
		CCT_t_Fe.append(math.log(int_time,10))
print(CCT_t_Fe,CCT_T_Fe)
# Calculate CCT Pearlite Start	
for i in range(0,len(logCR)):
	coolingRate = 10.**logCR[i]
	
	#Initialise calculation parameters
	D_vary = D
	int_time = 0. # s
	dt = 1./coolingRate
	sum_dt_dtau = 0.
	X_nuc = 0.01
	while sum_dt_dtau < 1.:
		T_eq = SSPT.eqIsodT(int_time,dt,coolingRate,T_aust) # C
		D_vary+= SSPT.calc_dD(D_vary,T_eq,dt,grainGrowthMethod,AE3)#outputs in mm
		G_vary = SSPT.ASTM_Grain(D_vary)		
		if T_eq <=Ms:#Bs:
			break
		if T_eq <= AE1:
			tauP_Tnow = SSPT.calcTauP(X_nuc,T_eq,AE1,G_vary,composition)
		else:
			tauP_Tnow = 10.**9.
		dt_tauP_Tnow = dt/tauP_Tnow
		sum_dt_dtau+=dt_tauP_Tnow
		int_time+= dt
	
	#Check solution
	if T_eq < Ms:#Bs:
		CCT_T_P.append(Ms)#Bs)
		CCT_t_P.append(math.log(int_time,10))
	elif T_eq < AE1:
		CCT_T_P.append(T_eq)
		CCT_t_P.append(math.log(int_time,10))
	else:
		CCT_T_P.append(AE1)
		CCT_t_P.append(math.log(int_time,10))
print(CCT_t_P,CCT_T_P)

# Calculate CCT Pearlite End
for i in range(0,len(logCR)):
	coolingRate = 10.**logCR[i]
	
	#Initialise calculation parameters
	D_vary = D
	int_time = 0. # s
	dt = 1./coolingRate
	sum_dt_dtau = 0.
	X_nuc = 0.999
	while sum_dt_dtau < 1.:
		T_eq = SSPT.eqIsodT(int_time,dt,coolingRate,T_aust) # C
		D_vary+= SSPT.calc_dD(D_vary,T_eq,dt,grainGrowthMethod,AE3)#outputs in mm
		G_vary = SSPT.ASTM_Grain(D_vary)
		if T_eq <=Ms:#Bs:
			break
		if T_eq <= AE1:
			tauP_Tnow = SSPT.calcTauP(X_nuc,T_eq,AE1,G,composition)
		else:
			tauP_Tnow = 10.**9.
		dt_tauP_Tnow = dt/tauP_Tnow
		sum_dt_dtau+=dt_tauP_Tnow
		int_time+= dt
	
	#Check solution
	if T_eq < Ms:#Bs:
		CCT_T_Pe.append(Ms)#Bs)
		CCT_t_Pe.append(math.log(int_time,10))
	elif T_eq < AE1:
		CCT_T_Pe.append(T_eq)
		CCT_t_Pe.append(math.log(int_time,10))
	else:
		CCT_T_Pe.append(AE1)
		CCT_t_Pe.append(math.log(int_time,10))
print(CCT_t_Pe,CCT_T_Pe)





fig=plt.figure()
plt.plot(CCT_t_F,CCT_T_F,'r',label='Ferrite Start')
plt.plot(CCT_t_Fe,CCT_T_Fe,':r',label='Ferrite End')
plt.plot(CCT_t_P,CCT_T_P,'c',label='Pearlite Start')
plt.plot(CCT_t_Pe,CCT_T_Pe,':c',label='Pearlite End')
plt.plot(CCT_t_B,CCT_T_B,'b',label='Bainite Start')
plt.plot(CCT_t_Be,CCT_T_Be,':b',label='Bainite End')
plt.legend(loc='lower right',ncol=3,fontsize=10)
plt.xlabel('log (Time (s))')
plt.ylabel('Temperature (C)')
plt.xlim([-2,6])
plt.ylim([0,800])
#plt.show()

#plt.plot([-6,6],[AE1,AE1],'k',[-6,6],[AE3,AE3],'k',[-6,t_Ms],[Ms,Ms],'k',[-6,t_Mf],[Mf,Mf],'k')
plt.plot([-6,6],[AE1,AE1],'k',[-6,6],[AE3,AE3],'k',[-6,6],[Bs,Bs],'k',[-6,6],[Ms,Ms],'k',[-6,6],[Mf,Mf],'k')
plt.text(-0.5, AE1+5, 'Ae1', fontsize=12)
plt.text(-0.5, AE3+5, 'Ae3', fontsize=12)
plt.text(-0.5, Bs+5, 'Bs', fontsize=12)
plt.text(-0.5, Ms+5, 'Ms', fontsize=12)
plt.text(-0.5, Mf+5, 'Mf', fontsize=12)


CR=[]
itemstoclean=sys.argv[1].strip('()')
columns = itemstoclean.split(',')
print(type(columns))
for i in range(0,len(columns)):
	print(type(columns[i]))
	CR.append(float(columns[i]))
# CR=[]
# for i in range(1,len(sys.argv)):
	# CR.append(float(sys.argv[i]))
#CR = [0.01, 0.1,  1.,10.,  50.,100.,200.,300.,400., ] 
#Critical Cooling rate = -10C/s
k = 0
for j in CR:
	flag_print = 0
	index_print = 0
	l = 0
	critical_cooling_T = []
	critical_cooling_t = list(range(-6000,6000))
	for i in range(0,len(critical_cooling_t)):
		critical_cooling_t[i] = float(critical_cooling_t[i])/1000.
	for i in critical_cooling_t:
		critical_cooling_T.append(850.-j*(10**i))
		if int(850.-j*(10**i)) == 300:
			flag_print+=1
			if flag_print == 1:
				index_print+= l
				print(index_print)
		l+=1
	k+=1
	plt.plot(critical_cooling_t,critical_cooling_T,'k:')
	plt.text(critical_cooling_t[index_print],180+(k*20),('-'+str(j)+' C/s'), fontsize=8)
	print(j,k,350-(((k+3)%4)*25),critical_cooling_t[index_print],300+(k%2)*50)

	
fig.savefig('CCT_with_Cooling_Curves.png')	




