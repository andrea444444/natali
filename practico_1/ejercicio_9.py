num_1 = int(input("Operando: "))
signo = input("Operador: ")
num_2 = int(input("Operando: "))
if signo == "+":
    print(f"{num_1}  +  {num_2}  =  {num_1+num_2}")
elif signo == "-":
    print(f"{num_1}  -  {num_2}  =  {num_1-num_2}")
elif signo == "*":
    print(f"{num_1}  *  {num_2}  =  {num_1*num_2}")
elif signo == "/":
    print(f"{num_1}  /  {num_2}  =  {num_1/num_2}")
elif signo == "**":
    print(f"{num_1}  **  {num_2}  =  {num_1**num_2}")