class Termometro:
    def __init__(self, ubicacion, temperatura_inicial: float=0.0,):
        self.ubicacion = ubicacion
        self.temperatura = max(0.0, float(temperatura_inicial))

    def mostrar_temperatura(self):
        print(f"Temperatura en {self.ubicacion}: {self.temperatura}°C")

    def aumentar_temperatura(self, grados: float):
        if grados > 0:
            self.temperatura += grados

    def disminuir_temperatura(self, grados: float):
        if grados > 0:
            self.temperatura = max(0.0, self.temperatura - grados)

termometro_aula = Termometro(ubicacion="Aula", temperatura_inicial=20.0)

termometro_aula.mostrar_temperatura()
termometro_aula.aumentar_temperatura(2)
termometro_aula.mostrar_temperatura()
termometro_aula.disminuir_temperatura(3)
termometro_aula.mostrar_temperatura()
        