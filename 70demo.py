# demo

import random
random.seed(1)


'''
size = 10000
#words = []
wordd = {}
for i in range(size):
	token = []
	for j in range(5):
		token.append(random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
	token =''.join(token)
	wordd[token] = True

#print(words)
	
for i in range(10000):
	if 'MARLE' in wordd:
		print('found')
'''

'''
def kdh_list(seq):
	kdsum = 0
	aas = 'IVLFCMAGTSWYPHEQDNKR' # string of amino acids
	kds = (4.5, 4.2, 3.8, 2.8, 2.5, 1.9, 1.8, -0.4, -0.7, -0.8, -0.9, -1.6, -3.2, -3.5, -3.5, 
	-3.5, -3.5, -3.9, -4.5, 0)
	for aa in seq:
		idx = aas.index(aa)
		kdsum += kds[idx]
	return kdsum/ len(seq)
'''
'''
#count windows skew problem 62skew
seq = 'ACGATGAGTGAGCTCGATGCATATGC'
w = 10

g = seq[0:w].count('G')
c = seq[0:w].count('C')

for i in range(len(seq) - w):
	off = seq[i]
	on = [i+w]
	
	if off == 'C': c -= 1
	elif off == 'G': g -= 1
	
	if on == 'C': c += 1
	elif on == 'G': g += 1
	
	comp = (c+g)/w
	if (g+c) > 0:
		skew = (g-c)/(g+c)
	else:
		skew = 0
		
	print(i, comp, skew)
'''
'''
#74 demo
import mcb185

seq = 'ATGATGGCGAATTAACCCCGATAGTAGCATAT'
#f0    M  M  A  N  *
anti = mcb185.anti_seq(seq)
seq = anti
print(anti)

for frame in range(3):
	print(frame)
	stop_used = {}
	fseq = seq[frame:]
	for i in range(0, len(fseq) -3 + 1, 3):
		codon = fseq[i:i+3]
		if codon != 'ATG':
			for j in range(i, len(fseq) -2, 3):
				codon = fseq[j:j+3]
				if codon == 'TAA' or codon == 'TAG' or codon == 'TGA':
					stop = j
					if stop not in stop_used:
						print('gene', len(anti)-i-1, len(anti)-j-3)
						stop_used[stop] = True
'''
'''
# kmer u find kmers that are there and check if thet exist, this wouldnt work w a large kmer count
# DONT DO W HIGH KMER COUNT!!!!
import itertools

seq = 'ACGTTGCATGCATGGTACTTTAC'

for k in range(1,4):
	print(k)
	kcount = {}
	for t in itertools.product('ACGT', repeat=k):
		kmer = ''.join(t)
		kcount[kmer] = 0
	print(kcount)
'''








