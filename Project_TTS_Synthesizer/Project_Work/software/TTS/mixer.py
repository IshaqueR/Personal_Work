# -*- coding: utf-8 -*-
"""
Created on Wed Aug 31 02:31:03 2022

@author: flare
"""
import numpy as np
import pylab as pl

#mixer
#the mixer is just the summing component in the synthesizer indicated with a + sign.
#so it simply adds signals and generates a single output.

length = 50
#signal 1: 
inp1 = np.ones(length)
inp1[20] = 5
#signal 2:
inp2 = np.ones(length)
inp2[25] = 3
#if these two are added, I'm expecting a 2 signal
output = np.zeros(length)
output[:]=inp1[:]+inp2[:]


pl.plot(inp1)
pl.plot(inp2)
pl.plot(output)