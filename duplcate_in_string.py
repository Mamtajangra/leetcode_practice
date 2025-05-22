'''Given a string S, the task is to print all the duplicate characters with their occurrences in the given string.

Example:

Input: S = "geeksforgeeks"
Output:
e, count = 4
g, count = 2
k, count = 2
s, count = 2

Explanation: g occurs 2 times in the string, k occurs 2 times in the string, s occurs 2 times in the string while e occurs 4 times in the string rest of the characters have unique occurrences.'''

def duplicates(S):
    count = 0
    seen = dict()
    seen1 = dict()
    for char in S:
        if char in seen:
            seen[char] += 1
        else:
            seen[char] = 1
    for char,freq in seen.items():                ## complexity o(n)
        if freq > 1:
            seen1[char] = freq
    return str(seen1)

S = "geeksforgeeks"
print(duplicates(S))  
