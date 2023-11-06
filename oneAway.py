def oneAway(str1, str2):
    l1 = len(str1)
    l2 = len(str2)

    if l1 == l2:
        count = 0
        for i in range(len(str1)):
            if str1[i] != str2[i]:
                count += 1
                if count > 1:
                    return False
               
        return True
    
    elif len(str1) - 1 == len(str2) or len(str2) - 1 == len(str1):
        big = str2
        j = 0
        count = 0
        if len(str1) > len(str2):
            big = str1
        for i in range(len(big)):
            if big == str1:
                if str1[i] == str2[j]:
                    if j < len(str2) - 1:
                        j += 1
                else:
                    count += 1
            else:
                if str2[i] == str1[j]:
                    if j < len(str1) - 1:
                        j += 1
                else:
                    count += 1
        if count == 1 or count == 0:
            return True
    return False

    
print(oneAway('palees', 'paleee'))

