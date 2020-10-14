n = int(input("n: "))
pi = 4
suma = 0
for i in range(1,n+1):
    if i%2 == 0:
        signo = -1
    else :
        signo = 1
    resultado = signo/(1+2*(i-1))
    suma = suma + resultado
pi = pi * suma
print(pi)