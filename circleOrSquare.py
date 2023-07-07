import math
def sq(radio, area):

    circunferencia = 3.14*(radio*2)
    perimeter = math.sqrt(area)*4

    if circunferencia > perimeter:
        return True
    else:
        return False

print(sq(16,625))
print(sq(5,100))
print(sq(8,144))