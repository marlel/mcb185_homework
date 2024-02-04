# 33triples.py by marle_lamountry

import math

for i in range(1, 100):
	for j in range(i+1, 100):
		c = math.sqrt(i**2 + j**2)
		if c % 1 == 0 and c < (i+j):
			print(i, j, int(c))




		