num = int (input("Enter the Number: "))
flag=0

if num==1:
    print(num,"is not  prime")
elif num > 1:
    for i in range(2,num):
        if(num % 2 == 0):
            flag=1
            break
    if flag:
        print("is not prime number: ",num)
    else:
        print("is  prime number: ",num)