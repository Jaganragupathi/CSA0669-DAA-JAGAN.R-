a=[5,3,9,8,7,1]
n=len(a)
for i in range(n-1):
    for j in range(i+1,n):
        if a[i]>a[j]:
            temp=a[i]
            a[i]=a[j]
            a[j]=temp
print(a)

