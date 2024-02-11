# 40demo.py by marle_lamountry
'''
#43
nts = 'A C G T'

for nt in nts:
	print(nt, end=' ')
print()

import random

for i in range(3): #make 3 sequences
	print('>seq-', i, sep='') #print header
	print(f'>seq-{i+1}')
	for j in range(random.randint(20,50)): #make sequence of var len
		print(random.choice(nts), end='')
		
print()

nts = 'A C G T'
#print the header
for nt in nts:
	print(nt, end=' ')
print()

#print the matrix
limit = 4
for i in range(0, limit):
	for j in range(0, limit):
			if i == j: print('+', end=' ')
			else: print('-', end=' ')
	print()
'''
	
import random
'''
for i in range(5):
	print(random.random())
	
for i in range(50): #container of values (ACGT), 50 letters
	print(random.choice('ACGT'), end='')
print()

for i in range(50):
	r = random.random()
	if r < 0.7: print(random.choice('AT'), end='') #print random w 70% AT avg
	else:		print(random.choice('CG'), end='')

for i in range(3):
	print(random.randint(1,6)) #prints random in 6 sided die 3x
	
for i in range(5):
	print(random.gauss(0.0, 1.0))

print('this line\n has some\n line breaks')
print('a\tb\tcat\tdogma')
print(10, 20, 30, 40, sep='\t')

i = 1
pi = 3.14159
print('normal string {i} {pi}')
print(f'formatted string {i} {pi}')
print(f'tau {pi + pi}')
print(f'formatted string {i} {pi:.3f}
'''
#random.seed(1)
#print(random.random())
#print(random.random())
random.seed(2)
print(random.random())
print(random.random())


	
	