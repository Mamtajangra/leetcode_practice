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
print(subarray_sum(nums,k))               ## o(n**2)



def subarray_sum1(nums,k):
    count = 0
    prefix_sum = 0
    count_sub = {0:1}          ## by default to hadle case of 0
    for i in range(len(nums)):
        prefix_sum = prefix_sum + nums[i]
# if target in dict increase count 
        if prefix_sum % k in count_sub:
            count  = count + count_sub[prefix_sum % k]

# simple dictionary condition 
        if prefix_sum % k in count_sub:
            count_sub[prefix_sum % k] += 1
        else:
            count_sub[prefix_sum % k] = 1
    return count

    
nums = [4,5,0,-2,-3,1]
k = 5  
print(subarray_sum1(nums,k))  

