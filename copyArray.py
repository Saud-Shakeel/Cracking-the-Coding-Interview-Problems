def copy_array(array):
    copy = []
    for value in array:
        copy = append_new(copy,value)
    return copy

def append_new(array,value):
    bigger = array.copy()
    bigger.append(value)
    return bigger

original_array = [1,2,3,4,5,6]
print(copy_array(original_array))


