import numpy as np
import matplotlib.pyplot as plt
import scipy as sp

ax = plt.figure(1)

data = np.loadtxt("supernova_data.txt")

#plt.plot(data[:,0],data[:,2])

c = 300000.0 
v = data[:,0]*c
d = data[:,2]
dd = data[::,3]
dv = data[:,1]*c

w=np.reciprocal(np.sqrt(dd))


from numpy.polynomial import polynomial as P

#k, stats = np.polyfit(v,d,1,w=w,cov=True)

k=1
stats=1

# np.polyfit(v,d,1,full=True,w=w)



print k
#print np.sqrt(np.diag(stats))
print stats

line1, =plt.plot(d,d*64.38, label='Fitting with V vs. D')

line2, =plt.plot(d,d*67.48, label='Fitting with D vs. V')

line3, =plt.plot(d,d*68.76, label='Fitting with D vs. V. with errors as weights ')

#plt.legend([line1,line2,line3])

#plt.plot(d,v,'.')

plt.errorbar(d,v,dv,dd,fmt="s",marker="o", color="k", ecolor="r")

plt.xlabel('Distance (Mpc)')
plt.ylabel('Velocity (km/s)')
plt.title('Type Ia Supernovae')

textstr = '(68.76 $\pm$ 20.09) km/(s*Mpc) \n  (67.48 $\pm$ 17.36) km/(s*Mpc) \n  (64.38 $\pm$ 3.74) km/(s*Mpc)'

ax.text(0.52, 0.4, textstr, fontsize=14,
        verticalalignment='top')

plt.savefig("snfig")

