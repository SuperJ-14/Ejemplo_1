class Estudiante:
    def __init__(self, nombre, nota1, nota2, nota3):
        self.nombre = nombre
        self.nota1 = nota1
        self.nota2 = nota2
        self.nota3 = nota3

    def calcular_promedio(self):
        return (self.nota1 + self.nota2 + self.nota3) / 3
    
    def determinar_resultado(self):
        if self.calcular_promedio() >= 61:
            return "Aprobado"
        else:
            return "Reprobado"
        
estudiante1 = Estudiante("Sebastian", 90, 75, 80)

print(f"Estudiante: {estudiante1.nombre}")
print(f"Estudiante: {estudiante1.calcular_promedio():.2f}")
print(f"Estudiante: {estudiante1.determinar_resultado()}")
