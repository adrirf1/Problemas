def number_length(num):
	x = 0
	for i in str(num):
		x = x+1
	return x

print(number_length(100))