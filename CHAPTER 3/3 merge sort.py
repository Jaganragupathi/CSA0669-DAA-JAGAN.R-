def m(a):
    n=len(a)
    if n<=1:
        return a
    i,j=0,0
    mid =n//2
    l=m(a[:mid])
    r=m(a[mid:])
    b=[]
    while i<len(l) and j<len(r):
        if l[i]<r[j]:
            b.append(l[i])
            i=i+1
        else:
            b.append(r[j])
            j=j+1
    while i<len(l):
        b.append(l[i])
        i=i+1
    while j<len(r):
        b.append(r[j])
        j=j+1
    return b
arr=[12,23,45,1,2,3,6,8,9]
print(m(arr))
"""
def m(a, comparison_count=0):
    n = len(a)
    if n <= 1:
        return a, comparison_count

    mid = n // 2
    l, comparison_count = m(a[:mid], comparison_count)
    r, comparison_count = m(a[mid:], comparison_count)

    i, j = 0, 0
    b = []
    while i < len(l) and j < len(r):
        comparison_count += 1  # Count each comparison
        if l[i] < r[j]:
            b.append(l[i])
            i += 1
        else:
            b.append(r[j])
            j += 1

    while i < len(l):
        b.append(l[i])
        i += 1

    while j < len(r):
        b.append(r[j])
        j += 1

    return b, comparison_count

# Example usage
arr = [12, 4, 78, 23, 45, 67, 89, 1]
sorted_arr, total_comparisons = m(arr)
print("Sorted array:", sorted_arr)
print("Total comparisons:", total_comparisons)
"""
