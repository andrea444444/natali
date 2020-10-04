año = int(input("Ingrese año: "))
if año % 4==0 or (año % 100==0 and año % 400==0):
    print("El año es bisiento")
else:
    print("El año no es bisiesto")