# conditional statement excdption handling

try:
    num = int (input("Enter a number: "))
    assert num%2 ==0
except:
    print("not an even number")
else:
    reciprocal = 1/num
    print(reciprocal)