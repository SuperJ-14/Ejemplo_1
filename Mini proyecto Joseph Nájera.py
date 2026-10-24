class Videojuego:
    def __init__(self, codigo, titulo, genero, plataforma):
        self.codigo = codigo
        self.titulo = titulo
        self.genero = genero
        self.plataforma = plataforma
        self.__horas_jugadas = 0
        self.__completado = False

    @property
    def horas_jugadas(self):
        return self.__horas_jugadas

    @property
    def completado(self):
        return self.__completado

    def sumar_horas(self, horas):
        if horas > 0:
            self.__horas_jugadas += horas
            print(f"Se sumaron {horas} horas. Total actual: {self.__horas_jugadas}")
        else:
            print("Error: Las horas deben ser mayores a cero.")

    def marcar_completado(self):
        self.__completado = True
        print(f"¡El videojuego '{self.titulo}' ha sido marcado como completado!")

    def mostrar_informacion(self):
        estado = "Completado" if self.__completado else "Pendiente"
        print(f"[{self.codigo}] {self.titulo} | Género: {self.genero} | Plataforma: {self.plataforma} | Horas: {self.__horas_jugadas} | Estado: {estado}")


class CatalogoVideojuegos:
    def __init__(self):
        self.lista_videojuegos = []

    def agregar_videojuego(self, juego):
        for j in self.lista_videojuegos:
            if j.codigo == juego.codigo:
                print("Error: Ya existe un videojuego con ese código.")
                return False
        self.lista_videojuegos.append(juego)
        print("Videojuego agregado exitosamente al catálogo.")
        return True

    def listar_catalogo(self):
        if not self.lista_videojuegos:
            print("El catálogo está vacío.")
            return
        print("\n--- CATÁLOGO DE VIDEOJUEGOS ---")
        for juego in self.lista_videojuegos:
            juego.mostrar_informacion()

    def buscar_por_codigo(self, codigo):
        for juego in self.lista_videojuegos:
            if juego.codigo.lower() == codigo.lower():
                return juego
        return None

    def buscar_por_titulo(self, titulo):
        encontrados = [j for j in self.lista_videojuegos if titulo.lower() in j.titulo.lower()]
        return encontrados

    def mostrar_estadisticas(self):
        total = len(self.lista_videojuegos)
        if total == 0:
            print("No hay datos para calcular estadísticas.")
            return
        
        completados = sum(1 for j in self.lista_videojuegos if j.completado)
        total_horas = sum(j.horas_jugadas for j in self.lista_videojuegos)
        promedio_horas = total_horas / total

        print("\n--- ESTADÍSTICAS DEL CATÁLOGO ---")
        print(f"Cantidad total de videojuegos: {total}")
        print(f"Videojuegos completados: {completados}")
        print(f"Videojuegos pendientes: {total - completados}")
        print(f"Total de horas jugadas: {total_horas}")
        print(f"Promedio de horas por juego: {promedio_horas:.2f}")


def main():
    catalogo = CatalogoVideojuegos()
    
    while True:
        print("\n=== MENÚ CATÁLOGO DE VIDEOJUEGOS ===")
        print("1. Agregar videojuego")
        print("2. Mostrar catálogo completo")
        print("3. Buscar videojuego por código")
        print("4. Buscar videojuego por título")
        print("5. Registrar horas jugadas")
        print("6. Marcar videojuego como completado")
        print("7. Mostrar estadísticas del catálogo")
        print("0. Salir")
        
        try:
            opcion = int(input("Seleccione una opción: "))
            
            if opcion == 1:
                cod = input("Código: ")
                tit = input("Título: ")
                gen = input("Género: ")
                plat = input("Plataforma: ")
                nuevo = Videojuego(cod, tit, gen, plat)
                catalogo.agregar_videojuego(nuevo)
                
            elif opcion == 2:
                catalogo.listar_catalogo()
                
            elif opcion == 3:
                cod = input("Ingrese el código a buscar: ")
                juego = catalogo.buscar_por_codigo(cod)
                if juego:
                    juego.mostrar_informacion()
                else:
                    print("Videojuego no encontrado.")
                    
            elif opcion == 4:
                tit = input("Ingrese el título (o parte de él) a buscar: ")
                resultados = catalogo.buscar_por_titulo(tit)
                if resultados:
                    print("\n--- RESULTADOS DE BÚSQUEDA ---")
                    for j in resultados:
                        j.mostrar_informacion()
                else:
                    print("No se encontraron videojuegos con ese título.")
                    
            elif opcion == 5:
                cod = input("Ingrese el código del videojuego: ")
                juego = catalogo.buscar_por_codigo(cod)
                if juego:
                    horas = int(input("Ingrese las horas jugadas a sumar: "))
                    juego.sumar_horas(horas)
                else:
                    print("Videojuego no encontrado.")
                    
            elif opcion == 6:
                cod = input("Ingrese el código del juego a completar: ")
                juego = catalogo.buscar_por_codigo(cod)
                if juego:
                    juego.marcar_completado()
                else:
                    print("Videojuego no encontrado.")
                    
            elif opcion == 7:
                catalogo.mostrar_estadisticas()
                
            elif opcion == 0:
                print("Saliendo del programa. ¡Hasta luego!")
                break
            else:
                print("Opción inválida. Intente de nuevo.")
                
        except ValueError:
            print("Error: Por favor, ingrese un valor numérico válido.")

if __name__ == "__main__":
    main()