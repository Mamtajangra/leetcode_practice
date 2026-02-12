'''Given an integer n, return true if it is a power of two. Otherwise, return false.
An integer n is a power of two, if there exists an integer x such that n == 2x.
Example 1:
Input: n = 1
Output: true
Explanation: 20 = 1
Example 2:
Input: n = 16
Output: true
Explanation: 24 = 16
'''

def power_of_two(n):
    if n <= 0:
        return False
    while n % 2 == 0:
        n = n//2
    return n== 1

n = 5
print(power_of_two(n))

# 2nd 

    # using bit manipulation method where 
    # 1. convert n into bit 
    # 2. convert n-1 into bit
    # 3. not using bitwise or means(if both 1 getting result 1 otherwise 0)
    # 4 if 0 then result get true i.e in power of 2 otherwise false 
def power_of_two2(n):            
    if n>0 and n &(n-1) ==0:
        return True
    else:
        return False    
      

n = 16
print(power_of_two2(n))