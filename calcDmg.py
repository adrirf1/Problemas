def damage(damage, speed, time):
	if damage < 0 or speed < 0 :
		return "invalid"
	elif time == "second":
		return int(damage*speed)
	elif time == "minute":
		return damage*speed*60
	elif time == "hour":
		return int(damage*speed*3600)
	
print(damage(40, 0.5, "minute"))
