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
print(subarray_sum(nums,k))       ## o(n**2)


# prefix and hash 

def subarray_sum1(nums,k): 
    count = 0
    prefix_sum = 0
    count_sub = {0:1}                 ## by default to handle the case 7-7 = 0
    for num in range(len(nums)):
        prefix_sum = prefix_sum + nums[num]
        if (prefix_sum - k) in count_sub:                      ## check prefix sum - target sum in dict increase count if yes 
             count = count + count_sub[prefix_sum - k]
        if prefix_sum in count_sub:                       ## simple case of hash map
             count_sub[prefix_sum] += 1
        else:
             count_sub[prefix_sum] = 1
    return count  

# check 
nums = [1,1,1]
k = 2
print(subarray_sum1(nums,k))  