def perm_palindrome(s):
    my_dict = {}
    for i in range(len(s)):
            if s[i] in my_dict:
                my_dict[s[i]] +=1
            else:
                my_dict[s[i]] = 1
    print(my_dict)

    if len(s) %2 == 0:
        for even_count in my_dict.values():
            if even_count % 2 ==0:
                return True
        return False 
    else:
        odd_count = 0
        for count in my_dict.values():
            if count %2 !=0:
                odd_count +=1
        if odd_count ==1 or count ==0:
            return True
        return False           
             

print(perm_palindrome('ssssaaaa'))

