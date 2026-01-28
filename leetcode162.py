'''A peak element is an element that is strictly greater than its neighbors.
Given a 0-indexed integer array nums, find a peak element, and return its index. If the array contains multiple peaks, return the index to any of the peaks.
You may imagine that nums[-1] = nums[n] = -∞. In other words, an element is always considered to be strictly greater than a neighbor that is outside the array.
You must write an algorithm that runs in O(log n) time.
Example 1:

Input: nums = [1,2,3,1]
Output: 2
Explanation: 3 is a peak element and your function should return the index number 2'''

def peak_element(nums):
    # maxi = 0
    if len(nums) == 1:                
        return 0
    
    if len(nums) == 2:
        if nums[0] > nums[1]:         ## x =[2,3] or [3,2] check which is larger than other
            return 0
        else:
            return 1    
           
    for i in range(1,len(nums)-1):                ## now we are checking from 1 to last ex = [2,3,1] result = 3
           
        if  nums[i-1] < nums[i] > nums[i + 1]:
            return i
    if nums[len(nums)-1] < nums[len(nums)-2]:           ## check last digits [1,3,2] gives = 0
            return 0    
    else:
            return len(nums)-1  

# check 
nums = [1,2,3,1]
print(peak_element(nums))   



def peak_element1(nums):
    if len(nums) == 1:
            return 0
        
    if nums[1] < nums[0]:
                return 0
    if nums[len(nums)-2] < nums[len(nums)-1]:

                return len(nums)-1    

    for i  in range(1,len(nums)-1):
            if nums[i] > nums[i+1] and nums[i-1]< nums[i]:
                return i
            

    # check 
nums = [1,2,3,1]
print(peak_element1(nums))           
        