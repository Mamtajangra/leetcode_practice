'''Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.
Example 1:

Input: nums = [1,3,5,6], target = 5
Output: 2
'''


## two pointer
## mid
def insert_pos(nums,target):
    low = 0
    high = len(nums) -1
    while low <= high: 
        mid = (low +high)//2    
        if nums[mid] == target:
            return mid
        elif nums[mid]< target:
            low= mid + 1
        else:
            high = mid - 1
    return low 


nums = [1,3,5,6]
target = 5
print(insert_pos(nums,target))


            