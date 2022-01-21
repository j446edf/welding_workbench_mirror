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

########## GENERATING TTT DIAGRAM

print('=== Plot TTT ===')
#Transformation start/end limits
trans_start = 0.01
trans_fin = 0.99
#Grain Size (micron)
D = float(os.getenv('USER_INP_GS'))
G = SSPT.ASTM_Grain(D)  #G=8.3#<-------------- USED in Li et al. and Hamelin et al.
grainGrowthMethod = os.getenv('USER_INP_grainGrowthMethod')
material = os.getenv('USER_INP_material')
ae13Choice = os.getenv('USER_INP_ae13CHOICE')
# D=17.9  #15.;#micron grain size used by Yongle in Jomimy benchmark
# G = SSPT.ASTM_Grain(D)  #G=8.3#<-------------- USED in Li et al. and Hamelin et al.
# grainGrowthMethod='CONSTANT' #<----- NOTE TTT does not know anything about grain growth as it does not require time history info
# material='SA508'
# ae13Choice='Grange'

if material == 'USER':
	inputComp = sys.argv[2].strip('()[]')
	inputComp = inputComp.split(',')
	inputComposition=[float(i) for i in inputComp]
	#s=input('--> ')
else:
	inputComposition = "0"

composition = SSPT.setComposition(material,inputComposition)	

AE1,AE3 = SSPT.Ae13Temperature(composition,ae13Choice)
Ms = SSPT.calcMs(composition)#SA508
Bs = SSPT.calcBs(composition)
t_Ms = math.log(((850. - Ms)/15),10)
Mf = Ms - 200.
t_Mf = math.log(((850. - Mf)/15),10)


taus_F=[]
temps_F=[]
for temp in range(int(Bs),int(AE3)):
	temps_F.append(float(temp))
	taus_F.append(math.log(SSPT.calcTauF(trans_start,float(temp),AE3,G,composition),10))#SA508
	
taus_Fe=[]
temps_Fe=[]
for temp in range(int(Bs),int(AE3)):
	temps_Fe.append(float(temp))
	taus_Fe.append(math.log(SSPT.calcTauF(trans_fin,float(temp),AE3,G,composition),10))#SA508

taus_P=[]
temps_P=[]
for temp in range(int(Bs),int(AE1)):
	temps_P.append(float(temp))
	taus_P.append(math.log(SSPT.calcTauP(trans_start,float(temp),AE1,G,composition),10))#SA508

taus_Pe=[]
temps_Pe=[]
for temp in range(int(Bs),int(AE1)):
	temps_Pe.append(float(temp))
	taus_Pe.append(math.log(SSPT.calcTauP(trans_fin,float(temp),AE1,G,composition),10))#SA508

taus_B=[]
temps_B=[]
for temp in range(int(Ms),int(Bs)):
	temps_B.append(float(temp))
	taus_B.append(math.log(SSPT.calcTauB(trans_start,float(temp),G,composition),10))#SA508

taus_Be=[]
temps_Be=[]
for temp in range(int(Ms),int(Bs)):
	temps_Be.append(float(temp))
	taus_Be.append(math.log(SSPT.calcTauB(trans_fin,float(temp),G,composition),10))#SA508
	

fig=plt.figure()
plt.plot([-6,6],[AE1,AE1],'k',[-6,6],[AE3,AE3],'k',[-6,6],[Bs,Bs],'k',[-6,6],[Ms,Ms],'k',[-6,6],[Mf,Mf],'k')
plt.text(-0.5, AE1+5, 'Ae1', fontsize=12)
plt.text(-0.5, AE3+5, 'Ae3', fontsize=12)
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

#plt.plot(critical_cooling_t,critical_cooling_T,'k:')
#plt.text(-0., 860., 'Critical cooling rate =15C/s', fontsize=12)
#plt.plot(cooling100_t,cooling100_T,'k:')
#plt.text(-1.5, 860., 'Cooling rate =100C/s', fontsize=12)

plt.plot(taus_F,temps_F,'r',label='Ferrite Start')
plt.plot(taus_Fe,temps_Fe,':r',label='Ferrite End')
plt.plot(taus_P,temps_P,'c',label='Pearlite Start')
plt.plot(taus_Pe,temps_Pe,':c',label='Pearlite End')
plt.plot(taus_B,temps_B,'b',label='Bainite Start')
plt.plot(taus_Be,temps_Be,':b',label='Bainite End')
plt.legend(loc='lower right',ncol=3,fontsize=10)
plt.xlabel('log (Time (s))')
plt.ylabel('Temperature (C)')
plt.xlim([-2,6])
plt.ylim([0,800])
fig.savefig('TTT_with_Cooling_Curves.png')
#plt.show()

