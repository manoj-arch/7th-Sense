row = int(input("Enter the value:" ))
ascii_value = 65

for i in range(row):
    for j in range(i+1):
        alpha = chr(ascii_value)
        print(alpha,end="")
        ascii_value += 1
    print()