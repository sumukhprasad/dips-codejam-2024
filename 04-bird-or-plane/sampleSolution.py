def factors(n):    
	return list(set(reduce(list.__add__, 
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0))))

def solve(s):
	path = [[i.split(",")[0][0], int(i.split(",")[0][1::]), int(i.split(",")[1])] for i in s.split()]
	durations = [i[0] for i in path]
	coords = [(i[1], i[2]) for i in path]
	
	def can_construct_from(sub, s):
		return sub * (len(s) // len(sub)) == s
	
	# check for patterns in duration:
	for L in range(1, len(durations) // 2 + 1):
		if len(durations) % L == 0:  # L must be a divisor of n
			sub = durations[:L]
			if can_construct_from(sub, durations):
				return True
	
	# check for patterns in coordinates:
	for L in range(1, len(coords) // 2 + 1):
		if len(coords) % L == 0:  # L must be a divisor of n
			sub = coords[:L]
			if can_construct_from(sub, coords):
				return True
	
	return False