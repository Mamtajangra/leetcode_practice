''' Find the Index of the First Occurrence in a String
Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
Example 1:

Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.
'''
def first_occur(haystack,needle):
    n = len(haystack)
    m = len(needle)
    # loop over the range of total lengthof num minus window (needle)
    for i in range(n-m+1):
        # slicing means including the only member from window length 
        if haystack[i:i+m] == needle:
            return i
    return -1

# check 
haystack = "leetcode"   
needle = "leeto"
print(first_occur(haystack,needle)) 