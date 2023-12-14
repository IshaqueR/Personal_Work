#tokenisation model
Input = sentence
Output = tokens

for char in sentence:
    if char == " ":
        split the word

for char in word:
    if char == punctuation mark:
        split the word
        
#profanity filtering
Input = tokens
Output = filtered_tokens

for token in tokens:
    if token in profanity dictionary:
        mark token as profanity
        
#POS tagger
Input = tokens
Output = POS of tokens

#first download corpus if not downloaded
train data = get sentences from corpus bank
tags = get number of unique tags in train words
words = get number of unique words in train words

t = number of tags
#calculate the transition probabilities
transition matrix = create (t x t) matrix

#for unknown tags rules may be specified
rules = #create rules list, eg. if ending in 'ed', POS = 'VERB'

#calculate the most probable tags
predicted_tags = Viterbi(tokens, train data, transition matrix)

#Viterbi function
function Viterbi:
 for word in words:
    v = #probability list for current word (viterbi values)
    for tag in train data:
        #make special case for first tag
        current transition = transition matrix[last state, tag]
        
        emission = #compute emission probability
        state = #compute state probability
        v list = #append state to list
    
    #get max viterbi value from list
    value = max(v)
    
    #if the max v value is a probability of 0, then apply the rule set
    if value = 0:
        POS = #accroding to rule set
    #otherwise just assign the POS relating to the highest state
    else:
        POS = #highest state probability
        
    POS list = #append to a POS list
    
 return POS list

#Phonetic transcription
Input: POS tagged words
Output: Phonetic representation and lexical stress (optional)
#lexicon text file is initially written to .npy file
lexicon = np.load('file')
#first index of every element in lexicon can be compared with the token

#return all instances of the word
for element in lexicon:
    possible words = #search lexicon index 0 and append if it matches token
    
for word in possible words:
    #check the second index of word to match POS
    if POS matches word POS:
        phonemes = remaining indices of word
        stress = third index of word
        
return phonemes,stress

