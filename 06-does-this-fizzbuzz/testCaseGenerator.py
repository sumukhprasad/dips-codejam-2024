import os
from random import random
os.mkdir('./testCases')
os.mkdir('./testCases/input')
os.mkdir('./testCases/output')
import random

def solve(arr):
	import math
	arr = arr.split()
	int_arr = []
	for i in arr:
		if i.isdigit():
			int_arr.append(int(i))
		else:
			int_arr.append(None)
	
	for i in range(len(int_arr)):
		if type(int_arr[i])==int:
			int_arr = list(range( int_arr[i]-i, int_arr[i]-i+len(int_arr) ))
			break
	
	fizz_terms = []
	buzz_terms = []
	
	for i in range(len(int_arr)):
		if "Fizz" in arr[i]:
			fizz_terms.append(int_arr[i])
		if "Buzz" in arr[i]:
			buzz_terms.append(int_arr[i])
	
	if fizz_terms == buzz_terms == []:
		return True
	
	gcd_f, gcd_b = math.gcd(*fizz_terms), math.gcd(*buzz_terms)
	
	if gcd_f == 1 or gcd_b == 1:
		return False
		
	return True
	

def getTestCase():
	fac1, fac2 = random.randint(3, 9), random.randint(3, 9)
	start = random.randint(10**4, 10**6)
	end = random.randint(start+10**4, start+10**6)
	
	l = []
	
	for i in range(start, end+1):
		r = ""
		if i%fac1 == 0:
			r+="Fizz"
		if i%fac2 == 0:
			r+="Buzz"
		else:
			r = i
			
		l.append(r)
		
	return " ".join([str(i) for i in l])

def getFalseTestCase():
	start = random.randint(10**4, 10**6)
	end = random.randint(start+10**4, start+10**6)
	
	l = []
	
	for i in range(start, end+1):
		r = i
		
		if random.randint(0,1):
			l.append( ["Fizz", "Buzz", "FizzBuzz"][random.randint(0, 2)] )
			
		l.append(r)
	
	return " ".join([str(i) for i in l])

for i in range(0, 20):
	n_fill = str(i).zfill(2)

	t = getTestCase() if random.randint(0, 1) else getFalseTestCase()
	
	s = solve(t)

	inputFile = open(f'./testCases/input/input{n_fill}.txt', 'a')
	inputFile.write(t)
	inputFile.close()
	
	outputFile = open(f'./testCases/output/output{n_fill}.txt', 'a')
	outputFile.write(str(1 if s else 0))
	outputFile.close()

	print(f'Written case {n_fill} with {len(t.split())} elements, fizzbuzz {"in" if not s else ""}valid.')