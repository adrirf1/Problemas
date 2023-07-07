#BITWISE AND = &
#Si los 2 son 1, se convierte en 1, sino no en 0.
#100111000 = 312
#111110100 = 500
#100110000 = 304
print("BITWISE AND")
print(500&312)

#BITWISE OR = |
#Si los 2 son 0, se convierte en 0, sino no en 1.
#100111000 = 312
#111110100 = 500
#111111100 = 508
print("BITWISE OR")
print(312|500)

#BITWISE XOR = ^
#Si solo uno es 1 se convierte en 1, si los dos son 1 o los dos son 0, se convierte en 0
#Si los dos son difertentes se convierte en 1, sino 0.
#100111000 = 312
#111110100 = 500
#011001100 = 204
print("BITWISE XOR")
print(312^500)


#BITWISE NOT = ~
#Cambia los 1 por los 0, y los 0 por los 1.
#100111000 = 312
#011000111 = 199
print("BITWISE NOT")
print(~123)


#SHIFT <<
#Es lo mismo a x * 2**y
print("SHIFT <<")
print(10<<6)

#SHIFT >> 
#Es lo mismo a  x // 2**y
print("SHIFT >>")
print(8966>>5)
print(8966//(2**5))