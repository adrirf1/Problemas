import math
def line_length(dot1, dot2):
	x1 = dot1[0]
	y1 = dot1[1]
	x2 = dot2[0]
	y2 = dot2[1]
	return round(math.sqrt((x2-x1)**2+(y2-y1)**2),2)

print(line_length([15, 7], [22, 11]))