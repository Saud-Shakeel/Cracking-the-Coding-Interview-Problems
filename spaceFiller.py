def emptySpace(s, truelen):
    str_list = list(s)
    strlen = len(s)   
    for i in range(truelen-1 , -1, -1):
        if s[i] == ' ':
            str_list[strlen - 1] = '0'
            str_list[strlen - 2] = '2'
            str_list[strlen - 3] = '%'
            strlen -= 3
        else:
            str_list[strlen - 1] = s[i]
            strlen -= 1
            
    modified_str = ''.join(str_list)
    return modified_str

print(emptySpace('Mr John Smith    ', 13))
