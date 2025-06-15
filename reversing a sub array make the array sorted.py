'''Given an array of n distinct integers. The task is to check whether reversing any one sub-array can make the array sorted or not. If the array is already sorted or can be made sorted by reversing any one subarray, print "Yes", else print "No".
Examples: 
Input : arr [] = {1, 2, 5, 4, 3}
Output : Yes
By reversing the subarray {5, 4, 3}, the array will be sorted.

example 2.Input : arr [] = { 1, 2, 4, 5, 3 }
Output : No
'''

## choose start and end point
## check zeroth element less than first one if yess move start to next 
## in case nums is already sorted return yes 
##  also check the last one with the second last if last one is large than the second last decrement from right side 
## subarray is between start to end 
## now reverse it 
## new array = start + that subarray(sorted) + end
### check new array is sorted return yes otherwise no



def reverse(nums):
    start = 0
    end = len(nums)-1
    while nums[start] < nums[start+1] and start < len(nums)-1:
        start += 1
        if start == len(nums)-1:
            return "Yes"
    while end > 0 and nums[end] > nums[end-1]:
        end -= 1
    sub = nums[start:end+1] 
    sub.reverse()
    new_nums = nums[:start] + sub + nums[end+1:]
    if new_nums == sorted(nums):
        return "Yes"
    else:
        return "No"
nums = [1, 2, 5, 4, 3]    
print(reverse(nums))