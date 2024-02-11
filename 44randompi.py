# 44randompi.py by marle_lamountry
# Co-author with Addie Ferrer

import random

pi_inside = 0
run = 0
while True:
	run += 1 #increment
	x = random.random()
	y = random.random()
	distance = (x**2 + y**2) **0.5
	if distance <= 1: pi_inside += 1
	pi = 4 * (pi_inside / run)
	print(pi)