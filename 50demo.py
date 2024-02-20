# 50demo.py by marle lamountry



s = 'ABCDEFGHIJ'
print(s[0:5])

tax = ('Homo', 'sapiens', 9606) # construct tuple
print(tax)

print(tax[1])
print(tax[::-1])

def quadratic(a, b, c):
    x1 = (-b + (b**2 - 4*a*c)**0.5) / (2*a)
    x2 = (-b - (b**2 - 4*a*c)**0.5) / (2*a)
    return x1, x2

x = quadratic(1,1,1)
print(x[0])

nts = 'ACGT'
for i in range(len(nts)):
	print(i, nts[i])
	
for i, nt in enumerate(nts):
	print(i, nt)
	
i = 0
for nt in nts:
	print(i, nt)
	i += 1
	
names = ('adenine', 'cytosine', 'guanine', 'thymine')
for nt, name in zip(nts, names):
	print(nt, name)
	
nts = ['A', 'T', 'C']
print(nts)
nts[2] = 'G'
print(nts)

nts.append('C')
print(nts)

nts = 'ACGT'
for i, nt in enumerate(nts):
	print(i, nt)

nts = 'ACGT'
for i in range(len(nts)):
    print(i, nts[i])

nts = 'ACGT'
names = ('adenine', 'cytosine', 'guanine', 'thymine')
for i in range(len(names)):
	print(nts[i], names[i])

names = ('adenine', 'cytosine', 'guanine', 'thymine')
nts = 'ACGT'
for nt, name in zip(nts, names):
	print(nt, name)

for i, (nt, name) in enumerate(zip(nts, names)):
	print(i, nt, name)

nts = ['A', 'T', 'C']
print(nts)
nts[2] = 'G'
print(nts)

nts.append('C')
print(nts)

last = nts.pop()
print(last)

nts.sort()
print(nts)
nts.sort(reverse=True)
print(nts)

nucleotides = nts
nucleotides.append('C')
nucleotides.sort()
print(nts, nucleotides)

items = list()
print(items)
items.append('eggs')
print(items)

stuff = []
stuff.append(3)
print(stuff)
alph = 'ACDEFGHIKLMPQRSVW'
print(alph)
aas = list(alph)
print(aas)

text =  'good day  to you'
words = text.split()
print(words)

line = '1.41,2.72,3.14'
print(line.split(','))

s = '-'.join(aas)
print(s)
s = ''.join(aas)
print(s)

alph = 'ACDEFGHIKLMPQRSVW'
if 'A' in alph: print('yay')
if 'a' in alph: print('no')

print('index G?', alph.index('G'))
print('index W?', alph.index('W'))
if thing in list: idx = list.index(thing)



	
	
	
	
	
	
	
	
	
	
	
	
	
	