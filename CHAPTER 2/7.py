haystack="codeleet"
needle="leet0"
l1=len(haystack)
l2=len(needle)
flag=0
for i in range(0,l1,l2):
    if haystack[i:i+l2]==needle:
        print(i)
        flag=1
        break
if flag==0:
    print("-1")
