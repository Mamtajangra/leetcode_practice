'''Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.
Assume the environment does not allow you to store 64-bit integers (signed or unsigned).
Example 1:
Input: x = 123
Output: 321
Example 2:
Input: x = -123
Output: -321
Example 3:
Input: x = 120
Output: 21
'''

def reverse_integer(x):
    if x < 0:
        sign = -1
    else:
        sign = 1    
    reverse = int(str(abs(x))[::-1])
    reverse *= sign
    if reverse < -2**31 or reverse > (2**31):
        return 0
    return reverse 

x = 120
print(reverse_integer(x))   
              
       