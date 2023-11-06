# ou are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.

# Return the merged string.

 

# Example 1:

# Input: word1 = "abc", word2 = "pqr"
# Output: "apbqcr"
# Explanation: The merged string will be merged as so:
# word1:  a   b   c
# word2:    p   q   r
# merged: a p b q c r

def mergedStrings(str1,str2):
    merged_string = ''
    l = min(len(str1),len(str2))

    for i in range(l):        
        if str1 or str2:
            merged_string += str1[i] + str2[i]        
    merged_string += str1[l:] + str2[l:]
            
    return merged_string

print(mergedStrings('abcd','jk'))

