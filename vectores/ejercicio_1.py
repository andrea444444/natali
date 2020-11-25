def FACT(vectorFact):
    for n in vectorFact:
        num = n
        multiplicacion = 1
        for i in range (1,n+1):
            multiplicacion= multiplicacion * i
        print(f"Factorial de {i}: {multiplicacion}")

vectorFact=[]
for i in range (1,21):
    vectorFact.append(i)
FACT(vectorFact)