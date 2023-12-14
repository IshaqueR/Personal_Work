# -*- coding: utf-8 -*-
"""
Created on Tue Nov 15 01:47:16 2022

@author: flare
"""
import numpy as np
import string
lexicon = np.load("CMU_lexicon.npy",allow_pickle=True)
words = np.load("CMU_words.npy",allow_pickle=True)


def transcribe(text):
    output = []
    for i in range(len(text)):
        #first check whether the word is profanity or a punctuation.
        if text[i][0] == 'XXX':
            #profanity append long silence
            output.append('XXX')
        elif text[i][0] in string.punctuation:
            #it's punctuation append short silence
            output.append('XX')
        else:
            #get the index of the word in the lexicon
            ind = np.where(words==text[i][0])
            index = ind[0][0]
            #if the index is not found then it won't work
            #set temp equal to that lexicon area and then
            #append prosody to the output and a very short silence
            temp = lexicon[index]
            for i in range(len(temp)-1):
                output.append(temp[i+1])
            output.append('X')
            
    return output

# =============================================================================
# list.index(element, start, end)
# =============================================================================
if __name__ == '__main__':
    filtered = [['HI', 'NOUN'],
                ['THERE', 'DET'],
                ['XXX', 'PROFANITY'],
                ['.', '.'],
                ["I'M", 'NOUN'],
                ['SENDING', 'VERB'],
                ['THIS', 'DET'],
                ['TEXT', 'NOUN'],
                ['TO', 'PRT'],
                ['SEE', 'VERB'],
                ['IF', 'ADP'],
                ['ANYTHING', 'NOUN'],
                ['HAS', 'VERB'],
                ['BEEN', 'VERB'],
                ['ALTERED', 'VERB'],
                ['ON', 'ADP'],
                ['THE', 'DET'],
                ['RECEIVING', 'VERB'],
                ['END', 'NOUN'],
                ['.', '.'],
                ['GOODBYE', 'NOUN'],
                ['!', '.']]

    synthesizer_input = transcribe(filtered)
