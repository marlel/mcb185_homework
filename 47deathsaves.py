# 47deathsaves.py by marle_lamountry

#if # < 10 = failure, if # > 10 = success
#if collect 3 failures = die, 3 success = stable
#if roll a 1 = 2 failures, if roll 20 = revive

import random

rolls = 10000
death = 0
stable = 0
revived = 0

for i in range(rolls):
	failure = 0
	success = 0
	while True:
		roll = random.randint(1, 20)
		if roll == 1:
			failure += 2
		elif roll == 20:
			revived += 1
			break
		elif roll >= 10:
			success += 1
		else:
			failure += 1
		
		if failure >= 3:
			death += 1
			break
		elif success >= 3:
			stable += 1
			break
prob_death = death / rolls
prob_stable = stable / rolls
prob_revived = revived / rolls

	
print(prob_death)
print(prob_stable)
print(prob_revived)



