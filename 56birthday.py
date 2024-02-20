# 56birthday.py by marle lamountry

# python3 56birthday.py 10000 365 23

import random
import sys

trials = int(sys.argv[1])
days = int(sys.argv[2])
people = int(sys.argv[3])

dup = 0
for i in range(trials):
	bdays = []
	for j in range(people):
		d = random.randint(1, days)
		if d in bdays:
			dup += 1
			break
		else:
			bdays.append(d)
print(dup / trials)
