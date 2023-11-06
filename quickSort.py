def quickSort(arr):
    if len(arr) <=1:
        return arr
    else:
        pivot = arr[-1]

        greater_elements = [x for x in arr[:-1] if x > pivot]
        lesser_elements = [x for x in arr[:-1] if x <= pivot]
       
        return quickSort(lesser_elements) + [pivot]  + quickSort(greater_elements)
       

quick = quickSort([7,9,3,6,1,4])
print(quick)