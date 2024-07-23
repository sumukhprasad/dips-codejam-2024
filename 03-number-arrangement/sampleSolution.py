def solve(a, b):
	a_digits = [int(i) for i in str(a)]
	b_digits = [int(i) for i in str(b)]
	
	if len(a_digits) != len(b_digits):
		return False
	
	a_deltas = [a_digits[i+1]-a_digits[i] for i in range(len(a_digits)-1)]
	b_deltas = [b_digits[i+1]-b_digits[i] for i in range(len(b_digits)-1)]
	
	return False if a_deltas != b_deltas else True