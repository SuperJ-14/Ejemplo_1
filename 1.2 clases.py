class Estudiante:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def saludar(self):
        print(f'Hola, soy {self.nombre} y tengo {self.edad} años')


estudiante1 = Estudiante("Pedro", 22)
estudiante2 = Estudiante("Maria", 20)

estudiante1.saludar()
estudiante2.saludar()