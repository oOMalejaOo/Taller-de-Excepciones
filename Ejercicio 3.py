#Programa que reciba una fecha de nacimiento y arroje la edad de la persona.

from datetime import date

try:
    # Pedir datos
    dia = int(input("Ingrese el día: "))
    mes = int(input("Ingrese el mes: "))
    anio = int(input("Ingrese el año: "))

    # Fecha actual
    hoy = date.today()

    # Calcular edad básica
    edad = hoy.year - anio

    # Verificar si ya cumplió años
    if mes > hoy.month:
        edad -= 1
    elif mes == hoy.month and dia > hoy.day:
        edad -= 1

    print("Tu edad es:", edad)

except:
    print("Error, datos inválidos")
