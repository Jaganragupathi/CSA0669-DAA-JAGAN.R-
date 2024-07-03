def insertion(arr):
    for j in range(0,len(arr)):
        key=arr[j]
        i=j-1
        while i>=0 and arr[i]>key:
            arr[i+1]=arr[i]
            i=i-1
            arr[i+1]=key
arr=[10,31,20,20,2,2,2]
insertion(arr)
print(arr)
