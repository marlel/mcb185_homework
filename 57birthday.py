# 57birthday.py by marle lamountry

# python3 57birthday.py 10000 365 23

import random
import sys

trials = int(sys.argv[1])
days = int(sys.argv[2])
people = int(sys.argv[3])

dup = 0
for i in range(trials):
	calendar = []
	for i in range(days):
		calendar.append(0)
	for j in range(people):
		d = random.randint(1, days - 1)
		calendar[d] += 1
		if calendar[d] > 1:
			dup += 1
			break
print(dup / trials)
