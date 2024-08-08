num = int (input("Enter the Number: "))
flag = False

if num==1:
    print(num,"is not  prime")
elif num > 1:
    for i in range(2,num):
        if(num % 2 == 0):
            flag = True
            break
    if flag:
        print("is not prime number: ",num)
    else:
        print("is  prime number: ",num)