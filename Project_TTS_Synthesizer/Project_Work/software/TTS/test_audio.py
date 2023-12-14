# =============================================================================
# # -*- coding: utf-8 -*-
# """
# Created on Thu Aug  4 13:40:30 2022
# 
# @author: flare
# """
# 
# import numpy as np
# import wave
# import struct
# 
# def signal_to_wav(signal, fname, Fs):
#     """Convert a numpy array into a wav file.
# 
#      Args
#      ----
#      signal : 1-D numpy array
#          An array containing the audio signal.
#      fname : str
#          Name of the audio file where the signal will be saved.
#      Fs: int
#         Sampling rate of the signal.
# 
#     """
#     data = struct.pack('<' + ('h'*len(signal)), *signal)
#     wav_file = wave.open(fname, 'wb')
#     wav_file.setnchannels(1)
#     wav_file.setsampwidth(2)
#     wav_file.setframerate(Fs)
#     wav_file.writeframes(data)
#     wav_file.close()
#     
# signal = np.zeros(500,dtype=int)
# for i in range(67,250):
#     signal[i] = 50
# signal_to_wav(signal, "testme.wav", 50)
# =============================================================================
import numpy as np
from scipy.io.wavfile import write
import pylab

data = np.random.uniform(-1,1,4100) # 44100 random samples between -1 and 1
scaled = np.int16(data/np.max(np.abs(data)) * 32767)
write('test.wav', 4100, scaled)
pylab.plot(data)
