class Estudiante:
    def __init__(self, nombre, carrera):
        self.nombre = nombre
        self.carrera = carrera

    def saludar(self):
        print(f'Hola, soy {self.nombre} y estudio {self.carrera}')


estudiante1 = Estudiante("Pedro", "Ingenieria en Sistemas")
estudiante2 = Estudiante("Maria", "Medicina")

estudiante1.saludar()
estudiante2.saludar()