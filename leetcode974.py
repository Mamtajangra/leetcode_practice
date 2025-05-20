'''Given an integer array nums and an integer k, return the number of non-empty subarrays that have a sum divisible by k.

A subarray is a contiguous part of an array.
Example 1:

Input: nums = [4,5,0,-2,-3,1], k = 5
Output: 7
Explanation: There are 7 subarrays with a sum divisible by k = 5:
[4, 5, 0, -2, -3, 1], [5], [5, 0], [5, 0, -2, -3], [0], [0, -2, -3], [-2, -3]
'''
def subarray_sum(nums,k):
    count = 0
    for num in range(len(nums)):     ## initialize list and sum here because we want each list for each array
        M = []
        sum = 0
        for num1 in range(num,len(nums)):  
            M.append(nums[num1])             ## append subarrays to the list 
            sum = sum + nums[num1]             ## now check the sum if divisible  by k(given)
            if sum % k ==0:
                count = count + 1               ## for each result increase one count 
            
    return count  

nums = [4,5,0,-2,-3,1]
k = 5  
print(subarray_sum(nums,k))       
