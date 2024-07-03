def merge_sort(arr):
    if len(arr) <= 1: return arr
    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])
    return merge(left_half, right_half)
def merge(left, right):
    sorted_arr = []
    while left and right:
        sorted_arr.append((left if left[0] <= right[0] else right).pop(0))
    return sorted_arr + left + right
arr = [5, 2, 9, 1, 5, 6]
sorted_arr = merge_sort(arr)
print(sorted_arr)
