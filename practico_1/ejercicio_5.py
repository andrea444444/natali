palabra_1 = input("Palabra 1: ")
palabra_2 = input("Palabra 2: ")
resta = len(palabra_2) - len(palabra_1)
resta_2 = len(palabra_1) - len(palabra_2)
if len(palabra_1)<len(palabra_2):
    print(f"La palabra {palabra_2} tiene {resta} letras más que {palabra_1}")
elif len(palabra_2)<len(palabra_1):
    print(f"La palabra {palabra_1} tiene {resta_2} letras más que {palabra_2}")
else :
    print("Tienen el mismo número de letras")

