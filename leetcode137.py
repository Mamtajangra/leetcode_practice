'''Given an integer array nums where every element appears three times except for one, which appears exactly once. Find the single element and return it.
You must implement a solution with a linear runtime complexity and use only constant extra space.
Example 1:
Input: nums = [2,2,3,2]
Output: 3
Example 2:
Input: nums = [0,1,0,1,0,1,99]
Output: 99
'''
def single2(nums):
    count = 0
    seen = {}
    for num in nums:
        if num in seen:
            seen[num] += 1
        else:
            seen[num] = 1
    for num,count in seen.items():
        if count == 1:
            return num
        
nums = [0,1,0,1,0,1,99]
print(single2(nums))