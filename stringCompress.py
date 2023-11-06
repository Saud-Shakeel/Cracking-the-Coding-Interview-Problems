def stringCompression(s):
    curr = s[0]
    count = 1
    comp_str = ''
    for i in range(len(s)):
        if s[i]== curr:
            count+=1
        else:
            comp_str += curr + str(count)
            count = 1
            curr = s[i]
    comp_str += curr + str(count)

    if len(s)==len(comp_str):
        return s
    return comp_str

print(stringCompression('aabcccccdaa'))