# brute force 
def all_duplicate(nums):
    nums.sort()      ## optional 
    M = []
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i] == nums[j]:
                M.append(nums[i])
    return M   


nums = [4,3,2,7,8,2,3,3,1]        
print(all_duplicate(nums))         ## not working for large data 



# or 


def all_duplicate2(nums):
    nums.sort()      ## optional 
    M = []
    for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                M.append(nums[i])
    return M   


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
