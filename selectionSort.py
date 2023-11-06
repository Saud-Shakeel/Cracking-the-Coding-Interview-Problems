def selectionSort(arr):
    print(arr)
    for i in range(len(arr)-1):
        mini = arr.index(min(arr[i:]))

        if arr[i] > arr[mini]:
            arr[i], arr[mini] = arr[mini], arr[i]
    return arr

sel = selectionSort([7,3,1,4,8])
print(sel)