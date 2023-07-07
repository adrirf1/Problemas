def asc_des_none(lst, s):
	if s == "None":
		return lst
	elif s == "Asc":
		return sorted(lst)
	elif s == "Des":
		return (sorted(lst))[::-1]
	

print(asc_des_none([7, 8, 11, 66],"Des"))