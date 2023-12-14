import numpy as np
import time

with open('CMU_lexicon.txt','r') as f:
	listl=[]
	for line in f:
		strip_lines=line.strip()
		listli=strip_lines.split()
		m=listl.append(listli)
	np.save("CMU_lexicon.npy",listl)


b = np.load("CMU_lexicon.npy",allow_pickle=True)

start = time.perf_counter()
print(b[0])
end = time.perf_counter()
ms = (end-start) * 10**6
print(f"Elapsed {ms:.03f} micro secs.")


start = time.perf_counter()
print(b[133000])
end = time.perf_counter()
ms = (end-start) * 10**6
print(f"Elapsed {ms:.03f} micro secs.")