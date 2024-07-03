def m(a, count=0):
    n = len(a)
    if n <= 1:
        return a, count
    mid = n // 2
    l, count = m(a[:mid], count)
    r, count = m(a[mid:], count)
    i, j = 0, 0
    b = []
    while i < len(l) and j < len(r):
        count += 1  
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
    return b, count
arr = [12, 4, 78, 23, 45, 67, 89, 1]
sorted_arr, total = m(arr)
print("Sorted array:", sorted_arr)
print("Total comparisons:", total)
