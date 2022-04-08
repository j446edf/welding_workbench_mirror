###################################
# Author: Jefri Draup
# Email: jefri.draup@edfenergy.com
###################################
import matplotlib.pyplot as plt
import math
import numpy as np
import sys
################ List of Functions associate with SSPT of Hamelin et al. 
def setComposition(material,inputComposition):
    "Sets the composition of the material. If user defines composition (material == USER), the format must be %weight [C, Mn, Si, Ni, Cr, Mo, V, W, Cu, P, Al, As, Ti, Co]"
    if material == 'SA508':
        composition = [0.2, 1.4, 0.25, 0.8, 0.2, 0.5, 0.003, 0.00, 0.04, 0.00, 0.003, 0.00, 0.00, 0.00]
        print(type(composition[0]))
    if material == '4140':
        composition = [0.37,0.77,0.15,0.04,0.98,0.21,0.,0.,0.,0.,0.,0.,0.,0.]
    if material == '16MND5':
        composition = [0.36,0.77,0.28,0.16,0.96,0.28,0.,0.,0.,0.,0.,0.,0.,0.]
    if material == 'USER':
        assert type(inputComposition) == list, "If material == USER, You must pass in a second argument - a list of chemical compositions in % weight of the form [C, Mn, Si, Ni, Cr, Mo, V, W, Cu, P, Al, As, Ti, Co]"
        assert len(inputComposition) == 14, "Your composition must contain these chemicals in the following order: (C, Mn, Si, Ni, Cr, Mo, V, W, Cu, P, Al, As, Ti, Co)"
        composition = []
        for i in inputComposition:
            assert type(i) == float, "Each entry for you material composition must be entered as % weight of type float"
            composition.append(i)
    return composition

def extractComp(composition):
	"Returns the individual components of the alloy chemical composition"
	C = composition[0]
	Mn = composition[1]
	Si = composition[2]
	Ni = composition[3]
	Cr = composition[4]
	Mo = composition[5]
	V = composition[6]
	W = composition[7]
	Cu = composition[8]
	P = composition[9]
	Al = composition[10]
	As = composition[11]
	Ti = composition[12]
	Co = composition[13]
	return C, Mn, Si, Ni, Cr, Mo, V, W, Cu, P, Al, As, Ti, Co

##################################################
######## List of functions for creating TTT
##################################################

#Calculates the Ae temperatures based on composition
# Equivalent of Temperature.m
def Ae13Temperature(composition, Method):
	"This returns the Ae1 and Ae3 temperatures in (C) from the user defined chemical composition of ferritic alloy and the method. For theory details consult https://doi.org/10.1016/j.actamat.2014.04.045 or http://www.chte.org/d/file/p/2013-01-22/bbf30bc70b449796e79d568fe864a802.pdf"
	C, Mn, Si, Ni, Cr, Mo, V, W, Cu, P, Al, As, Ti, Co = extractComp(composition)
	try:
		if Method == 'Grange':
			# Formulae of Grange
			AE1 = (1333. + 0.*float(C) - 25.*float(Mn) + 40.*float(Si) - 26.*float(Ni) + 42*float(Cr) + 0.*float(Mo) - 32.)*5./9.
			AE3 = (1570. - 323.*float(C) -25.*float(Mn) + 80.*float(Si) -32.*float(Ni) -3*float(Cr) + 0.*float(Mo) - 32.) * 5. / 9.
			return AE1, AE3
		if Method == 'Andrews':
			# Formulae of Andrews
			#AE1 = 712. + 0.*float(C) - 17.8*float(Mn) + 20.1*float(Si) - 19.1*float(Ni) - 11.9*float(Cr) + 9.8*float(Mo)
			#AE3 = 871. - (254.4*(float(C)**0.5)) + 0.*float(Mn) + 51.7*float(Si) -14.2*float(Ni) + 0.*float(Cr) + 0.*float(Mo) 
			AE1 = 723. - 10.7*float(Mn) + 29.1*float(Si) - 16.9*float(Ni) - 16.9*float(Cr) + 290.*float(As) +6.38*float(W)
			AE3 = 910. - (203.*(float(C)**0.5)) + 44.7*float(Si) - 15.2*float(Ni) +31.5*float(Mo) + 104.*float(V) + 13.1*float(W) - 30.*float(Mn) +11.*float(Cr) + 20.*float(Cu) - 700.*float(P) - 400.*float(Al) - 120.*float(As) - 400.*float(Ti)
			return AE1, AE3
		if Method == 'Eldis':
			# Formulae Eldis
			AE1 = 712. + 0.*float(C) - 17.8*float(Mn) + 20.1*float(Si) - 19.1*float(Ni) - 11.9*float(Cr) + 9.8*float(Mo)
			AE3 = 871. - (254.4*float(C)**0.5) + 0.*float(Mn) + 51.7*float(Si) -14.2*float(Ni) + 0.*float(Cr) + 0.*float(Mo)
			return AE1, AE3
	except:
		print('There is an error in your composition somehow...')


