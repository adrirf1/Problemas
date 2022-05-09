class Empleado:
    def __init__(self, nombre):
        self.nombre = nombre 

    @staticmethod
    def saludar():
        return "Hola."

e1 = Empleado("Adrian")

print(e1.saludar())