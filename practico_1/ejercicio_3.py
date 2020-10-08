divisor = int(input("Ingrese un divior por favor: "))
dividendo = int(input("Ingrese un divisor por favor: "))
division = divisor // dividendo
resto = divisor % dividendo
if resto==0:
    print("La división es exacta")
    print(f"cociente: {division}")
    print("Resto: 0")
else:
    print("La división no es exacta")
    print(f"cociente: {division}")
    print(f"Resto: {resto}")