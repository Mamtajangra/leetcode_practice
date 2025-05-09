# array
def two_sum(nums,target):
    for i in range(len(nums)):
        if nums[i]+nums[i+1]==target:
            return [i,i+1]
        


nums = [2,7,11,15]
target = 9
print(two_sum(nums,target))        


# hash map 
def two_sum(nums,target):
    i = 0
    seen = {}
    for i,value in enumerate(nums):
        compliment = target - value
        if 