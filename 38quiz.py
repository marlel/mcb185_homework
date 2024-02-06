# 38quiz.py by Marle Lamountry
#Co-author: Addie Ferrer

#Task 1
def pi_estimate(n):
	x = 1
	sign = -1
	for i in range(3, n, 2):
		equation = sign * (1/n)
		sign = sign * -1
		x = x + equation
		pi = 4 * (x)
	return pi
	
print(pi_estimate(4))
print(pi_estimate(12))

#Task 2
def nilakantha(limit):
	sign_flip = 1
	estimation = 3
	for i in range(1, limit):
		denom = 2 * i * (2 * i + 1) * (2 * i + 2)
		equation = 4 / denom
		estimation = estimation + (sign_flip * equation)
		sign_flip = sign_flip * -1
	return estimation

print(pi_estimate(100), nilakantha(100))
	
