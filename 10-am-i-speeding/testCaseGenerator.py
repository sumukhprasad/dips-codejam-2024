import os
from random import random
os.mkdir('./testCases')
os.mkdir('./testCases/input')
os.mkdir('./testCases/output')
import random

def solve(t, road):
	actual_time = getTime(road)
	if t<actual_time:
		return True
	else:
		return False

def getTime(road):
	road_arr = []
	for i in road:
		if i.isdigit():
			road_arr.append([int(i), 0]) # speed, distance
		else:
			road_arr[-1][1]+=1
	time = sum( [i[1]/i[0] for i in road_arr] )
	return time
	
def getTestCase():
	road = ""
	for i in range(random.randint(10, 20)):
		road+=str(random.randint(1, 9))
		for i in range(random.randint(1, 50)):
			road+="="
	actual_time = getTime(road)
	time = actual_time + (random.randint(0-int(actual_time/2), 0) if random.randint(0, 1) else random.randint(1, 100))
	
	return time, road

for i in range(0, 20):
	n_fill = str(i).zfill(2)
	inputFile = open(f'./testCases/input/input{n_fill}.txt', 'a')
	outputFile = open(f'./testCases/output/output{n_fill}.txt', 'a')
	
	
	n = random.randint(10**2, 10**3)
	inputFile.write(str(n))
	
	count = 0
	for i in range(n):
		inputFile.write("\n")
		t, r = getTestCase()
		inputFile.write(f"{t}\n{r}")
		if solve(t, r):
			count+=1

	outputFile.write(str(count))
	
	inputFile.close()
	outputFile.close()

	print(f'Written case {n_fill} with {n} cases and {count} speeding cases.')