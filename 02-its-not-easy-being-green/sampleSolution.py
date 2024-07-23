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