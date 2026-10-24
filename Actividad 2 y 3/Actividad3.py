class Libro:
    def __init__(self, titulo, autor, codigo):
        self.titulo = titulo
        self.autor = autor
        self.codigo = codigo
        self.disponible = True

    def obtener_informacion(self):
        estado = "Disponible" if self.disponible else "Prestado"
        return f"'{self.titulo}' por {self.autor} [{self.codigo}] - {estado}"

    def esta_disponible(self):
        return self.disponible


class Usuario:
    def __init__(self, nombre, carnet):
        self.nombre = nombre
        self.carnet = carnet
        self.libros_prestados = []

    def agregar_libro(self, libro):
        self.libros_prestados.append(libro)

    def remover_libro(self, libro):
        if libro in self.libros_prestados:
            self.libros_prestados.remove(libro)


class Bibliotecario:
    def __init__(self, nombre, turno):
        self.nombre = nombre
        self.turno = turno

    def prestar(self, libro, usuario):
        if libro.disponible:
            libro.disponible = False
            return f"{usuario.nombre} recibió {libro.titulo}"
        return "El libro no está disponible"

    def devolver(self, libro):
        libro.disponible = True
        return f"{libro.titulo} fue devuelto"


class Prestamo:
    def __init__(self, libro, usuario, fecha_inicio, fecha_limite):
        self.libro = libro
        self.usuario = usuario
        self.fecha_inicio = fecha_inicio
        self.fecha_limite = fecha_limite
        self.activo = True

    def resumen(self):
        return f"Préstamo de '{self.libro.titulo}' a {self.usuario.nombre} hasta {self.fecha_limite}"

    def finalizar(self):
        self.activo = False
        return f"Préstamo del libro '{self.libro.titulo}' finalizado."


class Estante:
    def __init__(self, codigo, categoria):
        self.codigo = codigo
        self.categoria = categoria
        self.libros = []

    def guardar_libro(self, libro):
        self.libros.append(libro)
        return f"{libro.titulo} guardado en el estante {self.codigo}"

    def buscar_por_codigo(self, codigo):
        for libro in self.libros:
            if libro.codigo == codigo:
                return libro
        return None
        



libro1 = Libro("Cien Años de Soledad", "Gabriel García Márquez", "L001")
usuario1 = Usuario("Sebastian", "U2024")
bibliotecario1 = Bibliotecario("Luis Ramos", "Matutino")
estante1 = Estante("A1", "Literatura")
prestamo1 = Prestamo(libro1, usuario1, "01/08/2026", "08/08/2026")

print(libro1.obtener_informacion())
print(bibliotecario1.prestar(libro1, usuario1))
print(bibliotecario1.devolver(libro1))
print(estante1.guardar_libro(libro1))
print(prestamo1.resumen())