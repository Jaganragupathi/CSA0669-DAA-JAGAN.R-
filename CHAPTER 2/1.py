a=[-5,-1,-3,-2,-4]
if len(a)==0:
    print("[]")
else:
    for i in range(len(a)):
        for j in range(len(a)):
            if a[j]>a[i]:
                temp=a[i]
                a[i]=a[j]
                a[j]=temp
    print(a)