# Calculates the Sigmoidal function
def calcSig(Xend):
	"Calculates reaction rate as a function of phase fraction"
	S=0
	dX = 1000
	for i in range(1,dX):
		x=float(Xend)*float(i)/float(dX)
		if i == 1:
			x1=float(Xend)*float(float(i)-0.999)/float(dX)
		else:
			x1=float(Xend)*float(i-1)/float(dX)
		y=1./((x**(0.4*(1-x)))*((1-x)**(0.4*x)))
		y1=1./((x1**(0.4*(1-x1)))*((1-x1)**(0.4*x1)))
		area = (x-x1)*0.5*(y+y1)
		S = S + area
	return S

## Used to calculate 

def calcMs(composition):
	"Calculates Ms in (C) from chemical composition"
	C, Mn, Si, Ni, Cr, Mo, V, W, Cu, P, Al, As, Ti, Co = extractComp(composition)
	Ms = 539. - 423.*float(C) -30.4*float(Mn) -17.7*float(Ni) -12.1*float(Cr) -7.5*float(Mo) +10.*float(Co) - 7.5*float(Si)	
	return Ms

def calcBs(composition):
	"Calculates Bs in (C) from chemical composition"
	C, Mn, Si, Ni, Cr, Mo, V, W, Cu, P, Al, As, Ti, Co = extractComp(composition)
	Bs = 637. - 58.*float(C) -35.*float(Mn) -15.*float(Ni) -34.*float(Cr) -41.*float(Mo)
	return Bs

def calcFC(composition):
	"Calculates FC from chemical composition"
	C, Mn, Si, Ni, Cr, Mo, V, W, Cu, P, Al, As, Ti, Co = extractComp(composition)
	FC = math.exp(1. + 6.31*float(C) + 1.78*float(Mn) +0.31*float(Si) +1.12*float(Ni) +2.7*float(Cr) +4.06*float(Mo))
	return FC

def calcPC(composition):
	"Calculates PC from chemical composition"
	C, Mn, Si, Ni, Cr, Mo, V, W, Cu, P, Al, As, Ti, Co = extractComp(composition)
	PC = math.exp(-4.25 + 4.12*float(C) + 4.36*float(Mn) +0.44*float(Si) +1.71*float(Ni) +3.33*float(Cr) +5.19*float(Mo)**0.5)
	return PC

def calcBC(composition):
	"Calculates MC from chemical composition"
	C, Mn, Si, Ni, Cr, Mo, V, W, Cu, P, Al, As, Ti, Co = extractComp(composition)
	#BC = math.exp(1. + 6.31*float(C) + 1.78*float(Mn) +0.31*float(Si) +1.12*float(Ni) +2.7*float(Cr) +4.06*float(Mo))### AS QUOTED IN HAMELIN ET AL
	BC = math.exp(-10.23 + 10.18*float(C) + 0.85*float(Mn) +0.55*float(Ni) +0.9*float(Cr) +0.36*float(Mo))#AS QUOTED IN LI!
	return BC


### Functions for tau

def calcTauF(X,T, AE3, G, composition):
	"Calculates time to form X phase fraction of Ferrite under isothermal conditions"
	C, Mn, Si, Ni, Cr, Mo, V, W, Cu, P, Al, As, Ti, Co = extractComp(composition)
	T=float(T)+273.15
	AE3=float(AE3)+273.15
	FC = calcFC(composition)
	SigX = calcSig(X)
	undercooling = (AE3-T)**3
	arrhenius = math.exp((-27500*4.186)/8.314/T)
	FG = (2.**(0.41*float(G)))
	FT = undercooling*arrhenius*FG
	tauF = FC*SigX/FT
	return tauF
	
	
def calcTauP(X,T, AE1, G, composition):
	"Calculates time to form X phase fraction of Pearlite under isothermal conditions"
	C, Mn, Si, Ni, Cr, Mo, V, W, Cu, P, Al, As, Ti, Co = extractComp(composition)
	T=float(T)+273.15
	AE1=float(AE1)+273.15
	PC = calcPC(composition)
	SigX = calcSig(X)
	undercooling = (AE1-T)**3
	arrhenius = math.exp((-27500*4.186)/8.314/T)
	FG = (2.**(0.32*float(G)))
	FT = undercooling*arrhenius*FG
	tauP = PC*SigX/FT
	return tauP
	
	
