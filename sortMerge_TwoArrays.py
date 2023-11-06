def sortMerge(a, b):
    i = len(a) - len(b) - 1
    j = len(b) - 1
    k = len(a) - 1

    while i >= 0 and j >= 0:
        if a[i] > b[j]:
            a[k] = a[i]
            i -= 1
        else:
            a[k] = b[j]
            j -= 1
        k -= 1

    return a

arr1 = [24, 34, 48, 0, 0, 0]
arr2 = [27, 36, 50]
merged = sortMerge(arr1, arr2)
print(merged)

