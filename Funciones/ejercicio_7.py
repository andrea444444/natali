def generar_n_caracteres(num):
    caracter = ""
    for i in range (1,num+1):
        i = "x"
        caracter = caracter + i
    print(caracter)


num = int(input("Número: "))
generar_n_caracteres(num)