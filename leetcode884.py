'''A sentence is a string of single-space separated words where each word consists only of lowercase letters.
A word is uncommon if it appears exactly once in one of the sentences, and does not appear in the other sentence.
Given two sentences s1 and s2, return a list of all the uncommon words. You may return the answer in any order.
Example 1:
Input: s1 = "this apple is sweet", s2 = "this apple is sour"
Output: ["sweet","sour"]
Explanation:
The word "sweet" appears only in s1, while the word "sour" appears only in s2.
'''

## split two stringc and add to single,create dictionary
## mention the count for every word
## create list
## if value of any word is 1 in dict then append that word to dict and return

def uncommon(s1,s2):
        s1 = s1.split()
        s2 = s2.split()
        s = s1 + s2
        seen = {}

        for ch in s:
            if ch in seen:
                seen[ch] += 1
            else:
                seen[ch] = 1
        M = [] 
        for ch in seen:
            if seen[ch] == 1:
                M.append(ch)
        return M

s1 = "this apple is sweet"
s2 = "this apple is sour"  
print(uncommon(s1,s2))

