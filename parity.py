def parity_analysis(num:int):
	number1 = list(map(int,str(num)))
	if num % 2 == 0 and sum(number1) % 2 == 0:
		return True
	elif num % 2 == 0 and sum(number1) % 2 != 0:
		return False
	elif num % 2 != 0 and sum(number1) % 2 != 0:
		return True
	elif num % 2 != 0 and sum(number1) % 2 == 0:
		return False

numero = 12345678939999999333330

print(list(map(int,str(numero))))

digito = sum(int(x) for x in str(numero))
print(digito)

