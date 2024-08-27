import os
from random import random
os.mkdir('./testCases')
os.mkdir('./testCases/input')
os.mkdir('./testCases/output')
import random
import string

def solve(s):
	m = 0
	for i in range(len(s)-5):
		substring = s[i:i+6]
		if not all(c in string.hexdigits for c in substring):
			break
		
		red, green, blue = [int(substring[j:j+2], 16) for j in range(0, 6, 2)]
		
		if blue < 0.8*green and red < 0.64*green:
			m+=1
			
	return m

	
	
for i in range(0, 20):
	n_char=random.randint(10**4, 10**6)
	s = ''.join(random.choices(string.hexdigits, k=n_char))
	ioArr = [s.upper(), str(solve(s))]

	n = str(i).zfill(2)

	inputFile = open(f'./testCases/input/input{n}.txt', 'a')
	inputFile.write(f"{n_char}\n")
	inputFile.write(ioArr[0])
	inputFile.close()
	
	outputFile = open(f'./testCases/output/output{n}.txt', 'a')
	outputFile.write(ioArr[1])
	outputFile.close()

	print(f'Written case {n} with {len(s)} characters.')