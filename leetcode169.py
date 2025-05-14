'''Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.
Example 1:

Input: nums = [3,2,3]
Output: 3
'''
# to find element which are present in maximum times firstly sort the array and find mid index if 
# mid index is greater than that is the element present in maximum number of times 
def majority_elements(nums):
    nums.sort()
    count = 0
    mid = len(nums)//2
    for i in range(len(nums)):
        # if mid>count:
            # count+=1
            return nums[mid]
        
# check 
nums =[2,2,1,1,1,2,2]
print(majority_elements(nums))    