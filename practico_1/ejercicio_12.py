num = int(input("cantidad de palabras: "))
pal_mas_larga = ""
pal_mas_corta = "                                            "
for i in range (1,num+1):
    pal = str(input("cantidad de palabras: "))
    if len(pal)>len(pal_mas_larga):
        pal_mas_larga = pal
    elif len(pal)<len(pal_mas_corta):
        pal_mas_corta = pal
print(f"La palabra más larga es: {pal_mas_larga}")
print(f"La palabra más corta es: {pal_mas_corta}")

