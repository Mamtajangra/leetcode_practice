# to find element which are present in maximum times firstly sort the array and find mid index if 
# mid index is greater than that is the element present in maximum number of times 
def majority_elements(nums):
    nums.sort()
    count = 0
    mid = len(nums)//2
    for i in range(len(nums)):
        if mid>count:
            count+=1
            return nums[mid]
        
# check 
nums =[2,2,1,1,1,2,2]
print(majority_elements(nums))    