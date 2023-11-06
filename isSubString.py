def subString(s1,s2):
    s1 = str.lower(s1+s1)
    if s2 in s1:
        print('Substring')
    else:
        print('Not Substring')
    
subString('WATERBOTTLE','bottlewater')