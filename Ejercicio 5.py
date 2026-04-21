#Programa que guarde en un archivo.txt diez palabras.


try:
    archivo = open("palabras.txt", "w")

    for i in range(10):
        palabra = input(f"Ingrese la palabra {i+1}: ")
        archivo.write(palabra + "\n")

    archivo.close()
    print("Palabras guardadas correctamente")

except:
    print("Error al guardar el archivo")