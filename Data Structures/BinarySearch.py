def BinarySearch(array,x,low ,high):
    while low <= high:
        mid = low + (high - low) // 2    
        if array[mid]==x:
            return mid 
        elif array[mid]<x:
            low =mid+1
            
        else:
            high=mid-1       
    return -1
array =[3,4,5,6,7,8,9]
x=int(input("Enter the Input: "))
result=BinarySearch(array,x,low = 0 ,high = len(array) - 1)
if (result==-1):
    print("Element not found")
else:
    print("Element is found",result)
    