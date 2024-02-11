# 41zscores.py by marle_lamountry

#program that generates numbers from a normal distrib
#calculate how many #s are 1,2,3 z-scores above

import random

z1 = 0
z2 = 0
z3 = 0
limit = 100000
for i in range(limit):
	r = random.gauss(0.0, 1.0)
	if r > 1: z1 += 1
	if r > 2: z2 += 1
	if r > 3: z3 += 1
print(1 - 2*z1/limit)
print(1 - 2*z2/limit)
print(1 - 2*z3/limit)