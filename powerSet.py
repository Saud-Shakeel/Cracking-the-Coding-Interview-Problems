def powerSet(arr):
    if not arr:
        return [[]]

    first_elem = arr[0]
    rest_of_elems = arr[1:]
    
    subsets_without_first = powerSet(rest_of_elems)
    
    subsets_with_first = []
    for subset in subsets_without_first:
        subsets_with_first.append([first_elem] + subset)
    
    return subsets_without_first + subsets_with_first

result = powerSet([1, 2, 3,4])
print(result)
