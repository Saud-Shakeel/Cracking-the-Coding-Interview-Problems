def longestPrefix(strs):
    if not strs:
        return None
    
    common_Pref = ''
    pref_len = len(min(strs))
    
    for i in range(pref_len):
        char = strs[0][i]
        for s in strs[1:]:
            if s[i] != char:
                return common_Pref
        common_Pref += char    
    return common_Pref           


arr = ['flower','flow','flight']
print(longestPrefix(arr))
