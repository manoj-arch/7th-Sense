rows = int(input("Enter the rows: "))
k = 0

for i in range(1,rows+1):
    for space in range(1,(rows-i)+1):
        print(end="  ")
    while k!=(2*i-1):
        print("*",end=" ")
        k+=1
    k=0
    print()
    
rows = int(input("Enter the rows: "))
k = 0

for i in range(1,rows+1):
    for space in range(1,(rows-i)+1):
        print(end="  ")
    for num in range(1, 2*i):
        print(num, end=" ")
    print()
