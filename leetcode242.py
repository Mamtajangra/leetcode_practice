'''Given two strings s and t, return true if t is an of s, and false otherwise.
Example 1:
Input: s = "anagram", t = "nagaram"
Output: true
Example 2:
Input: s = "rat", t = "car"
Output: false
'''
def anagram(s,t):
       ## create a dict
        ## check ch of s in dict.. if yes move to next if not assign it unique
        ## same check ch of t in dict.. if not return false and if yess skip this and check next one return true
        seen = dict()
        for ch in s:
            if ch in seen:
                seen[ch] += 1
            else:
                seen[ch] = 1
        for ch in t:
            if ch not in seen:
                return False
            seen[ch] -= 1
        return True 
s = "anagram"
t = "nagaram"
print(anagram(s,t))
