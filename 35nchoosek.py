# 35nchoosek.py by marle_lamountry

import math

def factorial(n):
	if n == 0: return 1
	fac = 1
	for i in range(1, n + 1):
		fac = fac * i
	return fac

def nchoosek(n, k):
	return factorial(n) // factorial(n - k) // factorial(k)


print(nchoosek(12, 3))
print(nchoosek(12, 4))