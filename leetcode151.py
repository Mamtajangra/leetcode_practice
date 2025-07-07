'''Given an input string s, reverse the order of the words.
A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.
Return a string of the words in reverse order concatenated by a single space.
Note that s may contain leading or trailing spaces or multiple spaces between two words. The returned string should only have a single space separating the words. Do not include any extra spaces.
Example 1:
Input: s = "the sky is blue"
Output: "blue is sky the"
'''
  ## split the string and add it into list
        ## two pointer left and right
        ## swapping left to right
        ## convert list to string after join

def reverse(s):
        list_s = list(s.split())
        left = 0
        right = len(list_s) - 1

        while left < right:
            list_s[left] , list_s[right] = list_s[right] , list_s[left]
            left += 1
            right -= 1
        return ' '.join(list_s)

s = "the sky is blue"
print(reverse(s))