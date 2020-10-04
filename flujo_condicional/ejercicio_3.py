partido_1 = "A"
partido_2 = "B"
print(f"{partido_1} o {partido_2}")
mensaje = input("Ingrese el partido por el cual votará: ")
if mensaje == partido_1:
    print(f"Usted ha votado por el partido {partido_1}")
elif mensaje == partido_2:
    print(f"Usted ha votado por el partido {partido_2} ")
else:
    print("Voto invalido")


