def distinct(nums):
    n=len(nums)
    sum=0
    for i in range(n):
        for j in range(i,n):
            sub=nums[i:j+1]
            c=len(set(sub))
            sum=sum+c**2
    return sum
nums=[1,2,1]
r=distinct(nums)
print(r)

