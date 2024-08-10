import os
from random import random
os.mkdir('./testCases')
os.mkdir('./testCases/input')
os.mkdir('./testCases/output')
import random

def solve(arr):
	import itertools
	
	areas = []
	for c in itertools.combinations(arr, 3):
		x,y = zip(*c)
		area = 0.5 * (x[0] * (y[1] - y[2]) + x[1] * (y[2] - y[0]) + x[2] * (y[0] - y[1]))
		area = area if area > 0. else (0-area)
		areas.append(area)
		
	return areas.count(42)


def getTestCase(n):
	return [ (random.randint(0, 42), random.randint(0, 42)) for _ in range(n) ]

for i in range(0, 20):
	n_fill = str(i).zfill(2)
	n = random.randint(10**2, 10**3)
	coords = getTestCase(n)
	s = solve(coords)
	print(s)

	inputFile = open(f'./testCases/input/input{n_fill}.txt', 'a')
	inputFile.write(f"{n}\n")
	inputFile.write("\n".join([f"{c[0]} {c[1]}" for c in coords]))
	inputFile.close()
	
	outputFile = open(f'./testCases/output/output{n_fill}.txt', 'a')
	outputFile.write(f"{s}")
	outputFile.close()

	print(f'Written case {n_fill} with {s} valid systems.')