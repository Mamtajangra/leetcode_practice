'''You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.
Increment the large integer by one and return the resulting array of digits.
Example 1:
Input: digits = [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Incrementing by one gives 123 + 1 = 124.
Thus, the result should be [1,2,4].
'''

     ## convert list to complete number    123
        ## add 1 to result  123 +1
        ## return the list again after converting it to the list  [1,2,4]
def plus_one(digits):
    x = int(''.join(str(d) for d in digits))
    res = x +1
    res_list = [int(ch) for ch in str(res)]
    return res_list 

digits = [1,2,3]
print(plus_one(digits))
        
            