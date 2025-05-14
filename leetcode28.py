# Find the Index of the First Occurrence in a String

'''Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
Example 1:

Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.'''
def first_occurrence(haystack,needle):
    for i in range(len(haystack)):
        if needle in haystack:
            return haystack.index(needle)          
        else:
            return -1    
        

haystack = "sadbutsad"    
needle = "sad"
print(first_occurrence(haystack,needle))    
        


        # to find index simply use .index
        