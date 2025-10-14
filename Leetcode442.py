'''Given an integer array nums of length n where all the integers of nums are in the range [1, n] and each integer appears at most twice, return an array of all the integers that appears twice.

You must write an algorithm that runs in O(n) time and uses only constant auxiliary space, excluding the space needed to store the output
Example 1:

Input: nums = [4,3,2,7,8,2,3,1]
Output: [2,3]
'''
# brute force 
def all_duplicate(nums):
    nums.sort()      ## optional                             having more tha two duplicates
    M = set()
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i] == nums[j]:
                M.add(nums[i])
    return list(M)   


nums = [4,3,2,7,8,2,3,3,1]        
print(all_duplicate(nums))         ## not working for large data 



# or 


def all_duplicate2(nums):
    nums.sort()      ## optional 
    M = set()
    for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                M.add(nums[i])
    return list(M)   


nums = [4,3,2,7,8,2,3,3,1]        
print(all_duplicate2(nums))         ##  working for large data 


#  The above functions were valid for examples where nums had duplicates of at most two.
#  all_duplicate_gen() will work for the cases where the duplicates were more than two.
def all_duplicate_gen(nums):
    seen = set()
    result = []
    for i in range(len(nums)):
        if nums[i] not in seen:
            seen.add(nums[i])
        else:
            if nums[i] not in result: 
                result.append(nums[i])

    return result   

nums = [4,3,2,7,8,2,3,3,1]        
print(all_duplicate_gen(nums))          


def all_duplicate_gen4(nums):
    seen = dict()
    M = []
    for num in nums:
        if num in seen:
            seen[num] += 1
        else:
            seen[num] = 1
    for num,count in seen.items():     ## MORE THAN TWO DUPLICATES
            if  count > 1:
                M.append(num)
    return M 

nums = [4,3,2,7,8,2,3,3,1,2,2,2,2,6,5,5,5]        
print(all_duplicate_gen4(nums))                   