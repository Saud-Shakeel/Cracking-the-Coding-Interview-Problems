# def uniqueArray(s):
#     dictt = {}
#     for ch in s:
#         if ch in dictt:
#             return False
#         else:
#             dictt[ch] =1
#     return True

# print(uniqueArray('abc'))

def sortedUniqueArray(s):

    s_list = list(s)
    s_list.sort()
    sorted = ''.join(s_list)

    prev = None
    for ch in sorted:
        if prev==ch:
            return False
        prev = ch
    return True

print(sortedUniqueArray('abcbd'))