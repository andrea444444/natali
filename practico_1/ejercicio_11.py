from time import localtime
t =  localtime ()
t.tm_mday
t.tm_mon
t.tm_year
print("Ingrese su fecha de nacimiento")
dia = int(input("Día: "))
mes = int(input("Mes: "))
anno = int(input("Año: "))
if dia<t.tm_mday:
    dia = 0
else:
    dia = 1
if mes+dia<t.tm_mon:
    mes = 0
else :
    mes = 1
print(t.tm_year-(anno+mes))