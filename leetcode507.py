'''A perfect number is a positive integer that is equal to the sum of its positive divisors, excluding the number itself. A divisor of an integer x is an integer that can divide x evenly.
Given an integer n, return true if n is a perfect number, otherwise return false.
Example 1:
Input: num = 28
Output: true
Explanation: 28 = 1 + 2 + 4 + 7 + 14
1, 2, 4, 7, and 14 are all divisors of 28.
Example 2:
Input: num = 7
Output: false
 '''

'''list
   check all the integer which divides the given positive integer and append to list
   now find the sum of all element of list
   if sum == num is perfect number otherwise no'''

def perfect_n(num):
    m = []
    for i in range(1,num):
        if num%i == 0:
            m.append(i)
    sum_n  = sum(m)
    if sum_n  == num:
        return True
    return False   


num = 28
print(perfect_n(num))
                
