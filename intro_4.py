import matplotlib
#%matplotlib PyQt5
#matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import numpy as np

lit = []
k_eff =[]
ind = []
std = []
for line in open('sss_log'):
    if line.startswith('k-eff (implicit)'):# or line.startswith('Referer'):
       lit.append(line)
#print(lit[1][19:26])
for i in lit:
	k_eff.append(i[19:26])
k_eff = [float(i) for i in k_eff] 

for i in range(len(k_eff)):
	ind.append(i)
	
for j in lit:
	std.append(j[32:37])
std = [float(j) for j in std]
#print(std[1])
zipped_lists = zip(k_eff, std)
y_max = [x + y for (x,y) in zipped_lists]

y_min =[]
zipped_obj = zip(k_eff, std)
for i,j in zipped_obj:
	y_min.append(i-j)
#print(y_min)

fig= plt.figure(1, figsize=(6,10))
fig, ax = plt.subplots()
ax.plot(ind,k_eff)
#plt.show()
ax.fill_between(k_eff,y_min,y_max,facecolor=(0,0,1),alpha=0.2 )
fig.savefig('demo.pdf')
