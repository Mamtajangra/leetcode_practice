'''Given a 0-indexed string word and a character ch, reverse the segment of word that starts at index 0 and ends at the index of the first occurrence of ch (inclusive). If the character ch does not exist in word, do nothing.
For example, if word = "abcdefd" and ch = "d", then you should reverse the segment that starts at 0 and ends at 3 (inclusive). The resulting string will be "dcbaefd".
Return the resulting string.
Example 1:
Input: word = "abcdefd", ch = "d"
Output: "dcbaefd"
Explanation: The first occurrence of "d" is at index 3. 
Reverse the part of word from 0 to 3 (inclusive), the resulting string is "dcbaefd".
'''


''' two list one for prefix aother for remaining member
    find the index of ch
    convert string to list
    in m list add members upto ch
    in n list add remaining members
    reverse the m and add two lists
    join resulting list into a single string and return'''
def reverse_prefix(word,ch):
    m = []
    n = []
    if ch not in word:
        return word
    idx  = word.index(ch)
    word = list(word)
    m = word[:idx +1]
    n = word[idx+1:]
    m.reverse()
    num = m + n
    num = "".join(num)
    return num

word = "abcdefd"
ch = "d" 
print(reverse_prefix(word,ch))
