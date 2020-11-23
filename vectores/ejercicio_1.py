
vectorFact=[]
for i in range (1,21):
    vectorFact.append(i)

for n in vectorFact:
    num = n
    multiplicacion = 1
    for i in range (1,n+1):
        multiplicacion= multiplicacion * i
    print(f"Factorial de {i}: {multiplicacion}")

