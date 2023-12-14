# -*- coding: utf-8 -*-
"""
Created on Sat Sep 10 20:42:09 2022

@author: flare
"""
import numpy as np
import synthesizer
import simpleaudio as sa
import pylab as pl
import matplotlib.pyplot as plt

"""
This code uses the Klatt synthesizer to generate a word from a list of phonemes

The available phonemes are:
vowels: AA, AE, AH, AO, AW, AY, EH, ER, EY, IH, IY, OW, OY, UH, UW
plosives: B, D, G, P
affricates: CH, JH
voiced fricates: DH, SH, V
unvoiced fricates: F, S, TH
sonor: L, R, W
nasal: M, N, NG

For profanity, the code will simply generate an empty audio wave form.
Profanity will be indicated with XX per phoneme.
"""

def makeSound(duration, F0beg, F0end, f1beg=0, f1end=0,\
              f2beg=0, f2end=0, f3beg=0, f3end=0, bw1beg=0,\
              bw2beg=0, bw3beg=0,\
              Abeg=60, Amid=60, Aend=60, A2=0, A3=0, A4=0,\
              A5=0, A6=0, bypass=0,fnp=None,fnz=None,SND=None):
    """
    Generic function to make a sound based on parameters. First fetch all specs
    """
    #create synthesizer with sound of duration
    s = synthesizer.create_synth(synthesizer.Spec(DUR=duration))
    #fetch samples
    N = s.specs["NUMSAMPLES"]
    #fundamental frequency, formant frequency
    F0 = s.specs["F0"]
    FF = np.asarray(s.specs["FF"]).T
    BW = np.asarray(s.specs["BW"]).T
    #amplitude of voicing as aspiration amplitude
    AV = s.specs["AV"]
    AH = s.specs['AH']
    #amplitude of quasi-sinusoidal voicing and frictation
    AVS = s.specs["AVS"]
    AF = s.specs["AF"]
    AB = s.specs["AB"]
    #formant amplitudes
    Amp2 = s.specs["A2"]
    Amp3 = s.specs["A3"]
    Amp4 = s.specs["A4"]
    Amp5 = s.specs["A5"]
    Amp6 = s.specs["A6"]
    #nasal resonator frequencies
    FNP = s.specs["FNP"]
    FNZ = s.specs["FNZ"]
    #amplitude of frication 
    AF = s.specs["AF"]
    #switch for fricative excitation
    SW = s.specs["SW"]
    
    """
    Check what kind of sound is being made, vowel, consonant(sonor, voiceless or
    voiced fricative, affricate, plosive, nasal)
    Though always edit the formants, bandwidths, and fundamental frequency
    """
    #formants
    formantbeg = np.r_[f1beg, f2beg, f3beg]
    formantend = np.r_[f1end, f2end, f3end]
    grad = np.linspace(1, 0, N)
    FF[:,:3] = np.outer(grad, formantbeg) + np.outer((1 - grad), formantend)
    s.specs["FF"] = FF.T
    #bandwidths
    bandbeg = np.r_[bw1beg, bw2beg, bw3beg]
    bandend = np.r_[bw1beg, bw2beg, bw3beg]
    BW[:,:3] = np.outer(grad, bandbeg) + np.outer((1 - grad), bandend)
    s.specs["BW"] = BW.T
    # fundamental frequency
    F0[:] = np.linspace(F0beg, F0end, N)
    if SND == "VOW":
        """
        For vowels, only edit the amplitude of voicing
        """
        AV[:int(N/2)] = np.linspace(1**0.1*Abeg, 1**0.1*Amid, int(N/2))
        AV[int(N/2):] = np.linspace(1**0.1*Amid, 1**0.1*Aend, int(N/2))
        
    elif SND == "SON":
        """
        For sonorants, they are modelled the same as vowels except, they should
        be 10dB lower than the vowel after it.
        """
        #note here to check what happens when making it a cascade configuration
        AV[:int(N/2)] = np.linspace(1**0.1*(Abeg-10), 1**0.1*(Amid-10), int(N/2))
        AV[int(N/2):] = np.linspace(1**0.1*(Amid-10), 1**0.1*(Aend-10), int(N/2))
        
    elif SND == "UVF":
        """
        Voiceless fricatives have the following specs for amplitudes AF=60, AV=0, AVS=0
        """
        AF[:] = np.linspace(1,0,N)**0.1*60
        AV[:] = np.linspace(1,0,N)**0.1*0
        AVS[:] = np.linspace(1,0,N)**0.1*0
        
    elif SND == "VF":
        """
        Voiced fricatives have the following specs for amplitudes AF=50, AV=47, AVS=47
        """
        AF[:] = np.linspace(1,0,N)**0.1*50
        AV[:] = np.linspace(1,0,N)**0.1*47
        AVS[:] = np.linspace(1,0,N)**0.1*47

    elif SND == "NAS":
        """
        Nasal consonants are obtained by providing a nasal freqeuncy, in the
        pole and zero resonators.
        """
        FNP[:] = np.linspace(fnp,fnp,N)
        FNZ[:] = np.linspace(fnz,fnz,N)
    
    elif SND == "H":
        """
        For the HH sonorant, the first formant frequency is set to 300Hz, and
        the voicing is replaced with aspiration
        """
        AV[:] = np.linspace(1,0,N)**0.1*0
        AH[:int(N/2)] = np.linspace(1**0.1*(Abeg-10), 1**0.1*(Amid-10), int(N/2))
        AH[int(N/2):] = np.linspace(1**0.1*(Amid-10), 1**0.1*(Aend-10), int(N/2))
    
    if SND == "UVF" or SND == "VF" or SND == "AFF" or SND == "PLO" or SND == "NAS":
        """
        For these consonants, the formant amplitudes are important
        """
        SW = 1
        AB[:] = np.linspace(1,1,N) ** 0.1 * bypass
        Amp2[:] = np.linspace(1,1,N) ** 0.1 * A2
        Amp3[:] = np.linspace(1,1,N) ** 0.1 * A3
        Amp4[:] = np.linspace(1,1,N) ** 0.1 * A4
        Amp5[:] = np.linspace(1,1,N) ** 0.1 * A5
        Amp6[:] = np.linspace(1,1,N) ** 0.1 * A6
    """
    Run the synthesizer to create the output, and scale to audio
    """
    s.run()
    if SND =="VOW":
        sound = s.to_audio()
    elif SND != 'SIL':
        sound = s.to_audio2()
    else:
        sound = s.to_audio3()
    """
    Perform clipping on the audio file if it requires any, *edit
    """
    sound = sound[100:]
    sound = sound[:-300]
    return sound
    
