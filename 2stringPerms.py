# def isPerm(str1,str2):
#     d1 = {}
#    
#     if len(str1) != len(str2):
#         return False
    
#     for i in range(len(str1)):
#         if  str1[i] in d1:
#             d1[str1[i]] =+ 1
#         else:
#             d1[str1[i]] =1

#     d2 = {}

#     for i in range(len(str2)):
#         if  str2[i] in d2:
#             d2[str2[i]] =+ 1
#         else:
#             d2[str2[i]] =1

#     for i in d1:
#         if i not in d2 or d1[i] != d2[i]:
#             return False
        
#     return True
    
# print(isPerm('axbcd','dcbaz'))

def isPerm(str1,str2):

    if len(str1) != len(str2):
        return False
    
    s1=''.join(sorted(str1))
    s2=''.join(sorted(str2))
    print(s1,s2)
    
    for i in range(len(str1)):        
        if s1[i] != s2[i]:
            return False
    return True

print(isPerm('xuio','xuio'))

