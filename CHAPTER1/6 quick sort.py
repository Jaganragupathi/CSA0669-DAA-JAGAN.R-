def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return quicksort(left) + middle + quicksort(right)
def find_max_element(arr):
    if not arr:
        return "The list is empty."
    sorted_arr = quicksort(arr)
    return sorted_arr[-1]
numbers = []  
numbers = [5,4,2,3,1]
print(quicksort(numbers))
print(find_max_element(numbers))
 