def makeWord(word,plot=False):
    """
    This function goes through every phoneme in the word, generates a sound for
    it depending on it's position in the word, and then combines each phoneme
    to make a single audio output word. The user may also plot the output
    waveform if desired.
    """
    output = []
    for phoneme in word:
        if phoneme == 'AA':#o in odd
            sound = makeSound(duration=0.2,F0beg=130,F0end=109,f1beg=625,f1end=610,\
                              f2beg=920,f2end=1100,f3beg=2499,f3end=2666,\
                              bw1beg=130,bw2beg=248,bw3beg=451,\
                              Abeg=40,Amid=60,Aend=40,SND="VOW")
            sound
            output.append(sound)
        elif phoneme == 'AE':#a in at
            sound = makeSound(duration=0.15,F0beg=122,F0end=103,f1beg=770,f1end=640,\
                              f2beg=1861,f2end=1788,f3beg=2513,f3end=2691,\
                              bw1beg=138,bw2beg=144,bw3beg=78,Abeg=60,Aend=60,SND="VOW")
            output.append(sound)
        elif phoneme == 'AH':#u in hut
            sound = makeSound(duration=0.2,F0beg=140,F0end=108,f1beg=718,f1end=644,\
                              f2beg=1234,f2end=1308,f3beg=2488,f3end=2636,\
                              bw1beg=146,bw2beg=265,bw3beg=248,Abeg=40,Aend=50,SND="VOW")
            output.append(sound)    
        elif phoneme == 'AO':#ough in ought
            sound = makeSound(duration=0.2,F0beg=120,F0end=112,f1beg=460,f1end=490,\
                              f2beg=644,f2end=773,f3beg=2710,f3end=2710,\
                              bw1beg=149,bw2beg=30,bw3beg=661,Abeg=59,Aend=58,SND="VOW")
            output.append(sound)
        elif phoneme == 'AW':#ow in cow
            sound = makeSound(duration=0.2,F0beg=131,F0end=107,f1beg=773,f1end=590,\
                              f2beg=1200,f2end=1013,f3beg=2150,f3end=2710,\
                              bw1beg=219,bw2beg=204,bw3beg=256,Abeg=58,Aend=58,SND="VOW")
            output.append(sound)
        elif phoneme == 'AY':#i in hide
            sound = makeSound(duration=0.2,F0beg=140,F0end=106,f1beg=737,f1end=460,\
                              f2beg=866,f2end=1900,f3beg=2322,f3end=2600,\
                              bw1beg=121,bw2beg=435,bw3beg=435,Abeg=60,Aend=60,SND="VOW")
            output.append(sound)
        elif phoneme == 'B':#b in bee (plosive)
            sound = makeSound(duration=0.07,F0beg=140,F0end=103,f1beg=200,f1end=200,\
                              f2beg=1100,f2end=1100,f3beg=2150,f3end=2150,\
                              bw1beg=60,bw2beg=110,bw3beg=130,Abeg=60,Aend=60,\
                              A2=0,A3=0,A4=0,A5=0,A6=0,bypass=63,SND="PLO")
            output.append(sound)
        elif phoneme == 'CH':#ch in cheese (affricate)
            sound = makeSound(duration=0.1,F0beg=140,F0end=103,f1beg=350,f1end=350,\
                              f2beg=1800,f2end=1800,f3beg=2820,f3end=2820,\
                              bw1beg=200,bw2beg=90,bw3beg=300,Abeg=60,Aend=60,\
                              A2=0,A3=44,A4=60,A5=53,A6=53,bypass=0,SND="AFF")
            output.append(sound)
        elif phoneme == 'D':#d in deez nuts (plosive)
            sound = makeSound(duration=0.06,F0beg=140,F0end=103,f1beg=200,f1end=200,\
                              f2beg=1600,f2end=1600,f3beg=2600,f3end=2600,\
                              bw1beg=60,bw2beg=100,bw3beg=170,Abeg=60,Aend=60,\
                              A2=0,A3=47,A4=60,A5=62,A6=60,bypass=0,SND="PLO")
            output.append(sound)
        elif phoneme == 'DH':#dh in these nuts (voiced fricative)
            sound = makeSound(duration=0.1,F0beg=122,F0end=103,f1beg=270,f1end=270,\
                              f2beg=1290,f2end=1290,f3beg=2540,f3end=2540,\
                              bw1beg=60,bw2beg=80,bw3beg=170,Abeg=30,Aend=30,\
                              A2=0,A3=0,A4=0,A5=0,A6=28,bypass=48,SND="VF")
            output.append(sound)
        elif phoneme == 'EH':#eh in ed
            sound = makeSound(duration=0.15,F0beg=126,F0end=111,f1beg=550,f1end=387,\
                              f2beg=2673,f2end=1972,f3beg=2986,f3end=2673,\
                              bw1beg=48,bw2beg=428,bw3beg=271,Abeg=60,Aend=60,SND="VOW")
            output.append(sound)
        elif phoneme == 'ER':#er in hurt
            sound = makeSound(duration=0.3,F0beg=117,F0end=117,f1beg=552,f1end=350,\
                              f2beg=1474,f2end=1548,f3beg=2654,f3end=2654,\
                              bw1beg=66,bw2beg=67,bw3beg=84,Abeg=60,Aend=50,SND="VOW")
            output.append(sound)
        elif phoneme == 'EY':#ey in ate
            sound = makeSound(duration=0.2,F0beg=150,F0end=126,f1beg=600,f1end=350,\
                              f2beg=2000,f2end=2270,f3beg=2670,f3end=3000,\
                              bw1beg=121,bw2beg=556,bw3beg=599,Abeg=60,Aend=50,SND="VOW")
            output.append(sound)
        elif phoneme == 'F':#f in fee (unvoiced fricate)
            sound = makeSound(duration=0.2,F0beg=122,F0end=103,f1beg=340,f1end=340,\
                              f2beg=1100,f2end=1100,f3beg=2080,f3end=2080,\
                              bw1beg=200,bw2beg=120,bw3beg=150,Abeg=10,Aend=10,\
                              A2=0,A3=0,A4=0,A5=0,A6=28,bypass=57,SND="UVF")
            output.append(sound)
        elif phoneme == 'G':#g in green (plosive)
            sound = makeSound(duration=0.05,F0beg=142,F0end=103,f1beg=200,f1end=200,\
                              f2beg=1990,f2end=1990,f3beg=2850,f3end=2850,\
                              bw1beg=60,bw2beg=150,bw3beg=280,Abeg=0,Aend=0,\
                              A2=0,A3=53,A4=43,A5=45,A6=45,bypass=0,SND ="PLO")
            output.append(sound)
        elif phoneme == 'HH':#hh in he (sonorant, special)
            #if next is AE
            sound = makeSound(duration=0.08,F0beg=142,F0end=103,f1beg=300,f1end=300,\
                              f2beg=1861,f2end=1788,f3beg=2513,f3end=2691,\
                              bw1beg=138,bw2beg=144,bw3beg=78,Abeg=60,Aend=60,\
                              A2=0,A3=0,A4=0,A5=0,A6=0,bypass=0,SND ="H")
            output.append(sound)
        elif phoneme == 'IH':#ih in ping / it / is
            sound = makeSound(duration=0.15,F0beg=130,F0end=122,f1beg=440,f1end=300,\
                              f2beg=2110,f2end=2220,f3beg=2750,f3end=2750,\
                              bw1beg=26,bw2beg=377,bw3beg=346,Abeg=60,Aend=40,SND="VOW")
            output.append(sound)
        elif phoneme == 'IY':#iy in eat
            sound = makeSound(duration=0.2,F0beg=122,F0end=107,f1beg=310,f1end=290,\
                              f2beg=2020,f2end=2070,f3beg=2960,f3end=2960,\
                              bw1beg=45,bw2beg=200,bw3beg=400,Abeg=50,Aend=10,SND="VOW")
            output.append(sound)
        elif phoneme == 'JH':#jh in gee (affricate)
            sound = makeSound(duration=0.1,F0beg=120,F0end=120,f1beg=260,f1end=260,\
                              f2beg=1800,f2end=1800,f3beg=2820,f3end=2820,\
                              bw1beg=60,bw2beg=80,bw3beg=270,Abeg=20,Aend=20,\
                              A2=0,A3=44,A4=60,A5=53,A6=53,bypass=0,SND="AFF")
            output.append(sound)
        elif phoneme == 'K':#k in key (plosive)
            sound = makeSound(duration=0.05,F0beg=120,F0end=120,f1beg=300,f1end=300,\
                              f2beg=1990,f2end=1990,f3beg=2850,f3end=2850,\
                              bw1beg=250,bw2beg=160,bw3beg=330,Abeg=0,Aend=0,\
                              A2=0,A3=53,A4=43,A5=45,A6=45,bypass=0,SND="PLO")
            output.append(sound)
        elif phoneme == 'L':#l in lee (sonor) rip :(
            sound = makeSound(duration=0.15,F0beg=122,F0end=103,f1beg=310,f1end=310,\
                              f2beg=1050,f2end=1050,f3beg=2880,f3end=2880,\
                              bw1beg=50,bw2beg=100,bw3beg=280,Abeg=60,Aend=60,SND="SON")
            output.append(sound)
        elif phoneme == 'M':#m in mister, should i call you mister? (nasal)
            sound = makeSound(duration=0.1,F0beg=120,F0end=120,f1beg=480,f1end=480,\
                              f2beg=1270,f2end=1270,f3beg=2130,f3end=2130,\
                              bw1beg=40,bw2beg=200,bw3beg=200,Abeg=60,Aend=60,\
                              A2=0,A3=0,A4=0,A5=0,A6=0,bypass=0,\
                              fnp=270,fnz=450,SND="NAS")
            output.append(sound)
        elif phoneme == 'N':#n in knee (nasal)
            sound = makeSound(duration=0.1,F0beg=120,F0end=120,f1beg=480,f1end=480,\
                              f2beg=1340,f2end=1340,f3beg=2470,f3end=2470,\
                              bw1beg=40,bw2beg=300,bw3beg=300,Abeg=60,Aend=60,\
                              A2=0,A3=0,A4=0,A5=0,A6=0,bypass=0,\
                              fnp=270,fnz=450,SND="NAS")
            output.append(sound)
        elif phoneme == 'NG':#ng in wing/ring/ping (made it a nasal, because it sounds like N)
            sound = makeSound(duration=0.1,F0beg=107,F0end=103,f1beg=515,f1end=275,\
                              f2beg=1456,f2end=1456,f3beg=2300,f3end=1880,\
                              bw1beg=77,bw2beg=322,bw3beg=608,Abeg=20,Aend=20,\
                              fnp=270,fnz=450,SND="NAS")
            output.append(sound)
        elif phoneme == 'OW':#ow in oat
            sound = makeSound(duration=0.2,F0beg=122,F0end=103,f1beg=660,f1end=450,\
                              f2beg=1220,f2end=1330,f3beg=2575,f3end=2750,\
                              bw1beg=120,bw2beg=66,bw3beg=93,Abeg=60,Aend=40,SND="VOW")
            output.append(sound)
        elif phoneme == 'OY':#oy in toy, boy
            sound = makeSound(duration=0.24,F0beg=122,F0end=103,f1beg=535,f1end=410,\
                              f2beg=900,f2end=1900,f3beg=2513,f3end=2513,\
                              bw1beg=105,bw2beg=105,bw3beg=260,Abeg=60,Aend=20,SND="VOW")
            output.append(sound)
        elif phoneme == 'P':#p in pee
            sound = makeSound(duration=0.07,F0beg=109,F0end=103,f1beg=400,f1end=400,\
                              f2beg=1100,f2end=1100,f3beg=2150,f3end=2150,\
                              bw1beg=300,bw2beg=150,bw3beg=220,Abeg=60,Aend=60,\
                              A2=0,A3=0,A4=0,A5=0,A6=0,bypass=63,SND="PLO")
            output.append(sound)
        elif phoneme == 'R':#r in read (sonorant) should be 10 db less than next vowel
            sound = makeSound(duration=0.15,F0beg=122,F0end=122,f1beg=310,f1end=310,\
                              f2beg=1060,f2end=1060,f3beg=1380,f3end=1380,\
                              bw1beg=70,bw2beg=100,bw3beg=120,Abeg=60,Amid=60,\
                              Aend=60,SND="SON")
            output.append(sound)
        elif phoneme == 'S':#s in sea (unvoiced fricative)
            sound = makeSound(duration=0.2,F0beg=122,F0end=122,f1beg=320,f1end=320,\
                              f2beg=1390,f2end=1390,f3beg=2530,f3end=2530,\
                              bw1beg=200,bw2beg=80,bw3beg=200,Abeg=0,Aend=0,\
                              A2=0,A3=0,A4=0,A5=0,A6=52,bypass=0,SND="UVF")
            output.append(sound)
        elif phoneme == 'SH':#sh in she (voiced fricative)
            sound = makeSound(duration=0.2,F0beg=122,F0end=122,f1beg=300,f1end=300,\
                              f2beg=1840,f2end=1840,f3beg=2750,f3end=2750,\
                              bw1beg=200,bw2beg=100,bw3beg=300,Abeg=10,Aend=10,\
                              A2=0,A3=57,A4=48,A5=48,A6=46,bypass=0,SND="VF")
            output.append(sound)
        elif phoneme == 'T':#t in tea (plosive)
            sound = makeSound(duration=0.08,F0beg=120,F0end=120,f1beg=400,f1end=400,\
                              f2beg=1600,f2end=1600,f3beg=2600,f3end=2600,\
                              bw1beg=300,bw2beg=120,bw3beg=250,Abeg=60,Aend=60,\
                              A2=0,A3=30,A4=45,A5=57,A6=63,bypass=0,SND="PLO")
            output.append(sound)
        elif phoneme == 'TH':#th in theta/ think/ thin (unvoiced fricative)
            sound = makeSound(duration=0.2,F0beg=122,F0end=103,f1beg=320,f1end=320,\
                              f2beg=1290,f2end=1290,f3beg=2540,f3end=2540,\
                              bw1beg=200,bw2beg=90,bw3beg=200,Abeg=0,Aend=0,\
                              A2=0,A3=0,A4=0,A5=0,A6=28,bypass=48,SND="UVF")
            output.append(sound)
        elif phoneme == 'UH':#uh in hood (short)
            sound = makeSound(duration=0.2,F0beg=122,F0end=103,f1beg=450,f1end=375,\
                              f2beg=1200,f2end=850,f3beg=2200,f3end=2200,\
                              bw1beg=65,bw2beg=110,bw3beg=140,Abeg=55,Amid=55,Aend=50,SND="VOW")
            output.append(sound)
        elif phoneme == 'UW':#uw in two (long)
            sound = makeSound(duration=0.2,F0beg=122,F0end=105,f1beg=420,f1end=310,\
                              f2beg=1680,f2end=1270,f3beg=3185,f3end=3185,\
                              bw1beg=52,bw2beg=133,bw3beg=547,Abeg=60,Aend=45,SND="VOW")
            output.append(sound)
        elif phoneme == 'V':#v in vee (voiced fricative)
            sound = makeSound(duration=0.2,F0beg=122,F0end=103,f1beg=220,f1end=220,\
                              f2beg=1100,f2end=1100,f3beg=2080,f3end=2080,\
                              bw1beg=60,bw2beg=90,bw3beg=120,Abeg=30,Aend=30,\
                              A2=0,A3=0,A4=0,A5=0,A6=0,bypass=57,SND="VF")
            output.append(sound)
        elif phoneme == 'W':#w in wee (sonor)
            sound = makeSound(duration=0.07,F0beg=150,F0end=120,f1beg=360,f1end=360,\
                              f2beg=1141,f2end=1540,f3beg=2450,f3end=2450,\
                              bw1beg=24,bw2beg=140,bw3beg=1050,Abeg=42,Aend=60,SND="SON")
            output.append(sound)
        elif phoneme == 'Y':#y in yield, yes, yebo (sonor)
            sound = makeSound(duration=0.12,F0beg=120,F0end=120,f1beg=260,f1end=260,\
                              f2beg=2070,f2end=2070,f3beg=3020,f3end=3020,\
                              bw1beg=40,bw2beg=250,bw3beg=500,Abeg=60,Amid=60,Aend=50,SND="SON")
            output.append(sound)
        elif phoneme == 'Z':#z in zee, zed, zebra, zest (voiced fricative)
            sound = makeSound(duration=0.15,F0beg=122,F0end=103,f1beg=240,f1end=240,\
                              f2beg=1390,f2end=1390,f3beg=2530,f3end=2530,\
                              bw1beg=70,bw2beg=60,bw3beg=180,Abeg=55,Aend=48,\
                              A2=0,A3=0,A4=0,A5=0,A6=52,bypass=0,SND="VF")
            output.append(sound)
        elif phoneme == 'ZH':#zh in treasure (fricative)
            sound = makeSound(duration=0.15,F0beg=122,F0end=103,f1beg=220,f1end=220,\
                              f2beg=1940,f2end=1940,f3beg=2750,f3end=2750,\
                              bw1beg=70,bw2beg=80,bw3beg=280,Abeg=60,Aend=20,\
                              A2=0,A3=57,A4=48,A5=48,A6=46,bypass=0,SND="VF")
            output.append(sound)
        elif phoneme == 'X':#short silence for word break 0.2 sec
