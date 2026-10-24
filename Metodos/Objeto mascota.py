class Mascota:
    def __init__(self, nombre, especie, edad, energia: str=60):
        self.nombre = nombre
        self.especie = especie
        self.edad = edad
        self.energia = energia

    def mostrar_datos(self):
        print(f"El nombre es: {self.nombre}, Especie: {self.especie}, Edad {self.edad} años y su energía: {self.energia}")

    def jugar(self):
        self.energia = max(0, self.energia - 10)
        print(f"{self.nombre} jugó (-10 de energía). Energía actual: {self.energia}")

    def dormir(self):
        self.energia += 20
        print(f"{self.nombre} durmio (+20 de energía). Energía actual: {self.energia}")

    def cumplir_anios(self):
        self.edad += 1
        print(f"{self.nombre} cumplio años (+1 año). Edad actual: {self.edad}")

informacion_mascota = Mascota(nombre="Bobi", especie="Perro", edad=2)

informacion_mascota.mostrar_datos()
informacion_mascota.jugar()
informacion_mascota.dormir()
informacion_mascota.cumplir_anios()
