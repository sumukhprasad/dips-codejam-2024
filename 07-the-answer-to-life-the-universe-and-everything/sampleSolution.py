def solve(arr):
	import itertools
	
	areas = []
	for c in itertools.combinations(arr, 3):
		x,y = zip(*c)
		area = 0.5 * (x[0] * (y[1] - y[2]) + x[1] * (y[2] - y[0]) + x[2] * (y[0] - y[1]))
		area = area if area > 0. else (0-area)
		areas.append(area)
		print(c, area)
		
	return areas.count(42)