# =============================================================================
#             sound = np.zeros(3200)
# =============================================================================
            sound = makeSound(duration=0.2,F0beg=120,F0end=120,\
                              Abeg=0,Amid=0,Aend=0,\
                              SND="SIL")
            output.append(sound)
        elif phoneme == 'XX':#short silence for punctuation 0.5 sec
            #append silence here
            sound = makeSound(duration=0.5,F0beg=120,F0end=120,\
                              Abeg=0,Amid=0,Aend=0,\
                              SND="SIL")
            output.append(sound)
        elif phoneme == 'XXX':#long silence for profanity 1 sec
            #add silence for word break
            sound = makeSound(duration=1,F0beg=120,F0end=120,\
                              Abeg=0,Amid=0,Aend=0,\
                              SND="SIL")
            output.append(sound)
            
            
    """
    Now generate the output audio
    """
    audio = np.hstack((output))
    
    """
    If user wants to plot and hear individual words, plot must be True.
    """
    if plot:
        pl.plot(audio)
# =============================================================================
#         fourier = np.fft.fft(audio)/len(audio)
#         fourier = fourier[range(int(len(audio)/2))]
#         tpCount = len(audio)
#         values = np.arange(int(tpCount/2))
#         timePeriod = tpCount/10000
#         frequencies = values/timePeriod
#         plt.plot(frequencies,abs(fourier))
# =============================================================================

        play_obj = sa.play_buffer(audio, num_channels=1, bytes_per_sample=2, sample_rate=16_000)
        play_obj.wait_done()
# =============================================================================
#         write("synthesized output", 16_000, audio)
# =============================================================================
    return audio

def makeSentence(words):
    """
    Generic function to make a sentence given a list of words
    """
    output = []
    for word in words:
        output.append(makeWord(word))
        
    for i in range(len(output)): 
        sa.play_buffer(output[0], num_channels=1, bytes_per_sample=2, sample_rate=16_000)
    return output

if __name__ == '__main__':
    #word odd
    word = ['X','IY']
    #to do, finish the HH sound
    makeWord(word,plot=True)