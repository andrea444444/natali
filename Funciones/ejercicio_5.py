def pal_inv(pal):
    log = len(pal)
    log = log - 1
    pal_invertida = " "
    for i in range(log, -1, -1):
        pal_invertida = pal_invertida + pal[i]
    print(pal_invertida)


pal = input("Ingrese carácter: ")
pal_inv(pal)
