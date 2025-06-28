'''Given a string s consisting of words and spaces, return the length of the last word in the string.
A word is a maximal consisting of non-space characters only.
Example 1:
Input: s = "Hello World"
Output: 5
Explanation: The last word is "World" with length 5.
'''

## split string into the different string in list
## now return length of last character in resulted list

def str(s):
    res = s.split()
    return len(res[-1])

s = "Hello World"
print(str(s))