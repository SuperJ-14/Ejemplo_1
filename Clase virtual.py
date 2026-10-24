class Estudiante:
    def __init__(self, nombre, nota):
        self.nombre = self.validar_nombre(nombre)
        self.nota = self.validar_nota(nota) 

#validamos que si exista un nombre
    def validar_nombre(self, nombre):
        nombre = nombre.strip()
        if not nombre:
            raise ValueError("El nombre no puede estar vacío")
        return nombre

    def validar_nota(self, nota):
        if not 0 <= nota <= 100:
            raise ValueError("La nota debe estar entre 0 y 10")
        return nota

    def actualizar_nota(self, nueva_nota):
        self.nota = self.validar_nota(nueva_nota)
