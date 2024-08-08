# Assuming that the grid has been parsed from input into a 2-dimensional array

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