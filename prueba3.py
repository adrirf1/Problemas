def texto(x:str):
    dictionario = {'a': 4, 'e': 3, 'i': 1}
    return sum(dictionario[v] for v in x.lower() if v in dictionario)

print(texto('holaoo'))

print(["good","bad"])

