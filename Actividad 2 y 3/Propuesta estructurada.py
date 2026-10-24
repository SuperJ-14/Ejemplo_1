def calcular_promedio(nota1, nota2, nota3):
    return (nota1 + nota2 + nota3)/ 3

def determinar_resultado(promedio):
    if promedio >= 61:
        return "Aprobado"
    else:
        return "Reprobado"
    
nombre_estudiante = "Sebastian"
nota1 = 80
nota2 = 75
nota3 = 90

prom = calcular_promedio(nota1, nota2, nota3)
resultado = determinar_resultado(prom)

print(f"Estudiante: {nombre_estudiante}")
print(f"Promedio: {prom: .2f}")
print(f"Estado: {resultado}")