horas = int(input("¿Cuántas horas trabajó?"))
pago_x_hora = float(input("Ingrese paga por hora:"))
pago_total = horas * pago_x_hora
mensaje = "monto total a pagar" + str(pago_total)
print(mensaje)