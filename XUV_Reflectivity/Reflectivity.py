from pylab import *
import pandas as pd
close('all')
# load optical constant
# nrg, n, k = np.genfromtxt('Au_Constants.txt', dtype = float, skip_header = 1, usecols = (0,1,2), delimiter = ',', unpack = True)

d = pd.read_csv('SiO2_Constants.txt', skiprows = 1, delimiter = ',')
nrg = d.values[:,0]
n = d.values[:,1]
k = d.values[:,2]

N = n - 1j*k
lam = 1239.842/nrg

theta = np.array([5, 10,20, 30, 40,45, 50, 60, 70, 80, 85])

plotme = where(theta == 70)[0][0]

pts = len(theta)
pts2 = len(N)

R_s = np.zeros((pts,pts2))
R_p = np.zeros((pts,pts2))

def Rs(theta, n):
    theta *= pi/180
    return abs(np.cos(theta) - (n**2-np.sin(theta)**2)**.5) ** 2 / abs(np.cos(theta) + (n**2-np.sin(theta)**2)**.5) ** 2

def Rp(theta, n):
    theta *= pi/180
    return abs(n**2*np.cos(theta) - (n**2-np.sin(theta)**2)**.5) ** 2 / abs(2**2*np.cos(theta) + (n**2-np.sin(theta)**2)**.5) ** 2


for i in range(pts):
    for k in range(pts2):
        R_s[i,k] = Rs(theta[i], N[k])
        R_p[i,k] = Rp(theta[i], N[k])

f, ax = plt.subplots(1,2, figsize = (16,8))
color_idx = np.linspace(0, 1, pts)
for i in range(pts):
    ax[0].plot(lam, R_s[i,:], color = plt.cm.Set1(color_idx[i]), label =  str(theta[i]))
    ax[1].plot(lam, R_p[i,:], color = plt.cm.Set1(color_idx[i]), label = str(theta[i]))

ax[0].set_xlabel('Wavelength [nm]')
ax[0].set_ylabel('Reflectivity')
ax[0].legend(title="AOI", loc = 'upper right')
ax[0].set_title('$s$-polarization')
ax[0].set_xlim(15,250)

ax[1].set_xlabel('Wavelength [nm]')
ax[1].set_ylabel('Reflectivity')
ax[1].legend(title="AOI",loc = 'upper right')
ax[1].set_title('$p$-polarization')
ax[1].set_xlim(15,250)
plt.show()

f, ax = plt.subplots(1,2, figsize = (16,8))
color_idx = np.linspace(0, 1, pts)
harms = arange(7,33,2)
for harm in harms:
    ax[0].axvline(1070/harm, color =  'k')
    ax[1].axvline(1070/harm, color =  'k')
for i in range(pts):
    ax[0].plot(lam, R_s[i,:], color = plt.cm.Set1(color_idx[i]), label =  str(theta[i]))
    ax[1].plot(lam, R_p[i,:], color = plt.cm.Set1(color_idx[i]), label = str(theta[i]))

ax[0].set_xlabel('Wavelength [nm]')
ax[0].set_ylabel('Reflectivity')
ax[0].legend(title="AOI", loc = 'upper right')
ax[0].set_title('$s$-polarization')
ax[0].set_xlim(15,250)

ax[1].set_xlabel('Wavelength [nm]')
ax[1].set_ylabel('Reflectivity')
ax[1].legend(title="AOI",loc = 'upper right')
ax[1].set_title('$p$-polarization')
ax[1].set_xlim(15,250)
plt.show()


f, ax = plt.subplots(1,2, figsize = (16,8))
color_idx = np.linspace(0, 1, pts)
harms = arange(7,33,2)
for harm in harms:
    ax[0].axvline(1070/harm, color =  'k')
    ax[1].axvline(1070/harm, color =  'k')

ax[0].plot(lam, R_s[plotme,:], color = plt.cm.Set1(color_idx[plotme]), label =  str(theta[plotme]))
ax[1].plot(lam, R_p[plotme,:], color = plt.cm.Set1(color_idx[plotme]), label = str(theta[plotme]))

ax[0].set_xlabel('Wavelength [nm]')
ax[0].set_ylabel('Reflectivity')
ax[0].legend(title="AOI", loc = 'upper right')
ax[0].set_title('$s$-polarization at ' + str(theta[plotme]) + ' deg')
ax[0].set_xlim(15,250)

ax[1].set_xlabel('Wavelength [nm]')
ax[1].set_ylabel('Reflectivity')
ax[1].legend(title="AOI",loc = 'upper right')
ax[1].set_title('$p$-polarization at ' + str(theta[plotme]) + ' deg')
ax[1].set_xlim(15,250)


plt.show()
