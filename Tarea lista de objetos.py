class Libro:
    def __init__(self, titulo: str, autor: str, precio: float, disponible: bool):
        self.titulo = titulo
        self.autor = autor
        self.precio = precio
        self.disponible = disponible

    def __str__(self):
        estado = "Disponible" if self.disponible else "No disponible"
        return f"Titulo: {self.titulo}, Autor: {self.autor}, Precio: ${self.precio:.2f}, Estado: {estado}"


if __name__ == "__main__":
    libros = [
        Libro("Python para principiantes", "Ana García", 250.00, True),
        Libro("Programación orientada a objetos", "Luis Pérez", 320.50, False),
        Libro("Aprendiendo JavaScript", "Marta López", 280.00, True),
        Libro("Algoritmos y estructuras de datos", "Carlos Ruiz", 390.75, True),
        Libro("Introducción a SQL", "Sofía Torres", 210.25, False),
    ]

    print("Lista de libros:")
    for libro in libros:
        print(libro)

    total = sum(libro.precio for libro in libros)
    disponibles = sum(1 for libro in libros if libro.disponible)
    no_disponibles = sum(1 for libro in libros if not libro.disponible)

    print(f"\nPrecio total de todos los libros: ${total:.2f}")
    print(f"Cantidad de libros disponibles: {disponibles}")
    print(f"Cantidad de libros no disponibles: {no_disponibles}")

    libros.append(Libro("Machine Learning Básico", "Daniel Vega", 420.00, True))