#!/usr/bin/env python

fileToRead=4
passToRead=2
fileOpen = 'PASS'+str(passToRead)+'_TCMESH_'+str(fileToRead)+'.resu'
f=open(fileOpen,'r')
datas=[]
datas2=[]
linecount=0
for line in f:
	if 'INST:' in line:
		line = line.strip()
		columns = line.split()
		datas.append(float(columns[4]))
	if 'N27' in line:
		line = line.strip()
		columns = line.split()
		datas2.append(float(columns[1]))
		print(columns)
fileWrite = 'mergeT_Pass_'+str(passToRead)+'_TC'+str(fileToRead)+'.csv'
f=open(fileWrite,'w')
f.write('\"arc_length\",\"THNONLI2TEMP\"')
f.close()
f=open(fileWrite,'a')
for i in range(0,len(datas)):
	writeme='\n'+str(datas[i])+','+str(datas2[i])
	f.write(writeme)
f.close()
