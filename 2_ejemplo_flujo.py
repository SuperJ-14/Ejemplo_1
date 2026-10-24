def solicitar_entero_positivo(mensaje):
    while True:
        entrada = input(mensaje).strip()
        try:
            valor = int(entrada)
            if valor > 0:
                return valor
            print("Error: ingrese un entero mayor que cero.")
        except ValueError:
            print("Error: ingrese únicamente números enteros.")


cantidad = solicitar_entero_positivo("Cantidad de productos: ")
print(f"Cantidad ingresada: {cantidad}")
