import os
os.mkdir('./testCases')
os.mkdir('./testCases/input')
os.mkdir('./testCases/output')
import random

def rotate90(l):
	return [list(reversed(x)) for x in zip(*l)]

def solve(grid):
	stones_on_receptacle = []
	
	for i in range(4):
		grid = rotate90(grid)
		unbalanced = 0
		for row in grid:
			row_split = [[]]
			for c in row:
				if c == "#":
					row_split.append([])
				else:
					row_split[-1].append(c)
					
			for z in row_split[:-1:]:
				unbalanced += z.count("O")
		stones_on_receptacle.append(unbalanced)
	
	return sorted(stones_on_receptacle)[0]
			
def printgrid(grid):
	for r in grid:
		print(" ".join([str(i) for i in r]))		
			

def getTestCase(m, n):
	chars = ["."]*3 + ["#", "O"]
	return [[chars[random.randint(0, len(chars)-1)] for j in range(n)] for i in range(m)]
	

for i in range(0, 20):
	n_fill = str(i).zfill(2)
	
	m, n = random.randint(10**2, 10**3), random.randint(10**2, 10**3)
	# m, n = random.randint(5, 10), random.randint(5, 10)
	grid = getTestCase(m, n)
	s = solve(grid)
	grid_rep = "\n".join([" ".join(r) for r in grid])
	
	
	inputFile = open(f'./testCases/input/input{n_fill}.txt', 'a')
	inputFile.write(f"{m} {n}\n")
	inputFile.write(grid_rep)
	inputFile.close()
	
	outputFile = open(f'./testCases/output/output{n_fill}.txt', 'a')
	outputFile.write(str(s))
	outputFile.close()

	print(f'Written case {n_fill} with {m} rows, {n} columns, {s} unbalanced stones.')