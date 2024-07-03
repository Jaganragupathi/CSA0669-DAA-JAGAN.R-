arr=[1,65,3,4,5]
n=len(arr)
for i in range(n-1):
    min=i
    for j in range(i+1,n):
        if arr[j]<arr[min]:
            min=j
    if(min!=i):
        temp=arr[min]
        arr[min]=arr[i]
        arr[i]=temp
print(arr)
