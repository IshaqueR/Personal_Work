# -*- coding: utf-8 -*-
"""
Created on Mon Oct 17 20:22:04 2022

@author: flare
"""

"""
This code cleans up the text produced by the email and prepares it for synthesis.
"""
import numpy as np
import string
import time

def tokenize(sentence):    
    """
    The tokenize function tokenizes a sentence, and returns the tokenized parts.
    """
    #this can be done easily with the .split() function.
    #the only problem with this is that it doesn't remove the punctuation as
    #it does the split on spaces, but that is fine. I can make special cases
    #for the punctuation.
    punctuation = string.punctuation
    sentence = sentence.split()
    output = []
    for word in sentence:
        #if last character is generic punctuation mark then split the word and the mark
        if word[-1] in punctuation:
            output.append(word[:-1])
            output.append(word[-1])
        else:
            output.append(word)
            
    return output
    

    
if __name__ == '__main__':
    array = []
    for i in range(5000):
        sentence = "Gmail Android connected to the Microsoft account. If you didn't grant this access, please remove the app from your account."
        start = time.perf_counter()
        #first tokenize the sentence
        sentence = tokenize(sentence)
        end = time.perf_counter()
        ms = (end-start) * 10**6
        array.append(ms)
        print(f"Elapsed {ms:.03f} micro secs.")
    
    print(sum(array)/len(array))