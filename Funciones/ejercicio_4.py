def vocal(pal):
    vocales = "aeiouAEIOU"
    if pal in vocales:
        print("true")
    else:
        print("false")


pal = input("Ingrese carácter: ")
vocal(pal)