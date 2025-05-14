'''Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.

There is only one repeated number in nums, return this repeated number.

You must solve the problem without modifying the array nums and using only constant extra space.
Example 1:

Input: nums = [1,3,4,2,2]
Output: 2
'''

def duplicate(nums):    
    nums.sort()
    for i in range(len(nums)-1):
            # for j in range(i+1,len(nums)):
        if nums[i] == nums[i+1]:
                return nums[i]
        


nums = [1,3,2,4,2,3,2]
print(duplicate(nums))        
        


def duplicate1(nums):  
    seen = set()
    for num in nums:
            if num  not in seen:
                seen.add(num)
            else:    
                return num                  
            

nums = [1,3,2,4,2,3,2]
print(duplicate1(nums))             