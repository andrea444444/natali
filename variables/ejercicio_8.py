inversion = int(input("Mónto a invertir:"))
interes = float(input("Interés anual: "))
numero_de_años = int(input("Número de años a invertir: "))
ganancia_neta_por_inversion = inversion * (1 + interes) ** numero_de_años
print(f"La ganancia neta originada por la inversión es: {ganancia_neta_por_inversion}")