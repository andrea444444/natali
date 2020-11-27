pos = int(input("Ingrese tamaño del vector: "))
numero = int(input("Ingrese un número: "))
arrayA = []

arrayB = []
import random
for i in range(0, pos):
    num = random.randint(0, 300)
    arrayA.append(num)
print(arrayA)
for i in arrayA:
    numB = str(i)
    if numB[len(numB)-1] == str(numero):
        arrayB.append(numB)
print(arrayB)
