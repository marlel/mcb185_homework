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