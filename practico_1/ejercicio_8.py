num_1 = int(input("Ingrese un número por favor: "))
num_2 = int(input("Ingrese un número por favor: "))
suma = 0
for i in range (num_1+1, num_2):
    suma = i + suma
print(f"La suma es: {suma}")