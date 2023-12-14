# -*- coding: utf-8 -*-
"""
Created on Wed Aug 31 02:08:26 2022

@author: flare
"""
import numpy as np
import pylab as pl
import matplotlib.pyplot as plt
#assume sample rate is 10000 and fundamental frequency is 100Hz
SR = 10000
F0 = 100
SAMPLES = 500
glottal_period = SR/F0
signal = np.zeros(SAMPLES)

#tracks where the last pulse was generated at
pulse_index = 0
for i in range(SAMPLES):
    if i - pulse_index >= glottal_period:
        signal[i] = 1
        pulse_index = i
        
# =============================================================================
# pl.plot(signal)
# =============================================================================
plt.plot(signal)
plt.grid()
plt.xlabel("Samples")
plt.ylabel("Magnitude")