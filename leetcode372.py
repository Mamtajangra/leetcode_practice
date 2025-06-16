'''Your task is to calculate ab mod 1337 where a is a positive integer and b is an extremely large positive integer given in the form of an array.
Example 1:
Input: a = 2, b = [3]
Output: 8
Example 2:
Input: a = 2, b = [1,0]
Output: 1024
Example 3:
Input: a = 1, b = [4,3,3,8,5,2]
Output: 1
'''


## convert list element to string then join them finally convert into number
## find the a raise to power b with modulo 1337

def super_pow(a,b):
    b = int("".join(map(str,b)))
    return pow(a,b) % 1337



a = 2
b = [1,0]
print(super_pow(a,b))