num = int(input("Duración de tramo: "))
suma = 0
while num > 0 :
    suma = num + suma
    num = int(input("Duración de tramo: "))
hora = suma // 60
minutos = suma % 60
if minutos<10:
    print(f"Tiempo tola de viaje: {hora}:0{minutos}")
else:
    print(f"Tiempo tola de viaje: {hora}:{minutos}")