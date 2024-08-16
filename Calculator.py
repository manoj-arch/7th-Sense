num1 = int(input("Enter the input 1: "))
num2 = int(input("Enter the input 2: "))

choice = int(input("Enter your choice (1 for addition, 2 for subtraction,3 for multiplication, 4 for division): "))

if choice == 1:
    result=num1 + num2
elif choice == 2:
    result=num1 - num2
elif choice == 3:
    result=num1*num2
elif choice == 4:
    result=num1/num2
elif choice == 5:
    print("Break the Operations:")
else:
\
    print("The output is : ", result )
