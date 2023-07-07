def int_to_str(num):
	return f"{num}"

def str_to_int(num):
    n =0
    for i in range(len(num)):
        digito = ord(num[i]) - 48
        n = n * 10 + digito
    return n
	    

	    





print(str_to_int("32"))


'''
"987"
57-48 = 9
56-48 = 8
55-48 = 7

n * 10 + numero
n = 0
n = 9
n = 98
n = 987
'''