def duplicate(nums):    
    nums.sort()
    for i in range(len(nums)-1):
            # for j in range(i+1,len(nums)):
        if nums[i] == nums[i+1]:
                return nums[i]
        


nums = [1,3,2,4,2,3,2]
print(duplicate(nums))        
        