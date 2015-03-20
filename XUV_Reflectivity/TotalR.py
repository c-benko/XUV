#TotalR.py
from pylab import *
from Mirrors import *

close('all')

M1 = mirror('Au', 70)
M2 = mirror('Au', 45)
M3 = mirror('SiO2', 45)

R_s = M1.R_s * M2.R_s * M3.R_s
R_p = M1.R_p * M2.R_p * M3.R_p

f, ax = plt.subplots()
ax.bar(M1.lamdas, R_s)
ax.set_xlabel('Wavelength [nm]')
ax.set_ylabel('Reflectivity')
ax.set_title('$s$-polarization')
plt.show()


f, ax = plt.subplots()
ax.bar(M1.lamdas, R_p)
ax.set_xlabel('Wavelength [nm]')
ax.set_ylabel('Reflectivity')
ax.set_title('$p$-polarization')
plt.show()
