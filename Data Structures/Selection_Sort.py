def selectionsort(arr,size):
    for i in range(size):
        minindex=i
        for j in range(i+1,size):
            if(arr[j]<arr[minindex]):
                minindex=j
        arr[i],arr[minindex]=arr[minindex],arr[i]
data = [2,1,8,5,10,12,9,15,3]
size=len(data)
selectionsort(data,size)
print(data)


