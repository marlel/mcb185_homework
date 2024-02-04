# 37nilakantha.py by marle_lamountry

#Co-authored with Jonathan Raigosa

def nilakantha(limit):
	sign_flip = 1
	estimation = 3
	for i in range(1, limit):
		denom = 2 * i * (2 * i + 1) * (2 * i + 2)
		equation = 4 / denom
		estimation = estimation + (sign_flip * equation)
		sign_flip = sign_flip * -1
	return estimation

print(nilakantha(1))
print(nilakantha(3))
print(nilakantha(20))
print(nilakantha(50))