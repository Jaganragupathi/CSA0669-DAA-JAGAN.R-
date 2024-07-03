def number(num,k):
    n=len(num)
    c=0
    for i in range(n):
        for j in range(i+1,n):
            if num[i]==num[j] and (i*j)%k==0:
                c=c+1
    return c
num=[3,1,2,2,2,1,3]
k=2
print(number(num,k))
