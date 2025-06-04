'''Given a string s, return true if the s can be palindrome after deleting at most one character from it.
Example 1:
Input: s = "aba"
Output: true
Example 2:
Input: s = "abca"
Output: true
Explanation: You could delete the character 'c'.
Example 3:
Input: s = "abc"
Output: false
'''
def palindrome(str):
    def is_palin(str):
        return str == str[::-1]
                
    left = 0
    right = len(str)-1
    while left < right:
        if str[left] != str[right]:
            return is_palin(str[left+1:right+1]) or is_palin(str[left:right])
        left += 1
        right -=1
    return True        
  


str =  "abca"
print(palindrome(str))