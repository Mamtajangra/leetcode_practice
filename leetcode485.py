'''Given a binary array nums, return the maximum number of consecutive 1's in the array.
Example 1:
Input: nums = [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.
Example 2:
Input: nums = [1,0,1,1,0,1]
Output: 2
'''

##  check if first number is 1 then count is 1
##  and if 2nd one is 0 then count become 0 
## again maximize the count and return
def binary_arr(nums):
    count = 0
    maxi = 0       
    for i in range(len(nums)):
        if nums[i] == 1:
            count += 1
            maxi = max(maxi,count)
        else:
            count = 0    
    return maxi  

nums =  [1,1,0,1,1,1]
print(binary_arr(nums))     
