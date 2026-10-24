class Vehiculo:
    def __init__(self, marca: str, modelo: str, color: str):
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.velocidad = 0      
        self.encendido = False  

    def encender(self):
        if not self.encendido:
            self.encendido = True
            print(f"El {self.marca} {self.modelo} {self.color} se ha encendido.")
        else:
            print("El vehículo ya está encendido.")

    def acelerar(self, incremento: int = 10):
        if self.encendido:
            self.velocidad += incremento
            print(f"Acelerando... Velocidad actual: {self.velocidad} km/h")
        else:
            print("No puedes acelerar, el vehículo está apagado.")

    def frenar(self, decremento: int = 10):
        if self.encendido:
            self.velocidad = max(0, self.velocidad - decremento)
            print(f"Frenando... Velocidad actual: {self.velocidad} km/h")
        else:
            print("El vehículo está apagado.")

    def apagar(self):
        if self.encendido:
            self.encendido = False
            self.velocidad = 0
            print(f"El {self.marca} {self.modelo} se ha apagado.")
        else:
            print("El vehículo ya está apagado.")


if __name__ == "__main__":
    mi_auto = Vehiculo(marca="Toyota", modelo="Corolla", color="Rojo")
    
    mi_auto.encender()
    mi_auto.acelerar(30)
    mi_auto.frenar(10)
    mi_auto.apagar()