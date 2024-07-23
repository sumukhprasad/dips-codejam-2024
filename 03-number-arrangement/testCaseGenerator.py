import os
from random import random
os.mkdir('./testCases')
os.mkdir('./testCases/input')
os.mkdir('./testCases/output')
import random
from math import *


def solve(a, b):
	a_digits = [int(i) for i in str(a)]
	b_digits = [int(i) for i in str(b)]
	
	if len(a_digits) != len(b_digits):
		return False
	
	a_deltas = [a_digits[i+1]-a_digits[i] for i in range(len(a_digits)-1)]
	b_deltas = [b_digits[i+1]-b_digits[i] for i in range(len(b_digits)-1)]
	
	return False if a_deltas != b_deltas else True
	
def increment(x):
	k=random.randint(0, min([9-int(i) for i in str(x)]))
	return "".join([str(int(j)+k) for j in str(x)])





for i in range(0, 20):
	testcase_number = str(i).zfill(2)
	
	m = 0
	
	inputFile = open(f'./testCases/input/input{testcase_number}.txt', 'a')
	lines = []
	n = random.randint(10**3, 10**4)
	lines.append(str(n))
	for i in range(n):
		a = random.randint(10**8, 10**10)
		b = random.randint(10**8, 10**10) if random.randint(0, 1) else increment(a)
		res = solve(a, b)
		lines.append(f"{a} {b}\n")
		if res:
			m+=1
	inputFile.writelines(lines)
	inputFile.close()
	
	result = sum([int(i) for i in str(floor(sqrt(m)))])
	outputFile = open(f'./testCases/output/output{testcase_number}.txt', 'a')
	outputFile.write(f"{result}")
	outputFile.close()

	print(f'Written case {testcase_number} with {m} positive trials in {n} total.')