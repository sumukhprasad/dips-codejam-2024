import os
from random import random
os.mkdir('./testCases')
os.mkdir('./testCases/input')
os.mkdir('./testCases/output')
import random
import string

def solve(lists):
	count = 0
	
	for l in lists:
		d = dict(l)
		keys = d.keys()
		for k in keys:
			v = d[k]
			if v in keys and d[v] == k:
				count+=1
		
	return count


def getTestCase(n):
	lists = []
	for i in range(n):
		lists.append([])
		z = random.randint(10**2, 10**3)
		o = {}
		while len(o.keys())<z:
			o[''.join(random.choices(string.ascii_lowercase, k=3))] = ''.join(random.choices(string.ascii_lowercase, k=3))
		
		lists[-1] = list(zip(o.keys(), o.values()))
	
	return lists

for i in range(0, 20):
	n_fill = str(i).zfill(2)
	n = random.randint(10**2, 10**3)
	lists = getTestCase(n)
	s = solve(lists)

	inputFile = open(f'./testCases/input/input{n_fill}.txt', 'a')
	inputFile.write(f"{n}\n")
	
	for l in lists:
		k = " ".join([ "=".join(j) for j in l ])
		inputFile.write(f"{k}\n")
	
	inputFile.close()
	
	outputFile = open(f'./testCases/output/output{n_fill}.txt', 'a')
	outputFile.write(str(s))
	outputFile.close()

	print(f'Written case {n_fill}, {n} lists, {s} transitive equalities.')