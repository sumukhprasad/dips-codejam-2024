def solve(code):
	code = [c.split() for c in code.split("\n")]
	
	o = {}
	p = ""
	
	for c in code:
		if c[0] == "!":
			break
			
		if c[0] == "@":
			o[c[1]] = int(c[2])
			
		if c[0] == "+":
			o[c[1]]+=int(c[2])
			
		if c[0] == "*":
			o[c[1]]*=int(c[2])
			
		if c[0] == "#":
			p+=f"{o[c[1]]}\n"
	
	return p[:-1:]