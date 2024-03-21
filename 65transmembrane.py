# 65transmembrane.py by marle lamountry

import mcb185
import sys
import dogma

def hydrophobicity(seq):
	aas = 'ACDEFGHIKLMNPQRSTVWY'
	kds = [1.8, 2.5, -3.5, -3.5, 2.8, -0.4, -3.2, 4.5, -3.9, 3.8, 1.9, -3.5, -1.6, -3.5, -4.5, -0.8, -0.7, 4.2, -0.9, -1.3]
	kds_values = []
	for aa in seq:
		if aa not in aas:
			kds_values.append(0.0)
		else:
			kds_values.append(kds[aas.index(aa)])
	return kds_values

def sums(kds_values):
	total = 0
	for kds_value in kds_values:
		total += kds_value
	return total

def transmembrane(seq):
	sp_region = seq[:30]
	t_region = seq[30:]
	test1 = False
	test2 = False
	for i in range(len(sp_region) -8 + 1):
		signalpep = sp_region[i:i+8]
		avg_kd_sp = sums(hydrophobicity(signalpep)) / 8
		if avg_kd_sp >= 2.5 and 'P' not in signalpep:
			test1 = True
			break
	for i in range(len(t_region) -11 + 1):
		transmem = t_region[i:i+11]
		avg_kd_transmem = sums(hydrophobicity(transmem)) / 11
		if avg_kd_transmem >= 2.0 and 'P' not in transmem:
			test2 = True
			break
	if test1 and test2:
		return True
	else:
		return False

for defline, seq in mcb185.read_fasta(sys.argv[1]):
	if transmembrane(seq):
		print(defline[:60])