peso = float(input("¿Cuátos kg pesa?"))
altura = float(input("¿Cuántos metros mide?"))
imc = peso / altura ** 2
imc = round(imc, 2)
f"Tu índice de masa corporal es {imc}"
print(f"Tu índice de masa corporal es {imc}")