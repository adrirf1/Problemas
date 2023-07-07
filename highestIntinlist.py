def find_highest(lst):
	x = None
	for i in lst:
		if x == None or x<i:
			x=i
	return x


print(find_highest([-21,0,1]))

    