"""Definir la clase y crear la lista de objetos"""
class Estudiante:
    def __init__(self, nombre, edad, nota):
        self.nombre = nombre
        self.edad = edad
        self.nota = nota

    def __str__(self):
        return f"Nombre: {self.nombre}, Edad: {self.edad}, Nota: {self.nota}"

#creación de una lista de objetos Estudiante
estudiantes = [
    Estudiante("Alice", 20, 8.5),
    Estudiante("Bob", 22, 7.0),
    Estudiante("Charlie", 19, 9.5),
]

"""Recorrer la lista e imprimir cada objeto"""
for e in estudiantes:
    print(e)

"""Acceder a un atributo especifico de un elemento"""
print(estudiantes[0].nombre)  # Imprime: el nombre del primer estudiante
print(estudiantes[1].nombre)  #Imprime: el nombre del segundo estudiante
print(estudiantes[2].nombre)  #Imprime: el nombre del tercer estudiante
print('###### fin Acceder a un atributo especifico de un elemento ######')

"""Calcular un valor agregado (promedio de notas)"""
suma_notas = 0 #Línea en blanco para separar la salida
for estudiante in estudiantes:
    suma_notas += estudiante.nota
promedio_notas = suma_notas / len(estudiantes)  
"""len = suma todo y devuelve el total de elementoss de la lista"""


print(f"------- Promedio de notas: {promedio_notas} -------")
print('###### fin promedio de notas ######')