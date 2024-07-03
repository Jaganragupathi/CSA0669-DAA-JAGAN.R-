arr=[1,2,3,4]
k=2
f=0
n=1
c=0
while f==0:
    if n not in arr:
        c+=1
    if c==k:
        print(n)
        f=1
    n+=1
