# 53genomestats.py by marle lamountry

# python3 53genomestats.py ~/Code/MCB185/data/A.thaliana.gff.gz gene


import sys
import gzip
import math

gffpath = sys.argv[1]
feature = sys.argv[2]

val = [] #empty list
with  gzip.open(gffpath, 'rt') as fp:
	for line in fp:
		if line[0] == '#': continue
		words = line.split()
		if words[2] == feature:
			beg = int(words[3])
			end = int(words[4])
			val.append(end - beg + 1)

#count
print('Count:', len(val))

#min, max
def minmax(vals):
	mini = vals[0]
	maxi = vals[0]
	for x in vals:
		if x < mini: mini = x
		elif x > maxi: maxi = x
	return mini, maxi
mini, maxi = minmax(val)
print("Minimum:", mini)
print("Maximum:", maxi)

#mean
def mean(vals):
	total = 0
	for x in vals: total += x
	return total / len(vals)
mean = mean(val)
print("Mean:", mean)

#stdv
num = 0
for x in val:
	num += ((x - mean) ** 2)
stdv = math.sqrt(num / len(val))
print("Standard Deviation:", stdv)

#median
for x in sys.argv[3:]:
	val.append(int(x))
val.sort()

if len(val) % 2 == 0:
	a = val[len(val) // 2 - 1]
	b = val[len(val) // 2]
	med = (a + b) / 2
else:
	med = val[len(val) // 2]
print("Median:", med)
	

