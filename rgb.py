def color_invert(rgb):
	return (abs(rgb[0]-255),abs(rgb[1]-255),abs(rgb[2]-255))

print(color_invert((100,200,255)))