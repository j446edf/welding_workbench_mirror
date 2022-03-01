#!/usr/bin/env python

###
### This file is generated automatically by SALOME v9.3.0 with dump python functionality
###

import os
import numpy as np
import matplotlib
import matplotlib.cm as cm
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import pandas as pd

############################
#format

W=2.0
BB=0.05
FS=6
GR=0.5+0.5*(5**0.5)
matplotlib.rcParams.update({'font.size': FS})

####

#For interpolating time base (simulation)
x_int_sim = np.arange(0,300,0.5).tolist()
x_ints_sim=[]
y_ints_sim=[]
sim_x_int_pass=[]
sim_y_int_pass=[]
#For interpolating time base (Experiment)
x_int_exp = np.arange(0,300,0.5).tolist()
x_ints_exp=[]
y_ints_exp=[]
exp_x_int_pass=[]
exp_y_int_pass=[]
####

## INTERPOLATE SIM DATA
filesToRead=1
tcNumber=int(float(os.getenv('USER_INP_NO_OF_TC')))
#tcNumber=5

for i in range(0,filesToRead):
	fig=plt.figure()
	plt.xlabel('Time (s)')
	plt.ylabel('Temperature (C)')
	plt.xlim([0.,300.])
	plt.ylim([0.,500.])
	for j in range(0,tcNumber):
		fileOpen = './mergeT_Pass_'+str(i+1)+'_TC'+str(j+1)+'.csv'
		df = pd.read_csv(fileOpen)
		df_keys=df.keys()
		x=df[df_keys[0]]
		y=df[df_keys[1]]
		y_int_sim = np.interp(x_int_sim,x,y)
		x_ints_sim.append(x_int_sim)
		y_ints_sim.append(y_int_sim)
		if j < 3:
			labels='TC_'+str(j+1)
		else:
			labels='TC_'+str(j+1+2)
		#plt.plot(x.subtract(0.),y,color=((5-j)/5.,0.,j/5.),label=labels)
		plt.plot(x.subtract(0.),y,color=((tcNumber-j)/tcNumber,0.,j/tcNumber),label=labels)
		plt.legend(fontsize=FS)
		sim_x_int_pass=[x_ints_sim]
		sim_y_int_pass=[y_ints_sim]
	fig.savefig('Sim_Pass_'+str(i+1),bbox_inches='tight',pad_inches=BB)

## Interpolate EXP data
# Manipulate cleaned csv data with Pandas
################################ connect UI option so chosen file is read here (force correct format) ###########################
exp_data=os.getenv('USER_INP_TC_EXP')
print(exp_data)
for i in range(0,filesToRead):
	fileOpen2 = 'clean_TG8_2_3_B_passe'+str(i+1)+'.txt'
	#fielOpen2 = str(exp_data)
	#print(fileOpen2)
	df = pd.read_csv(fileOpen2)
	df_keys=df.keys()
	

	# Extract Time/Temp history for each TC
	for j in range(0,10):
		if j not in [3,4,7,8,9]:
			x=df[df_keys[(j*2)]]
			y=df[df_keys[(j*2)+1]]
			y_int_exp = np.interp(x_int_exp,x,y)
			x_ints_exp.append(x_int_exp)
			y_ints_exp.append(y_int_exp)

#### Compare on same time base
deltaT_exp=[]
deltaT_sim=[]
for i in range(0,len(x_ints_exp)):
	fig=plt.figure()
	plt.xlabel('Time (s)')
	plt.ylabel('Temperature (C)')
	plt.xlim([0.,300.])
	plt.ylim([0.,500.])
	if j < 3:
		labels='TC_'+str(j+1)
		labels_='SIM_TC_'+str(j+1)
	else:
		labels='TC_'+str(j+1+2)
		labels_='SIM_TC_'+str(j+1+2)
	#plt.plot(x_ints_exp[i],y_ints_exp[i],color=((5-i)/5.,0.,i/5.),label=labels,marker='o',linewidth=2.,linestyle='-')
	#plt.plot(x_ints_sim[i],y_ints_sim[i],color=((5-i)/5.,0.,i/5.),label=labels_,linewidth=2.,linestyle='-')
	plt.plot(x_ints_exp[i],y_ints_exp[i],color=((tcNumber-i)/tcNumber,0.,i/tcNumber),label=labels,marker='o',linewidth=2.,linestyle='-')
	plt.plot(x_ints_sim[i],y_ints_sim[i],color=((tcNumber-i)/tcNumber,0.,i/tcNumber),label=labels_,linewidth=2.,linestyle='-')
	plt.legend(fontsize=FS)
	fig.savefig('crossCompare_TC'+str(i+1),bbox_inches='tight',pad_inches=BB)
	deltaT_exp.append(max(y_ints_exp[i])-y_ints_exp[i][0])
	deltaT_sim.append(max(y_ints_sim[i])-y_ints_sim[i][0])
	#print(len(y_ints_exp[i]))
	#print(float(max(y_ints_exp[i]))-float(y_ints_exp[i][0]))

print('dT exp',deltaT_exp)
print('dT sim',deltaT_sim)

## Calculate Error RMS
# individual RMS

######################### UI option for selecting near and far field tc needed ############################
ind_RMS=[]
for i in range(0,len(deltaT_exp)):
	ind_RMS.append((((deltaT_sim[i]-deltaT_exp[i])/deltaT_exp[i])**2)**0.5)
	if i  < 3:
		print('TC_%s_RMS = ' % str(i), np.round(100.*ind_RMS[-1],decimals=1), '%')
	else:
		print('TC_%s_RMS = ' % str(i+2), np.round(100.*ind_RMS[-1],decimals=1), '%')

calibRMS = (0.5*( (((deltaT_sim[2]-deltaT_exp[2])/deltaT_exp[2])**2) +  (((deltaT_sim[4]-deltaT_exp[4])/deltaT_exp[4])**2) ))**0.5
print('calibrated_RMS = ', np.round(100.*calibRMS,decimals=1), '%')
