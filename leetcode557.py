'''Given a string s, reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.
Example 1:
Input: s = "Let's take LeetCode contest"
Output: "s'teL ekat edoCteeL tsetnoc"
Example 2:
Input: s = "Mr Ding"
Output: "rM gniD"
'''

'''split each word
   reverse the words
   and apend these words to list after reversing
   then join each word in string'''

def reverse(s):
    words = s.split()
    reverse_w = []
    for word in words:
        reverse_w.append(word[::-1])
    return ' '.join(reverse_w)


s = "Let's take LeetCode contest"
print(reverse(s))