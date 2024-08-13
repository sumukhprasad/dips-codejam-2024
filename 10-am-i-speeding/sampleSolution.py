def solve(t, road):
	actual_time = getTime(road)
	if t<actual_time:
		return True
	else:
		return False

def getTime(road):
	road_arr = []
	for i in road:
		if i.isdigit():
			road_arr.append([int(i), 0]) # speed, distance
		else:
			road_arr[-1][1]+=1
	time = sum( [i[1]/i[0] for i in road_arr] )
	return time