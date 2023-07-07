import math
def number_split(n):
	if n < 0:
		return [math.floor(n/2),int(n/2)]
	if n % 2 == 0:
		return [int(n/2),int(n/2)]
	elif n % 2 != 0:
		return [int(n/2),math.ceil(n/2)]
	

print(number_split(11))