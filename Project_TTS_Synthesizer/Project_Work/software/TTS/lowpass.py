# -*- coding: utf-8 -*-
"""
Created on Wed Aug 31 21:50:59 2022

@author: flare
"""

import numpy as np
import pylab as pl
import matplotlib.pyplot as plt

#lowpass filter as a one-zero 6db/oct filter

inp = np.ones(50)
out = np.zeros(50)
out[0] = inp[0]

for i in range(1,50):
    out[i] = inp[i]+out[i-1]

pl.plot(10*np.log(inp))
pl.plot(10*np.log(out))
pl.plot(0,0,'bo')
pl.plot(1,6,'bo')
pl.plot(2,12,'bo')
pl.plot(4,18,'bo')
pl.plot(8,24,'bo')
pl.plot(16,30,'bo')
pl.plot(32,36,'bo')
pl.plot(64,42,'bo')