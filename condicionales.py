edad = int(input("¿Qué edad tienes?"))

#*Condicional If - Else

if edad >= 18:
    print("Puedes entrar")
elif edad >= 15:
    print("Puedes entrar con un adudlto")
else:
    print("No puedes entrar")



#?Switch case
comando = "reiniciar"
match comando:
case "iniciar":
print("Arrancando el sistema...")
case "apagar":
        print("Apagando el sistema")    
