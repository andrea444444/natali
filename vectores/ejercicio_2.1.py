vectorA = []
vectorB = []
for i in range(0,5):
    num = int(input("Ingrese un número para el vector A: "))
    vectorA.append(num)
for i in range(0,5):
    num2 = int(input("Ingrese un número para el vector B: "))
    vectorB.append(num2)
vectorSuma = []
for i in range (0,5):
    suma = vectorA[i]+vectorB[i]
    print(f"El vector suma del componente {i+1} es : {suma}")
    vectorSuma.append(suma)
print(vectorSuma)