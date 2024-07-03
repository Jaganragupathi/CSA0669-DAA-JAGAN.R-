a=[1,2,15,4,10,6,7,9]
h=8                                                       
for i in range(0,h):
    min=a[0]
    max=a[0]
    if min>a[i]:
        min=a[i]
for i in range(0,h):        
    if max<a[i]:
        max=a[i]
print(min)
print(max)
