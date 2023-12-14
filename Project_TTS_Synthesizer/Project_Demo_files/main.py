import numpy as np
import mail_client_ver3 as email
import tokenizer as token
import HMM_POS_tagger as hmm
import normalizer as norm
import profanity_filter as prof
import phonetic_transcription as pt
import prosody_gen as pg
import time

#program begins
print("BEGINNING PROGRAM\r\n")

#first subsystem: email client
print("Receiving email\r\n")
text = email.getMessage()

# =============================================================================
# print("Email: ",text)
# =============================================================================
start = time.time()


#second subsystem: NLP and linguistics analysis
#first tokenize the text
tokenized_text = token.tokenize(text)

print("Tokenized: ",tokenized_text)
print("\r\n")

#second tag the text with POS
tagged_text = hmm.tag_text(tokenized_text)

print("POS tagged: ",tagged_text)
print("\r\n")

#third normalize the text
norm_text = norm.normalize_text(tagged_text)

print("Normalized: ",norm_text)
print("\r\n")

#next profanity filter the text
filt_text = prof.profanity_filter(norm_text)

print("Profanity filtered: ",filt_text)
print("\r\n")

#now check the lexicon for phonetic transcription
phonemes = pt.transcribe(filt_text)

print("Transcription: ",phonemes)
print("\r\n")

end = time.time()
difference = end-start
  
print("Execution Time in seconds: ", difference)
#finally speech generation and audio output
pg.makeWord(phonemes,plot=True)

