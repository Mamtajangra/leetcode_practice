'''Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.
Example 1:

Input: nums = [3,0,1]
Output: 2
Explanation:

n = 3 since there are 3 numbers, so all numbers are in the range [0,3]. 2 is the missing number in the range since it does not appear in nums.
'''
def missing_number(nums):
    n = len(nums) 
    total_sum=n*(n+1)//2
    nums_sum = sum(nums)
    result = total_sum - nums_sum
    return result



nums = [3,0,1]
print(missing_number(nums))