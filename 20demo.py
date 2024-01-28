# 20demo.py by marle_lamountry

import math

print('hello, again') # greetings

print(1.5e-2)
print(4 // 3)
print(math.ceil(3.14159))
print(0.1 * 3)

a = 3
b = 4
c = math.sqrt(a**2 + b**2)
print(c)
print(type(a), type(b), type(c), sep=', ')

def pythagoras(a, b):
	c = math.sqrt(a**2 + b**2)
	return c
	
x = pythagoras(3, 4)
print(x)