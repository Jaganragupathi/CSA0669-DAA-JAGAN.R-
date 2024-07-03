def ic(nums1, nums2):
    s1 = set(nums1)
    s2 = set(nums2)
    
    a1 = sum(1 for num in nums1 if num in s2)
    a2 = sum(1 for num in nums2 if num in s1)
    
    return [a1, a2]

nums1 = [2, 3, 2]
nums2 = [2, 1]
print(ic(nums1, nums2))
