# lists = [  [("abc", "def"), ("ghi", "jkl"), ("mno, "pqr""), ...], ...  ]

def solve(lists):
	count = 0
	
	for l in lists:
		d = dict(l)
		keys = d.keys()
		for k in keys:
			v = d[k]
			if v in keys and d[v] == k:
				count+=1
		
	return count