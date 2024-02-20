# 51cdslength.py by marle lamountry

import gzip

path = '../MCB185/data/GCF_000005845.2_ASM584v2_genomic.gff.gz' #hard-coded path to data file
with gzip.open(path, 'rt') as fp:
	for line in fp:
		if line[0] == '#': continue
		words = line.split()
		if words[2] != 'CDS': continue
		beg = int(words[3])
		end = int(words[4])
		print(end - beg + 1)