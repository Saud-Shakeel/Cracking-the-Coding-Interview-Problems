def parens(n):
    if n == 1:
        return ['()']
    
    paren_list = parens(n-1)
    print(paren_list)
    new_list = set()
    for i in range(len(paren_list)):
        new_list.add(paren_list[i]+ '()')
        new_list.add('(' + paren_list[i] + ')')
        new_list.add('()' + paren_list[i])
    return list(new_list)

print(parens(2))