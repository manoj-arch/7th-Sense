num = int(input("Enter the value: "))

def palindrome():
    temp = num
    rev= 0
    while temp > 0:
        rem = temp % 10
        rev = (rev * 10) + rem
        temp = temp // 10
    if num == rev:
        print("Is prime number")
    else:
        print("Is not prime number")
palindrome()  

