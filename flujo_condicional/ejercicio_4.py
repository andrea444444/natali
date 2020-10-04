consumo = int(input("¿Cuál fue su consumo?: "))
if consumo <= 100 :
    print("El precio es 1.00")
elif consumo > 100 and consumo <= 499 :
    print("El precio es 1,20")
elif consumo > 499 and consumo <= 999 :
    print("El precio es 1.50")
else :
    print("El precio es 2,00")