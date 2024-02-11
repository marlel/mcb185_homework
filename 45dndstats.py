# 45dndstats.py by marle_lamountry

import random

rolls =  1000

# 3D6: roll 3 six sided dice
total_3d6 = 0
for i in range(rolls):
	score = 0
	for j in range(3):
		d = random.randint(1, 6)
		score += d
	total_3d6 += score
print(total_3d6 / rolls)

# 3D6r1: roll 3 six-sided dice, but re-roll any 1s
total_3dr1 = 0
for i in range(rolls):
	score = 0
	d1 = random.randint(1, 6)
	d2 = random.randint(1, 6)
	d3 = random.randint(1, 6)
	if d1 == 1:
		d1 = random.randint(1, 6)
		score += d1
	else:
		score += d1
	if d2 == 1:
		d2 = random.randint(1, 6)
		score += d2
	else:
		score += d2
	if d3 == 1:
		d3 = random.randint(1, 6)
		score += d3
	else:
		score += d3
	total_3dr1 += score
print(total_3dr1 / rolls)

# 3D6x2: roll pairs of six-sided die 3x, taking the max each time
total_3d6x2 = 0
n = 3
for i in range(rolls):
	score = 0
	d1 = random.randint(1, 6)
	d2 = random.randint(1, 6)
	if d1 >= d2:
		score += d1
	else:
		score = d2
	total_3d6x2 += score
print((total_3d6x2 / rolls)*n)
		

# 4Dr1: roll 4 six-sided die, dropping the lowest roll
total_4dr1 = 0
for i in range(rolls):
	score = 0
	d1 = random.randint(1, 6)
	d2 = random.randint(1, 6)
	d3 = random.randint(1, 6)
	d4 = random.randint(1, 6)
	if d1 < d2 and d1 < d3 and d1 < d4: score += d2 + d3 + d4
	elif d2 < d1 and d2 < d3 and d2 < d4: score += d1 + d3 + d4
	elif d3 < d1 and d3 < d2 and d3 < d4: score += d1 + d2 + d4
	else: score += d1 + d2 + d3
	total_4dr1 += score
print(total_4dr1 / rolls)
