# Mirrors.py

from pylab import *
import pandas as pd
from scipy.interpolate import interp1d
import os

def import_index(file):
    d = pd.read_csv(file, skiprows = 1, delimiter = ',')
    nrg = d.values[:,0]
    n = d.values[:,1]
    k = d.values[:,2]
    ind = interp1d(1240/nrg, n-1j*k)

    return ind

def Rs(theta, n):
    theta *= pi/180
    return abs(np.cos(theta) - (n**2-np.sin(theta)**2)**.5) ** 2 / abs(np.cos(theta) + (n**2-np.sin(theta)**2)**.5) ** 2

def Rp(theta, n):
    theta *= pi/180
    return abs(n**2*np.cos(theta) - (n**2-np.sin(theta)**2)**.5) ** 2 / abs(2**2*np.cos(theta) + (n**2-np.sin(theta)**2)**.5) ** 2


class mirror():
    def __init__(self, type = 'Au', AOI = 45):
        self.lamdas = array([x for x in 1070/arange(9,31,2)])
        if type == 'Au':
            self.type = type
            self.file = 'Au_Constants.txt'
            self.index = import_index(self.file)
        elif type == 'SiO2':
            self.type = type
            self.file = 'SiO2_Constants.txt'
            self.index = import_index(self.file)
        else:
            self.type = type
            self.file = 'Au_Constants.txt'
            self.index = import_index(self.file, self.lamdas)

        self.AOI = AOI
        self.R_s = Rs(self.AOI, self.index(self.lamdas))
        self.R_p = Rp(self.AOI, self.index(self.lamdas))
