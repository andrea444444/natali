numero = str(input("Ingrese un número: "))
log = len(numero)
log = log - 1
numero_invertido = ""
for i in range(log, -1, -1):
    numero_invertido = numero_invertido + numero[i]
num2 = numero_invertido
if numero == num2:
    print("Es capicua.")
else:
    print("No es capicua.")