def linearsearch(array,n,x):
    for i in range(0,n):
        if array[i]==x:
            return i
    return -1
array=[1,5,8,9,10,12,3]
x=int(input("Enter the Input: "))
n=len(array)
result=linearsearch(array,n,x)
if(result==-1):
    print("Element not found")
else:
    print("Element is found",result,x)