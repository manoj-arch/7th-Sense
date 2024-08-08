year = int(input("Enter the year: "))

if (year % 400 ==0) and (year % 100 == 0):
    print("is a leap year",format(year))
elif(year % 4 == 0) and (year % 100 != 0):
    print("Is a leap year:",format(year))
else:
    print("Not a leap year",format(year))        
