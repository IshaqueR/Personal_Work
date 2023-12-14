# -*- coding: utf-8 -*-
"""
Created on Sat Oct 22 11:24:19 2022

@author: flare
"""

"""
This code is a POS tagger using a Hidden Markov Model
Perhaps implementing the Viterbi algorithm
"""
import nltk
import numpy as np
import pandas as pd
import random
from sklearn.model_selection import train_test_split
import pprint, time

def download_data():
    nltk.download('treebank')
    nltk.download('universal_tagset')
    nltk.download('brown')
    
def get_data():
    data_bank = list(nltk.corpus.treebank.tagged_sents(tagset='universal'))
    return data_bank

# compute Emission Probability
def word_given_tag(word, tag, train_bag):
    tag_list = [pair for pair in train_bag if pair[1]==tag]
    count_tag = len(tag_list)#total number of times the passed tag occurred in train_bag
    w_given_tag_list = [pair[0] for pair in tag_list if pair[0]==word]
#now calculate the total number of times the passed word occurred as the passed tag.
    count_w_given_tag = len(w_given_tag_list)
 
    return (count_w_given_tag, count_tag)

# compute  Transition Probability
def t2_given_t1(t2, t1, train_bag):
    tags = [pair[1] for pair in train_bag]
    count_t1 = len([t for t in tags if t==t1])
    count_t2_t1 = 0
    for index in range(len(tags)-1):
        if tags[index]==t1 and tags[index+1] == t2:
            count_t2_t1 += 1
    return (count_t2_t1, count_t1)

#modified Viterbi to include rule based tagger in it
def Viterbi_rule_based(words, train_bag, tags_df, rule_based_tagger):
    state = []
    T = list(set([pair[1] for pair in train_bag]))
     
    for key, word in enumerate(words):
        #initialise list of probability column for a given observation
        p = [] 
        for tag in T:
            if key == 0:
                transition_p = tags_df.loc['.', tag]
            else:
                transition_p = tags_df.loc[state[-1], tag]
                 
            # compute emission and state probabilities
            emission_p = word_given_tag(words[key], tag, train_bag)[0]/word_given_tag(words[key], tag,train_bag)[1]
            state_probability = emission_p * transition_p
            p.append(state_probability)
             
        pmax = max(p)
        state_max = rule_based_tagger.tag([word])[0][1]       
        
         
        if(pmax==0):
            state_max = rule_based_tagger.tag([word])[0][1] # assign based on rule based tagger

        else:
            if state_max != 'X':
                # getting state for which probability is maximum
                state_max = T[p.index(pmax)]                
             
         
        state.append(state_max)
    return list(zip(words, state))

def tag_text(text):
    """
    If data hasn't been downloaded, then download it.'
    """
    downloaded = True
    if not downloaded:
        download_data()
    
    data = get_data()

# =============================================================================
#     train_set,test_set =train_test_split(data,train_size=0.80,test_size=0.20,random_state = 101)
#     print(type(train_set))
# =============================================================================
# =============================================================================
#     np.save('train_set.npy',train_set)
# =============================================================================
    train_set = np.load('train_set.npy',allow_pickle = True)
    train_tagged_words = [tup for sent in data for tup in sent]
    
# =============================================================================
#     test_tagged_words = [ tup for sent in test_set for tup in sent ]
# =============================================================================

    tags = {tag for word,tag in train_tagged_words}
    vocab = {word for word,tag in train_tagged_words}

# =============================================================================
#     tags_matrix = np.zeros((len(tags), len(tags)), dtype='float32')
#     for i, t1 in enumerate(list(tags)):
#         for j, t2 in enumerate(list(tags)): 
#             tags_matrix[i, j] = t2_given_t1(t2, t1, train_tagged_words)[0]/t2_given_t1(t2, t1, train_tagged_words)[1]
# =============================================================================
    
# =============================================================================
#     np.savetxt('tags_matrix.txt',tags_matrix,fmt="%f")
# =============================================================================
    tags_matrix = np.loadtxt("tags_matrix.txt",dtype = 'float32')
    
    tags_df = pd.DataFrame(tags_matrix, columns = list(tags), index=list(tags))
# =============================================================================
#     display(tags_df)
# =============================================================================

    patterns = [
        (r'.*ing$', 'VERB'),              # gerund
        (r'.*ed$', 'VERB'),               # past tense 
        (r'.*es$', 'VERB'),               # verb    
        (r'.*\'s$', 'NOUN'),              # possessive nouns
        (r'.*s$', 'NOUN'),                # plural nouns
        (r'\*T?\*?-[0-9]+$', 'X'),        # X
        (r'^-?[0-9]+(.[0-9]+)?$', 'NUM'), # cardinal numbers
        (r'.*', 'NOUN')                   # nouns
    ]
    rule_based_tagger = nltk.RegexpTagger(patterns)
    #pos tagging code
    start = time.perf_counter()
    output=Viterbi_rule_based(text, train_tagged_words, tags_df,rule_based_tagger)
    end = time.perf_counter()
    ms = (end-start) * 10**6
    print(f"Elapsed {ms:.03f} micro secs.")
    print(output)
    
    return output


if __name__ == '__main__':
    
    text = ['Hi', 'there', 'intercom', '.', "I'm", 'sending', 'this', 'text', 'to', 'see', 'if', 'anything', 'has', 'been', 'altered', 'on', 'the', 'receiving', 'end', '.', 'Goodbye', '!']
    
    tag_text(text)
   
#accuracy code
# =============================================================================
#     start = time.time()
#     tagged_seq = Viterbi_rule_based(test_tagged_words,train_tagged_words, tags_df)
#     end = time.time()
#     difference = end-start
#      
#     print("Time taken in seconds: ", difference)
#      
#     # accuracy
#     check = [i for i, j in zip(tagged_seq, test_run_base) if i == j] 
#      
#     accuracy = len(check)/len(tagged_seq)
#     print('Viterbi Algorithm Accuracy: ',accuracy*100)
# =============================================================================
