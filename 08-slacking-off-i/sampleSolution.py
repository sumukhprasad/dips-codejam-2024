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