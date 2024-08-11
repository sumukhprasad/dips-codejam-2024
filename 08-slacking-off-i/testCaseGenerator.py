import os
from random import random
os.mkdir('./testCases')
os.mkdir('./testCases/input')
os.mkdir('./testCases/output')
import random

def solve(n, arr):
	s = []
	f = []

	for i in range(n):
		inputArr = list(map(int, arr[i].split()))
		s.append(inputArr[0])
		f.append(inputArr[1])

	comp = []
	
	i = 0
	comp.append(i)
	for j in range(n):
		if s[j] >= f[i]:
			comp.append(j)
			i = j
	
	return len(comp)

def getTestCase():
	numberOfCompilations = random.randint(0,10**4)
	compilationTimesIntegerStore = []
	for _ in range(numberOfCompilations):
		startT = random.randint(0,(10**4)-50)
		dur = random.randint(1,50)
		compilationTimesIntegerStore.append([startT, startT+dur])
		
	compilationTimesIntegerStore.sort(key=lambda x: x[1])

	conferenceTimes = [str(e[0]) + " " + str(e[1]) for e in compilationTimesIntegerStore]

	return [str(numberOfCompilations) + "\n" + "\n".join(conferenceTimes), str(solve(numberOfCompilations, conferenceTimes))]

for i in range(0, 20):
	n = str(i).zfill(2)
	ioArr = getTestCase()

	inputFile = open(f'./testCases/input/input{n}.txt', 'a')
	inputFile.write(ioArr[0])
	inputFile.close()
	
	outputFile = open(f'./testCases/output/output{n}.txt', 'a')
	outputFile.write(ioArr[1])
	outputFile.close()

	print(f'Written case {n} with {ioArr[1]} possible compilations.')