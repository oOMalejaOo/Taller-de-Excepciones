#Programa que valide correo electrónico.

def validar_correo(correo):

    try:
        if "@" not in correo:
            raise ValueError("El correo electrónico debe contener el símbolo @")
        
        if "." not in correo:
            raise ValueError("El correo electrónico debe contener un punto")
        
        partes= correo.split("@")

        if len(partes) != 2:
            raise ValueError("El correo electrónico debe contener exactamente un símbolo @")
        
        usuario, dominio = partes

        if usuario == "" or dominio == "":
            raise ValueError("Usuario o dominio no pueden estar vacíos")
        
        print("Correo válido")

    except ValueError as e:
        print(f"Error: {e}")

correo = input("Ingrese un correo electrónico: ")
validar_correo(correo)