def sum_odd_and_even(lst):
	x = 0
	y= 0
	for i in lst:
		if i % 2 == 0:
			x=x+i
		elif i % 2 != 0:
			y = y +i
	return [x,y]

print(sum_odd_and_even([-1, -2, -3, -4, -5, -6]))