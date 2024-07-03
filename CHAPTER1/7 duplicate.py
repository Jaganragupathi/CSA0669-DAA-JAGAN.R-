def unique(n):
    a = set()
    for i in n:
        if i not in a:
            a.add(i)
    return a
n = [3, 7, 3, 4, 5, 2, 2, 7, 6]
print(unique(n))

    
