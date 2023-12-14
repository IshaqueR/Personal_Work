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
def Viterbi_rule_based(words, train_bag, tags_df):
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
            emission_p = word_given_tag(words[key], tag, train_tagged_words)[0]/word_given_tag(words[key], tag,train_tagged_words)[1]
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

if __name__ == '__main__':
    
    """
    If data hasn't been downloaded, then download it.'
    """
    downloaded = True
    if not downloaded:
        download_data()
    
    data = get_data()

    train_set,test_set =train_test_split(data,train_size=0.90,test_size=0.10,random_state = 101)

    train_tagged_words = [tup for sent in data for tup in sent]

    test_tagged_words = [ tup for sent in test_set for tup in sent ]

    tags = {tag for word,tag in train_tagged_words}
    vocab = {word for word,tag in train_tagged_words}

    tags_matrix = np.zeros((len(tags), len(tags)), dtype='float32')
    for i, t1 in enumerate(list(tags)):
        for j, t2 in enumerate(list(tags)): 
            tags_matrix[i, j] = t2_given_t1(t2, t1, train_tagged_words)[0]/t2_given_t1(t2, t1, train_tagged_words)[1]
     
    tags_df = pd.DataFrame(tags_matrix, columns = list(tags), index=list(tags))
    display(tags_df)
      
    random.seed(1234)

    rndom = [random.randint(1,len(test_set)) for x in range(10)]
     
    test_run = [test_set[i] for i in rndom]
     
    test_run_base = [tup for sent in test_run for tup in sent]

    test_tagged_words = [tup[0] for sent in test_run for tup in sent]
    

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
   
#accuracy code
# =============================================================================
#     rule_based_tagger = nltk.RegexpTagger(patterns)
# 
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

#pos tagging code
# =============================================================================
#     #Check how a sentence is tagged by the two POS taggers
#     #and compare them
#     test_sent="He lookee a little bit garbo today."
#     start = time.perf_counter()
#     pred_tags_rule=Viterbi_rule_based(test_sent.split(), train_tagged_words, tags_df)
#     end = time.perf_counter()
#     ms = (end-start) * 10**6
#     print(f"Elapsed {ms:.03f} micro secs.")
#     print(pred_tags_rule)
# =============================================================================

#profanity filtering code   
# =============================================================================
#     #profanity filtering
#     print(test_sent)
#     profanity_list = ["garbo", "fuzzy", "lookee", "ayaya"]
#     start = time.perf_counter()
#     for i in range(len(pred_tags_rule)):
#         if pred_tags_rule[i][0] in profanity_list:
#             pred_tags_rule[i] = tuple(['XXX','PROFANITY'])
#     end = time.perf_counter()
#     ms = (end-start) * 10**6
#     print(f"Elapsed {ms:.03f} micro secs.")
#     print(pred_tags_rule)
# =============================================================================
    
