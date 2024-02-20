# 55colorname.py by marle lamountry

# python3 55colorname.py ~/Code/MCB185/data/colors_extended.tsv 200 0 50

import sys

colorfile = sys.argv[1]
R = int(sys.argv[2])
G = int(sys.argv[3])
B = int(sys.argv[4])

mind = float('1000')
result = []
with open(colorfile) as fp:
	for line in fp:
		words = line.split('\t')
		color = words[0]
		dec = words[2].split(',')
		r = int(dec[0])
		g = int(dec[1])
		b = int(dec[2])
		d = ((R-r) ** 2 + (G-g) ** 2 + (B-b) ** 2) ** 0.5
		if d < mind:
			mind = d
			result = color
print(result)

