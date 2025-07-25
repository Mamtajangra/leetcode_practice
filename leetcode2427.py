'''Given two positive integers a and b, return the number of common factors of a and b.
An integer x is a common factor of a and b if x divides both a and b.
Example 1:
Input: a = 12, b = 6
Output: 4
Explanation: The common factors of 12 and 6 are 1, 2, 3, 6.
Example 2:
Input: a = 25, b = 30
Output: 2
Explanation: The common factors of 25 and 30 are 1, 5.
'''

def common_factor(a,b):
    count = 0
    limit = min(a,b)
    for x in range(1,limit + 1):
        if a%x == 0 and b%x == 0:
            count += 1
    return count


a = 12
b = 6
print(common_factor(a,b))            