num = int(input("n: "))
while num > 1:
    if num%2==0:
        num_1 = num // 2
        print(num)
        num = num_1
    else :
        num_1 = (num*3)+1
        print(num)
        num = num_1
print(1)

