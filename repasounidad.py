class Cuenta:
    def __init__(self, saldo):
        self.__saldo = saldo


    def obtener_saldo(self):
        return self.__saldo

    def set_saldo(self, nuevo_saldo):
        if(nuevo_saldo > 0):
            self.__saldo += nuevo_saldo
            print("Su saldo ha sido acreditado, saldo actual Q." \
            "{self.__saldo}")
        else:
            print("El valor debe ser mayor a 0")



def validar_edad():
    return 0<= edad <= 120

try:
    numero = in(Input("Ingrese un numero: "))
except ___:
    print('Debe ingresar un numero valido')
finally:
    print("Termino de ejecutar el try o except")