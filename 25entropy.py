# 25entropy.py by marle_lamountry
#co-authored with David

import math
import sys

def shannon(a, c, g, t):
	nt = (a + c + g + t)
	if nt == 0: return 0
	pa = a/nt
	pc = c/nt
	pg = g/nt
	pt = t/nt
	return -(pa*math.log2(pa) + pc*math.log2(pc) + pg*math.log2(pg) + pt*math.log2(pt))
	
print(shannon(1, 2, 3, 4))
print(shannon(21, 18, 9, 54))
print(shannon(64, 98, 12, 10))