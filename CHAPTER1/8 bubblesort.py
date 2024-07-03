num=[3,2,1,6,9,7,5,4]
n=len(num)
for i in range(0,n):
        for j in range(i+1,n):
            if num[i]>num[j]:
                num[i],num[j]=num[j],num[i]
print(num)