def calcTauB(X,T, G, composition):
	"Calculates time to form X phase fraction of Bainite under isothermal conditions"
	C, Mn, Si, Ni, Cr, Mo, V, W, Cu, P, Al, As, Ti, Co = extractComp(composition)
	T=float(T)+273.15
	Bs = calcBs(composition)+273.15
	BC = calcBC(composition)
	SigX = calcSig(X)
	undercooling = (Bs-T)**2
	arrhenius = math.exp((-27500*4.186)/8.314/T)
	FG = (2.**(0.29*float(G)))
	FT = undercooling*arrhenius*FG
	tauB = BC*SigX/FT
	return tauB

	
def ASTM_Grain(D):
	"Converts from grain size (micron) to ASTM Grain Size Number assuming spherical grains"
	D=float(D)+0.
	shape = 400./3.142
	G = math.log(2.,10) + math.log((shape*(25.4/D)**2),10)/math.log(2.,10)
	return G
    
def calc_dD(D0,T_eq,dt,modelFlag,AE3):
	"Calculates change in austenite grain size dD based on Ikawa grain growth model. Note this is known to overpredict grain growth in welds. Takes grain size in micron, performs calculation in mm, returns grain size in micron"
	D=0.001*float(D0) #convert micron to mm
	T=float(T_eq)+273.15
	
	if modelFlag == 'IKAWA':
		DF_4=((2.969e15)*(dt/60.)*math.exp(-69300/T))  # note time in mins according to Ikawa
		D0_4=(D)**4
		DF=((DF_4+D0_4)**0.25) #in mm
		dD=1000*(DF - D) #in micron
	
	if modelFlag == 'CONSTANT':
		dD=0.
		
	if modelFlag == 'TWORATE':
		D=1000*D*1e-6 ##convert mm to micron to metres
		Tc = 1020.+273.15 #in Kelvin
		A1 = 4.2 # in um^2/s
		A2 = 16.8 # in um^2/s
		Dlim = (3 + 0.58*(T-(AE3+273.15)))*1e-6 #in metres
		Q = 190000. #in Joules
		if T <= Tc:
			dLdt = A1*((1/D)-(1/Dlim))*math.exp(-Q/(8.314)/T) #output relation is in micron/s according to Sun et al
			dD = dt*dLdt #output in micron
		else:
			dLdt = A2*(1/D)*math.exp(-Q/(8.314)/T) #output relation is in micron/s according to Sun et al
			dD = dt*dLdt #output in micron
				
	return dD
	
def calc_D_Ikawa(D0,dt,T_eq,sumVar):
	"Calculates austenite grain size D based on Ikawa grain growth model. Note this is known to overpredict grain growth in welds. Takes grain size in micron, performs calculation in mm, returns grain size in micron"
	D=0.001*float(D0) #convert micron to mm
	T=float(T_eq)+273.15
	dt=float(dt)/60.
	DF_4=float(sumVar) + ((2.969e15)*dt*math.exp(-69300/T))  # note time in mins according to Ikawa
	D0_4=(D)**4
	DF=((DF_4+D0_4)**0.25) #in mm
	D=1000*(DF) #in micron		
				
	return D,DF_4	
    
##################################################
######## List of functions for creating CCT
##################################################	

def eqIsodT(t_now,dt,coolingRate,T_peak):
	"Calculates the equivalent temperature (C) for the current dt"
	T_peak = float(T_peak)+273.15
	T_now = float(T_peak) - (float(coolingRate)*float(t_now))
	T_dt = float(T_peak) - (float(coolingRate)*(float(t_now)+float(dt)))
	T_eq = 0.5*(T_now + T_dt) - 273.15
	return T_eq

def calcdXdt_F(X,T, AE3, G, composition):
	"Calculates the rate of change in ferritic phase dXdt formed during dt"
	C, Mn, Si, Ni, Cr, Mo, V, W, Cu, P, Al, As, Ti, Co = extractComp(composition)
	T=float(T)+273.15
	X=float(X)
	AE3=float(AE3)+273.15
	undercooling = (AE3-T)**3
	FG = (2.**(0.41*float(G)))
	FC = calcFC(composition)
	arrhenius = 1.#math.exp((-27500*4.186)/8.314/T)
	FX = ((X**(0.4*(1-X)))*((1-X)**(0.4*X)))
	dXdt = undercooling*arrhenius*FX/(FC*FG)
	return dXdt

def calcdX_M(T_eq,Ms):
	"Calculates the martensite phase at current temperature - only valid if Mf < T < Ms"
	T = float(T_eq)
	M_Start = float(Ms)
	M_Finish = M_Start - 200.
	X = (M_Start - T) / (M_Start - M_Finish)
	return X

#def calcdX_M_dt(T_eq,Ms,CR,dt):
	#"Calculates the martensite phase at current temperature - only valid if Mf < T < Ms"
	#T = float(T_eq)
	#CR = 0. - float(CR)
	#dt = float(dt)
	#M_Start = float(Ms)
	#M_Finish = M_Start - 200.
	#dX = (-1*CR*dt) / (M_Start - M_Finish)
	#return dX
