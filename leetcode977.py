'''Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.
Example 1:
Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Explanation: After squaring, the array becomes [16,1,0,9,100].
After sorting, it becomes [0,1,9,16,100].
'''

def sq_sorted(nums):
    M = []
    for i in range(len(nums)):
        M.append(nums[i]**2)
        M.sort()
    return M

nums =  [-4,-1,0,3,10] 
print(sq_sorted(nums))      