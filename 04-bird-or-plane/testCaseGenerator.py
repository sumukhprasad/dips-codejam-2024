import os
from random import random
os.mkdir('./testCases')
os.mkdir('./testCases/input')
os.mkdir('./testCases/output')
import random
from functools import reduce

def factors(n):    
	return list(set(reduce(list.__add__, 
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0))))

def solve(s):
	path = [[i.split(",")[0][0], int(i.split(",")[0][1::]), int(i.split(",")[1])] for i in s.split()]
	durations = [i[0] for i in path]
	coords = [(i[1], i[2]) for i in path]
	
	def can_construct_from(sub, s):
		return sub * (len(s) // len(sub)) == s
	
	# check for patterns in duration:
	for L in range(1, len(durations) // 2 + 1):
		if len(durations) % L == 0:  # L must be a divisor of n
			sub = durations[:L]
			if can_construct_from(sub, durations):
				return True
	
	# check for patterns in coordinates:
	for L in range(1, len(coords) // 2 + 1):
		if len(coords) % L == 0:  # L must be a divisor of n
			sub = coords[:L]
			if can_construct_from(sub, coords):
				return True
	
	return False
	

def getTestCase():
	isbird = random.randint(0,1)
	
	durations = ["S", "M", "L"]
	
	coords=[]
	
	if not isbird:
		for _ in range(random.randint(100, 1000)):
			coords.append( durations[random.randint(0, 2)] + str(random.randint(0,1000)) + "," + str(random.randint(0,1000)))

	else:
		n_coords = random.randint(100, 1000)
		fac=factors(n_coords)
		p_length = fac[random.randint(0, len(fac)-1)]
		n_repeats = int(n_coords/p_length)
		p = []
		durationrepeats = random.randint(0,1)
		
		if durationrepeats:
			duration_pattern = [durations[random.randint(0, 2)] for _ in range(p_length)]
			for _ in range(n_repeats):
				for i in range(p_length):
					coords.append(duration_pattern[i] + str(random.randint(0,1000)) + "," + str(random.randint(0,1000)))

		else:
			for _ in range(p_length):
				p.append(durations[random.randint(0, 2)] + str(random.randint(0,1000)) + "," + str(random.randint(0,1000)))
		
			coords = p*n_repeats
	
	return " ".join(coords)
			
		

for i in range(0, 20):
	n = str(i).zfill(2)

	inputFile = open(f'./testCases/input/input{n}.txt', 'a')
	outputFile = open(f'./testCases/output/output{n}.txt', 'a')
	
	lines = []
	n_paths = random.randint(100, 1000)
	lines.append(str(n_paths)+"\n")
	
	birds = 0
	
	for i in range(n_paths):
		t = getTestCase()
		lines.append(t+"\n")
		if solve(t):
			birds+=1
	
	

	inputFile.writelines(lines)
	outputFile.write(str(birds))
	
	
	inputFile.close()
	outputFile.close()

	print(f'Written case {n} -- {n_paths} paths, {birds} birds.')