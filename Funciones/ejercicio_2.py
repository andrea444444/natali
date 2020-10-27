def max_3(num,num2,num3):
    if num > num2 and num >num3:
        print(num)
    elif num2 > num and num2 >num3:
        print(num2)
    elif num3 > num2 and num3 >num:
        print(num3)
    else:
        print("Son iguales")
max_3((int(input("Número 1: "))),(int(input("Número 2: "))),(int(input("Número 3: "))))