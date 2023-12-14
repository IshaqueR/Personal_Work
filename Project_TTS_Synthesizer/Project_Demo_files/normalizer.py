# -*- coding: utf-8 -*-
"""
Created on Mon Nov 14 21:17:27 2022

@author: flare
"""

def normalize_text(pos_text):
    #pos text will contain tuples where the first element in every tuple is
    #a word, and the second element is a POS. Normalizing simply capitalizes
    #all the words
    output = []
    for element in pos_text:
        temp = list(element)
        temp[0] = temp[0].upper()
        output.append(temp)
    return output

if __name__ == '__main__':
    #it works, the message it returns has a \r\n
    text = [('Hi', 'NOUN'), ('there', 'DET'), ('intercom', 'NOUN'), ('.', '.'), ("I'm", 'NOUN'), ('sending', 'VERB'), ('this', 'DET'), ('text', 'NOUN'), ('to', 'PRT'), ('see', 'VERB'), ('if', 'ADP'), ('anything', 'NOUN'), ('has', 'VERB'), ('been', 'VERB'), ('altered', 'VERB'), ('on', 'ADP'), ('the', 'DET'), ('receiving', 'VERB'), ('end', 'NOUN'), ('.', '.'), ('Goodbye', 'NOUN'), ('!', '.')]
    norm_text = normalize_text(text)