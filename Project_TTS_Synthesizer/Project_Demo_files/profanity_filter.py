# -*- coding: utf-8 -*-
"""
Created on Mon Nov 14 21:32:54 2022

@author: flare
"""

#profanity filtering code
def profanity_filter(text):
    output = []
    profanity_list = ["INTERCOM", "APPLE"]
    for i in range(len(text)):
        if text[i][0] in profanity_list:
            text[i][0] = 'XXX'
            text[i][1] = 'PROFANITY'
        output.append(text[i])
    return output
   
if __name__ == '__main__':
    text = [['HI', 'NOUN'],
            ['THERE', 'DET'],
            ['INTERCOM', 'NOUN'],
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
    
    filtered = profanity_filter(text)
    