def palindromo(pal):
    log = len(pal)
    log = log - 1
    pal_invertida = ""
    for i in range(log, -1, -1):
        pal_invertida = pal_invertida + pal[i]
    pal2 = pal_invertida
    if pal == pal2 :
        print("true")
    else:
        print("false")

pal = input("Ingrese palabra: ")
palindromo(pal)