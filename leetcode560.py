'''Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.

A subarray is a contiguous non-empty sequence of elements within an array.
Example 1:

Input: nums = [1,1,1], k = 2
Output: 2
'''
def subarray_sum(nums,k):
    count = 0
    for num in range(len(nums)):
        M = []
        sum = 0
        for num1 in range(num,len(nums)):
                M.append(nums[num1])
                sum = sum + nums[num1]
                if sum == k:
                    count = count + 1
    return count    



nums = [1,1,1]
k = 2
print(subarray_sum(nums,k))