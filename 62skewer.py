# 62skewer.py by Marle Lamountry

import sys
import mcb185

w = int(sys.argv[2])

for defline, seq in mcb185.read_fasta(sys.argv[1]):
	g = seq[:w].count('G')
	c = seq[:w].count('C')

	for i in range(len(seq) - w + 1):
		off = seq[i]
		on = [i + w - 1]
		
		if off == 'C':
			c -= 1
		elif off == 'G':
			g -= 1
		
		if on == 'C':
			c += 1
		elif on == 'G':
			g += 1
		
		comp = (c + g) / w
		if (g + c) > 0:
			skew = (g - c) / (g + c)
		else:
			skew = 0
			
		print(i, f'{comp:.3f}, {skew:.3f}')
