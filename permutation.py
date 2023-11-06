def perm(s, pref):
    if len(s)==0:
        print(pref)
    else:
        for i in range(len(s)):
            rem = s[0:i]+s[i+1:]
            perm(rem,pref+s[i])

perm('xyz','')
