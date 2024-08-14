import os
from random import random
os.mkdir('./testCases')
os.mkdir('./testCases/input')
os.mkdir('./testCases/output')
import random

def solve(grid, start):
	m, n = len(grid), len(grid[0])
	start_x, start_y = start
	
	# Directions for moving in straight lines: horizontal, vertical, and diagonal
	directions = [
		(1, 0), (-1, 0),  # Down, Up
		(0, 1), (0, -1),  # Right, Left
		(1, 1), (-1, -1), # Down-Right, Up-Left
		(1, -1), (-1, 1)  # Down-Left, Up-Right
	]
	
	def can_reach_hole(x, y, dx, dy):
		while 0 <= x < m and 0 <= y < n:
			if grid[x][y] == 1:  # Hole found
				return True
			if grid[x][y] == 2:  # Obstacle found
				return False
			x += dx
			y += dy
		return False  # Reached the edge of the grid without finding a hole
	
	# Try all directions from the starting position
	for dx, dy in directions:
		if can_reach_hole(start_x, start_y, dx, dy):
			return True
	
	return False

def getTestCase(grid_size, num_holes, num_obstacles):
	m, n = grid_size
	grid = [[0] * n for _ in range(m)]
	
	# Place holes
	holes_placed = 0
	while holes_placed < num_holes:
		x = random.randint(0, m - 1)
		y = random.randint(0, n - 1)
		if grid[x][y] == 0:
			grid[x][y] = 1
			holes_placed += 1
	
	# Place obstacles
	obstacles_placed = 0
	while obstacles_placed < num_obstacles:
		x = random.randint(0, m - 1)
		y = random.randint(0, n - 1)
		if grid[x][y] == 0:
			grid[x][y] = 2
			obstacles_placed += 1

	# Choose a random start position
	start_x = random.randint(0, m - 1)
	start_y = random.randint(0, n - 1)
	
	return grid, (start_x, start_y)

for i in range(0, 20):
	n_fill = str(i).zfill(2)
	m, n = random.randint(10, 50), random.randint(10, 50)
	grid, start = getTestCase((m,n), random.randint(0, 5), random.randint(0, 50))

	for row in grid:
		print(" ".join(map(str, row)))
	print("Start position:", start)
	
	s = 1 if solve(grid, start) else 0
	print(s)

	inputFile = open(f'./testCases/input/input{n_fill}.txt', 'a')
	inputFile.write(f"{m} {n} {start[0]} {start[1]}\n")
	for row in grid:
		inputFile.write(" ".join(map(str, row))+"\n")
	inputFile.close()
	
	outputFile = open(f'./testCases/output/output{n_fill}.txt', 'a')
	outputFile.write(str(s))
	outputFile.close()

	print(f'Written case {n_fill}.')