#Programa que haga el calculo de una nómina, reciba un sueldo y calcule el pago de 15 días trabajados, calculando también el auxilio de transporte.


try:
    sueldo = float(input("Ingrese su sueldo mensual: "))

    salario_minimo = 1300000
    auxilio = 162000

    pago_15 = (sueldo / 30) * 15

    if sueldo <= 2 * salario_minimo:
        auxilio_15 = (auxilio / 30) * 15
    else:
        auxilio_15 = 0

    total = pago_15 + auxilio_15

    print("Pago por 15 días:", pago_15)
    print("Auxilio de transporte:", auxilio_15)
    print("Total a pagar:", total)

except:
    print("Error: dato inválido")