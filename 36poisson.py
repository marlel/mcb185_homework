# 36poisson.py by marle_lamountry
# n:n^k e^-n/k!

import math

def poisson(n, k):
	return ((n**k) * (math.e)**(-n)) / math.factorial(k)
	
print(poisson(4, 5))
