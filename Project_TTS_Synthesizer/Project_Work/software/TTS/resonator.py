#Date: 16/08/2022
#Author: I. Ramedies
#Digital resonator

#The code below implements a digital resonator, the basic
#building block of the synthesizer.
#Derived from Klatts paper: 1979

#imports
import numpy as np
import pylab as pl
import matplotlib.pyplot as plt
#now implementing the configuration:
#y(nT) = Ax(nT)+By(nT-T)+Cy(nT-2T)

class digital_resonator:
    def __init__(self,_A,_B,_C):
        self.A = _A
        self.B = _B
        self.C = _C
        self.buffer1 = 0
        self.buffer2 = 0
        
    def filter(self,x):
        y = self.A*x + self.buffer1*self.B + self.buffer2*self.C
        self.buffer2 = self.buffer1
        self.buffer1 = y
        return y
    
class digital_anti_resonator:
    def __init__(self,_A,_B,_C):
        self.A = _A
        self.B = _B
        self.C = _C
        self.buffer1 = 0
        self.buffer2 = 0
        
    def filter(self,x,x1,x2):
        y = self.A*x + self.buffer1*self.B + self.buffer2*self.C
        self.buffer2 = self.buffer1
        self.buffer1 = x
        return x

#test resonator
# =============================================================================
# #These parameters differ for each sound that will be generated
# #Resonant frequency is F in Hz
# #Resonance bandwidth is BW in Hz
# 
# F = 2000
# BW = 200
# 
# #The sampling frequency S changes accuracy of sound signal
# #Sampling period is T
# S = 10000
# T = 1/S
# 
# #constants
# C = -np.exp(-2*np.pi*BW*T)
# B = 2*np.exp(-np.pi*BW*T)*np.cos(2*np.pi*F*T)
# A = 1-B-C
# 
# #creating the filter
# r1 = digital_resonator(A, B, C)
# 
# x = np.zeros(300)
# x[0] = 1
# y = np.zeros(300)
# y1 = np.zeros(300)
# #resonator response
# for i in range(len(x)):
#     y[i] = r1.filter(x[i])
# 
# fourier = np.fft.fft(y)/len(y)
# fourier = fourier[range(int(len(y)/2))]
# tpCount = len(y)
# values = np.arange(int(tpCount/2))
# timePeriod = tpCount/S
# frequencies = values/timePeriod
# 
# 
# plt.plot(frequencies,10*np.log(abs(fourier)))
# plt.grid()
# plt.xlabel("Frequency (Hz)")
# plt.ylabel("Magnitude (dB)")
# =============================================================================


#test cascading
# =============================================================================
# S = 10000
# T = 1/S
# #filter 1
# F = 1000
# BW = 100
# C = -np.exp(-2*np.pi*BW*T)
# B = 2*np.exp(-np.pi*BW*T)*np.cos(2*np.pi*F*T)
# A = 1-B-C
# r1 = digital_resonator(A, B, C)
# 
# x = np.zeros(300)
# x[0] = 1
# y = np.zeros(300)
# y1 = np.zeros(300)
# y2 = np.zeros(300)
# #resonate
# for i in range(len(x)):
#     y[i] = r1.filter(x[i])
# 
# #filter 2
# F = 2000
# BW = 200
# C = -np.exp(-2*np.pi*BW*T)
# B = 2*np.exp(-np.pi*BW*T)*np.cos(2*np.pi*F*T)
# A = 1-B-C
# 
# r2 = digital_resonator(A,B,C)
# for i in range(len(y)):
#     y1[i] = r2.filter(y[i])
# 
# fourier = np.fft.fft(y1)/len(y1)
# fourier = fourier[range(int(len(y1)/2))]
# tpCount = len(y1)
# values = np.arange(int(tpCount/2))
# timePeriod = tpCount/S
# frequencies = values/timePeriod
# plt.plot(frequencies,10*np.log(abs(fourier)))
# plt.grid()
# plt.xlabel("Frequency (Hz)")
# plt.ylabel("Magnitude (dB)")
# =============================================================================


#test lowpass filter
#filter 1
# =============================================================================
# F = 0
# BW = 1000
# S = 10000
# T = 1/S
# 
# C = -np.exp(-2*np.pi*BW*T)
# B = 2*np.exp(-np.pi*BW*T)*np.cos(2*np.pi*F*T)
# A = 1-B-C
# 
# r1 = digital_resonator(A, B, C)
# 
# x = np.zeros(300)
# x[0] = 1
# y = np.zeros(300)
# y1 = np.zeros(300)
# #resonator response
# for i in range(len(x)):
#     y[i] = r1.filter(x[i])
# 
# fourier = np.fft.fft(y)/len(y)
# fourier = fourier[range(int(len(y)/2))]
# tpCount = len(y)
# values = np.arange(int(tpCount/2))
# timePeriod = tpCount/S
# frequencies = values/timePeriod
# 
# plt.plot(frequencies,10*np.log(abs(fourier)))
# plt.grid()
# plt.xlabel("Frequency (Hz)")
# plt.ylabel("Magnitude (dB)")
# =============================================================================


#test anti resonator
# =============================================================================
# S = 10000
# T = 1/S
# #filter 1
# F = 1000
# BW = 50
# C = -np.exp(-2*np.pi*BW*T)
# B = 2*np.exp(-np.pi*BW*T)*np.cos(2*np.pi*F*T)
# A = 1-B-C
# 
# Ap = 1/A
# Bp = -B/A
# Cp = -C*A
# 
# r1 = digital_anti_resonator(Ap, Bp, Cp)
# 
# x = np.zeros(300)
# x[0] = 10
# x[1] = 10
# x[2] = 10
# y = np.zeros(300)
# #resonate
# for i in range(2,len(x)-2):
#     y[i] = r1.filter(x[i],x[i-1],x[i-2])
# 
# fourier = np.fft.fft(y)/len(y)
# fourier = fourier[range(int(len(y)/2))]
# tpCount = len(y)
# values = np.arange(int(tpCount/2))
# timePeriod = tpCount/S
# frequencies = values/timePeriod
# plt.plot(frequencies,abs(fourier))
# =============================================================================


# =============================================================================
# 
# pl.plot(y1)
# =============================================================================

#frequency response
#plot omega from 0 to pi
# =============================================================================
# w = np.arange(0,np.pi,0.001)
# #convert omega to z values using the relationship
# z = np.exp(1j*w)
# 
# h = (A)/(1-(B*z**-1)-(C*z**-2))
# 
# pl.plot(np.linspace(0,5000,len(h)),np.abs(h))
# =============================================================================

