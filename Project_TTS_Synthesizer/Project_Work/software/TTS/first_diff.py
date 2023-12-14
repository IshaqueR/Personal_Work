# -*- coding: utf-8 -*-
"""
Created on Sun Nov  6 16:17:41 2022

@author: flare
"""

import numpy as np
import pylab as pl
import matplotlib.pyplot as plt

#first diff

Fs = 500
f = 5
sample = 500
x = np.arange(sample)
y = np.sin(2 * np.pi * f * x / Fs)

z = np.zeros(500)

z[0] = 0
for i in range(1, 500):
    z[i] = y[i] - y[i-1]

plt.plot(x, y)
plt.plot(x, z)
plt.xlabel('Sample(n)')
plt.ylabel('Amplitude')
plt.grid()
plt.show()
