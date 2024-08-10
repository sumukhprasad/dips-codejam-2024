def solve(arr):
	import math
	arr = arr.split()
	int_arr = []
	for i in arr:
		if i.isdigit():
			int_arr.append(int(i))
		else:
			int_arr.append(None)
	
	for i in range(len(int_arr)):
		if type(int_arr[i])==int:
			int_arr = list(range( int_arr[i]-i, int_arr[i]-i+len(int_arr) ))
			break
	
	fizz_terms = []
	buzz_terms = []
	
	for i in range(len(int_arr)):
		if "Fizz" in arr[i]:
			fizz_terms.append(int_arr[i])
		if "Buzz" in arr[i]:
			buzz_terms.append(int_arr[i])
	
	if fizz_terms == buzz_terms == []:
		return True
	
	gcd_f, gcd_b = math.gcd(*fizz_terms), math.gcd(*buzz_terms)
	
	if gcd_f == 1 or gcd_b == 1:
		return False
		
	return True