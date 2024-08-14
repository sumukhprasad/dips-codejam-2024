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