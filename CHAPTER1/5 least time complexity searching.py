def search(nums,target):
    if target in nums:
        return nums.index(target)
nums=[1,2,3,4,5]
target=5
print(search(nums,target))
