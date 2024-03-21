# 64profinder.py by Marle Lamountry
# Co-authored with Yutong Ji

import mcb185
import sys
import dogma

min_length = int(sys.argv[2])

def sixframe_trans(seq, min_length):
	translations = []
	for frame in range(3):
		aas = dogma.translate((seq[frame:])).split('*')
		for aa in aas:
			if 'M' in aas:
				protein = aa[aa.find('M'):]
				if len(protein) >= min_length:
					translations.append(protein)
	return translations

for defline, seq in mcb185.read_fasta(sys.argv[1]):
	strand = sixframe_trans(seq, min_length)
	rev_strand = sixframe_trans(dogma.revcomp(seq), min_length)
	for protein in rev_strand:
		strand.append(protein)
	for i, protein in enumerate(strand):
		print(f'>{defline[:11]}-protein-{i + 1}')
		print(f'{protein}*')