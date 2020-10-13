peso = float(input("¿Cuátos kg pesa?"))
altura = float(input("¿Cuántos metros mide?"))
edad = float(input("¿Cuál es su edad?"))
imc = peso / altura ** 2
imc = round(imc, 2)
if imc<22.0 and edad<45:
    print("Su condición de riesgo es baja")
if imc<22.0 and edad>=45:
    print("Su condición de riesgo es media")
if imc>=22.0 and edad>=45:
    print("Su condición de riesgo es alta")
if imc>=22.0 and edad<45:
    print("Su condición de riesgo es media")

