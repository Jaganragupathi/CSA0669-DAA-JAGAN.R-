def largeGroupPositions(s):
    result = []
    i = 0
    while i < len(s):
        count = 1
        while i + 1 < len(s) and s[i] == s[i + 1]:
            count += 1
            i += 1
        if count >= 3:
            result.append([i - count + 1, i])
        i += 1
    return result
s = "abbxxxxzzy"
print(largeGroupPositions(s))
