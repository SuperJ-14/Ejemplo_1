"""Almacenamiento directo al crear la lista"""

class Empleado:
    def __init__(self, codigo, nombre, salario):
        self.codigo = codigo
        self.nombre = nombre
        self.salario = salario

    def __str__(self):
        return f"Código: {self.codigo}, Nombre: {self.nombre}, Salario: ${self.salario:.2f}"