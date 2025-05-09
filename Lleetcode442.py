# brute force 
def all_duplicate(nums):
    nums.sort()      ## optional 
    M = []
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i] == nums[j]:
                M.append(nums[i])
    return M   


nums = [4,3,2,7,8,2,3,1]        
print(all_duplicate(nums))         ## not working for large data 



# or 


def all_duplicate(nums):
    nums.sort()      ## optional 
    M = []
    for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                M.append(nums[i])
    return M   


nums = [4,3,2,7,8,2,3,1]        
print(all_duplicate(nums))         ##  working for large data 

