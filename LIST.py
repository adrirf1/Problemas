test = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
test.sort(key=lambda x: x[1])


test2 = [6,4,1,0,9,2,1]
nueva = []
for i in test2:
    if i not in nueva:
        nueva.append(i)


def ejercicio10(num,texto):
    separados = texto.split()
    nueva = []
    for i in separados:
        if len(i) > num:
            nueva.append(i)
    return nueva

def ejercicio11(lista1,lista2):
    for i in range(len(lista1)):
        for j in range(len(lista2)):
            if lista1[i] == lista2[j]   :
                return True

def ejercicio12(lista):
   return [y for x,y in enumerate(lista) if x not in [0,4,5] ]




def ejercicio13():
    x = []
    for i in range(3):
       x.append([])
       for j in range(4):
        x[i].append([])
        for k in range(6):
            x[i][j].append("*")
    return x



