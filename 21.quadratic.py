# 21.quadratic.py by marle_lamountry

import math

def quadratic(a, b, c):
	x1 = (-b + math.sqrt(b**2 - 4 * a * c)) / 2 * a
	x2 = (-b - math.sqrt(b**2 - 4 * a * c)) / 2 * a
	assert(a > 0)
	return x1,  x2
# x1, x2 = quadratic(a, b, c)	
print(quadratic(1, 2, -3))
print(quadratic(1, 14, 48))
print(quadratic(1, -6, -27))
print(quadratic(3, -17, -6))