lista = [1,2,3,4,5,6,11,8]
#[9,12]
def func(lista):
    pares = []
    nones = []
    for i in range(len(lista)):
        if lista[i] % 2 == 0:
            pares.append(lista[i])
        if lista[i] % 2 != 0:
            nones.append(lista[i])
    return(sum(pares),sum(nones))


print(func(lista))
