'''You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.
Return true if you can reach the last index, or false otherwise.
Example 1:

Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
'''
def jump(nums):
    maxreach = 0
    for i in range(len(nums)):
        if i > maxreach:        ## where index is larer than maximum give false
            return False
        maxreach = max(maxreach,i+nums[i])       ## it determine the maximum of max and the position where we are at current moment and its value
        if maxreach >= len(nums) -1:     ## if max value is greater than or qual to the length of array it gives true value otherwise false
            return True
    return False

nums = [2,3,1,1,4]
print(jump(nums))
    