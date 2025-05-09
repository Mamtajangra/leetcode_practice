# to sort the colors using bubble sort 
def sort_color(nums): 
    for i in range(len(nums)):
        for j in range(0,len(nums)-1-i):
            if nums[j]>nums[j+1]:
                nums[j],nums[j+1] = nums[j+1],nums[j]
    return nums           


nums = [2,0,2,1,1,0]   
print(sort_color(nums))             