# def anangrams(s, arr):
#     a = []
#     char = sorted(s)
#     for i in range(len(arr)):
#         sort_Word = sorted(arr[i])
#         if char == sort_Word:
#             a.append(sort_Word)
    
#     if len(a) > 0:
#         print(f"The following strings are anagrams of '{s}':")
#         for anagram in a:
#             print(anagram)
#     else:
#         print(f"No anagrams of '{s}' found in the list.")
            

# anangrams('lead', ['deal', 'peal', 'dale'])

def anagrams(s, arr):
    anagram_dict = {}    
    for char in s:
        if char in anagram_dict:
            anagram_dict[char] += 1
        else:
            anagram_dict[char] = 1
    
    anagram_list = []

    for word in arr:
        c = anagram_dict.copy()
        if len(word) == len(s):
            for j in range(len(word)):
                if word[j] in c:
                    c[word[j]] -= 1
                else:
                    break
            else:
                anagram_list.append(word)
    
    return anagram_list

# Test the function
s = 'lead'
arr = ['deal', 'peal', 'dale', 'apple', 'lead']
anagram_list = anagrams(s, arr)
print(anagram_list)

    
