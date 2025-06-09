'''Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].'''

# array
def two_sum(nums,target):
    for i in range(len(nums)):
        if nums[i]+nums[i+1]==target:
            return [i,i+1]
        


nums = [2,7,11,15]
target = 9
print(two_sum(nums,target))        


# hash map 
def two_sum1(nums,target):
    i = 0
    seen = {}
    for i,value in enumerate(nums):
        compliment = target - value
        if compliment in seen:
            return [i,seen[compliment]]
        else:
            seen[value] = i

nums = [2,7,11,15]
target = 9
print(two_sum1(nums,target))            
