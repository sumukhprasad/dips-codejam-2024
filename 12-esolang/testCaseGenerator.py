import os
from random import random
os.mkdir('./testCases')
os.mkdir('./testCases/input')
os.mkdir('./testCases/output')
import random


def solve(code):
	code = [c.split() for c in code.split("\n")]
	
	o = {}
	p = ""
	
	for c in code:
		if c[0] == "!":
			break
			
		if c[0] == "@":
			o[c[1]] = int(c[2])
			
		if c[0] == "+":
			o[c[1]]+=int(c[2])
			
		if c[0] == "*":
			o[c[1]]*=int(c[2])
			
		if c[0] == "#":
			p+=f"{o[c[1]]}\n"
	
	return p[:-1:]


def getTestCase(num_lines):
	# Possible commands
	commands = ['@', '+', '*', '#']
	rare_command = '!'
	variables = ['x', 'y', 'z']
	
	# Probability of the rare command appearing
	rare_probability = 0.01  # 1% chance
	
	# List to store the generated lines
	code_lines = [f"@ {i} 333" for i in variables]
	
	for _ in range(num_lines):
		# Decide whether to add the rare command or a regular command
		if random.random() < rare_probability:
			# Rare command - add it with low probability
			code_lines.append(rare_command)
		else:
			# Regular commands
			command = random.choice(commands)
			
			if command == '#':
				# PRINT command
				var = random.choice(variables)
				code_lines.append(f'# {var}')
			else:
				var = random.choice(variables)
				value = random.randint(1, 9)  # Values between 1 and 100
				if command == '@':
					code_lines.append(f'@ {var} {value}')
				elif command == '+':
					code_lines.append(f'+ {var} {value}')
				elif command == '*':
					code_lines.append(f'* {var} {value}')
	
	return code_lines


for i in range(0, 20):
	n_fill = str(i).zfill(2)
	num_lines = random.randint(100, 200)
	code = getTestCase(num_lines)
	result = solve("\n".join(code))
	
	inputFile = open(f'./testCases/input/input{n_fill}.txt', 'a')
	inputFile.write(f"{num_lines+3}\n")
	inputFile.write("\n".join(code))
	inputFile.close()
	
	outputFile = open(f'./testCases/output/output{n_fill}.txt', 'a')
	outputFile.write(result if result.strip() != "" else "no output")
	outputFile.close()

	print(f'Written case {n_fill}.')