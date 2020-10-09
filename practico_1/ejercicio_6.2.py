num_1 = int(input("Ingrese el primer número por favor: "))
num_2 = int(input("Ingrese el segundo número por favor: "))
num_3 = int(input("Ingrese el tercer número por favor: "))
if num_1<num_2 and num_1<num_3:
    if num_3>num_2:
        print(num_1, num_2, num_3)
    elif num_3<num_2:
        print (num_1, num_3, num_2)
elif num_2<num_1 and num_2<num_3:
    if num_3>num_1:
        print(num_2, num_1, num_3)
    elif num_3<num_1:
        print (num_2, num_3, num_1)
elif num_3<num_1 and num_3<num_2:
    if num_2>num_1:
        print(num_3, num_1, num_2)
    elif num_2<num_1:
        print (num_3, num_2, num_1)

