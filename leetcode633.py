'''Given a non-negative integer c, decide whether there're two integers a and b such that a2 + b2 = c.
Example 1:
Input: c = 5
Output: true
Explanation: 1 * 1 + 2 * 2 = 5
Example 2:
Input: c = 3
Output: false
'''

'''two pointer approach
    left = 0 right = root(c)
    curr sum = left** left + right** right
    if curr sum == c, true
    less than c left += 1
    greater than right -= 1
    false'''
import math
def square(c):
    left = 0
    right = int(math.sqrt(c))
    while left <= right:
        curr_sum = left* left + right * right
        if curr_sum == c:
            return True
        elif curr_sum < c:
            left += 1
        else:
            right -= 1
    return False   


c = 5
print(square(c))