# 43randomna.py by marle_lamountry

import random

nts  = 'ACGT' #make variable
n = 10 #make variable
for i in range(n): #make n sequences
	print(f'>seq-{i+1}')  #print header
	for j in range(random.randint(20,50)): #make sequence of var len
		print(random.choice(nts), end='') #print nts in loop
	print() #print enter space
		

