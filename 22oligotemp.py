# 22oligotemp.py by marle_lamountry

import math

def oligos(a, c, g, t):
	oligo = (a + c + g + t)
	if oligo <= 13:
		tm = (a + t)*2 + (g + c)*4
	elif oligo > 13:
		tm = 64.9 + 41* (g + c - 16.4)/ (a + t + g + c)
	return tm
		
print(oligos(1, 2, 3, 5))
print(oligos(33, 23, 13, 44))


