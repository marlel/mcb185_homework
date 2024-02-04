# 32fibonacci.py by marle_lamountry

def fibonacci(i):
	if i == 0:
		return 0
	elif i == 1:
		return 1
	else:
		return fibonacci(i-1) + fibonacci(i-2)

print(fibonacci(1))
print(fibonacci(2))
print(fibonacci(3))
print(fibonacci(4))
print(fibonacci(5))
print(fibonacci(6))
print(fibonacci(7))
print(fibonacci(8))
print(fibonacci(9))
print(fibonacci(10))
