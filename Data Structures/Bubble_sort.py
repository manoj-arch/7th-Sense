def Bubblesort(arr):
    for i in range(len(arr)):
        for j in range(0,len(arr)-i-1):
            if arr[j] > arr[j+1]:
                temp=arr[j]
                arr[j]=arr[j+1]
                arr[j+1]=temp
        return arr
arr =[1,10,2,7,3,8]
result=Bubblesort(arr)
print("Sorted Array is: ",result)


                
        