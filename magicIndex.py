def magicIndex(arr, left, right):
    if left > right:
        return None

    mid = (left + right) // 2
    mid_value = arr[mid]
    if mid_value == mid:
        return mid
    
    left_result = magicIndex(arr, left, min(mid-1, mid_value))
    if left_result is not None:
        return left_result
    
    return magicIndex(arr, max(mid+1, mid_value), right)

array = [-4, -3, 20, -1, 4, 4, 78]
result = magicIndex(array, 0, len(array) - 1)
print(result)
