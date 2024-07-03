a=[1,2,3,1]
maxi=a[0]
index=0
for i in range (0,len(a)):
    if a[i]>maxi:
        maxi=a[i]
        index=i
print(index)
