l=[2,3,2]
x=[]
f=0
last=0
for i in range(len(l)):
    for j in range(i+1,len(l)):
        if j!=i+1:
                x.append(l[i]+l[j])
                f=i
                last=j
print("output:",max(x))
print("house robbed is ",f," and ",last)
