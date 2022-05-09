from textwrap import wrap


def funcion_decorador(func):
    def wrapper(*args):
        print("------------")
        print(func(*args))
        print("------------")
    return wrapper

def gritar(func):
    def wrapper(nombre,edad):
        return func(nombre,edad).upper()
    return wrapper

def secreto(func):
    def wrapper(nombre,edad):
        return func(nombre,edad).lower()
    return wrapper


def saludo(nombre,edad):
    s = "Hola {} tienes {} anos.".format(nombre,edad)
    return s
@funcion_decorador
def suma(n,m):
    return n+m


print(saludo('adrian',20))