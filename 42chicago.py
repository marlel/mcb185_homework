# 42chicago.py by marle_lamountry

#chicago game
#what is approx dist of game scores?
#what is avg score for a game of chicago
# how often does a  player end a game w/ a score of zero

import random

'''
games = 1000
for i in range(games):
	print(f'game #{i}')
	for target in range(2, 13):
		d1 = random.randint(1, 6)
		d2 = random.randint(1, 6)
		if d1 + d2 == target:
			print(f'yay, rolled {d1} and {d2} for {target} points')

games = 10000
for i in range(games):
	score = 0
	for target in range(2, 13):
		if random.randint(1, 6) + random.randint(1, 6) == target:
			score += target
	print(score)
'''
games = 1000000
log = games // 100
total = 0
zeroes = 0
for i in range(games):
	if i % log == 0: print(f'{100 * i/games:.0f}')
	score = 0
	for target in range(2, 13):
		if random.randint(1, 6) + random.randint(1, 6) == target:
			score += target
	if score == 0: zeroes += 1
	total += score
print(total / games)
print(zeroes / games)