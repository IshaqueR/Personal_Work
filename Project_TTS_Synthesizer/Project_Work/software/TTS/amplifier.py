# -*- coding: utf-8 -*-
"""
Created on Wed Aug 31 15:27:31 2022

@author: flare
"""

import numpy as np
import pylab as pl

#amplifier
#specify amplification in dB
db = 10

input = np.ones(50)*5
output = np.zeros(50)

#amplifier does a conversion to signal value
db = np.sqrt(10)**(db/10)

output[:] = input[:]*db

pl.plot(10*np.log(input))
pl.plot(10*np.log(output))
