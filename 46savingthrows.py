# 46savingthrows.py by marle_lamountry

import random


#roll normal
def roll_normal(n):
	for i in range(n):
		r1 = random.randint(1, 20)
		return r1
	
# roll advantage
def roll_advantage(n):
	for i in range(n):
		r1 = random.randint(1, 20)
		r2 = random.randint(1, 20)
		if r1 >= r2: return r1
		elif r2 >= r1: return r2

#roll disadvantage
def roll_disadvantage(n):
	for i in range(n):
		r1 = random.randint(1, 20)
		r2 = random.randint(1, 20)
		if r1 <= r2: return r1
		elif r2 <= r1: return r2

print('DC', 'norm', 'adv', 'dis', sep='\t')	

#write a program with rolling random numbers and see if they beat the dcs on 5,10,15

trials = 1000
for dc in range(5, 16, 5):
	n = 0
	a = 0
	d = 0
	for i in range(trials):
		if roll_normal(1) >= dc: n += 1
		if roll_advantage(1) >= dc: a += 1
		if roll_disadvantage(1) >= dc: d += 1
	print(dc, n/trials, a/trials, d/trials, sep='\t')

	



		