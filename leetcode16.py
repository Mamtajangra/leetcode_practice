'''Given an integer array nums of length n and an integer target, find three integers in nums such that the sum is closest to target.
Return the sum of the three integers.
You may assume that each input would have exactly one solution.
Example 1:
Input: nums = [-1,2,1,-4], target = 1
Output: 2
Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
Example 2:
Input: nums = [0,0,0], target = 1
Output: 0
Explanation: The sum that is closest to the target is 0. (0 + 0 + 0 = 0).
'''
''' two pointer fix one 
    sort the array
    fix one number and move other two
    find the total sum = sum (fixed) + sum(1st pointer) + sum( 2nd pointer)
    check sum is equal to target if yess return otherwise move pointers
    also check total_sum - target < closest - target if yes closest become total _sum and return it
    '''



def three_sum_closest(nums,target):
    nums.sort()
    closest = float('inf')
    for i in range(len(nums)-2):
        left = i + 1
        right = len(nums) -1
        while left < right:
            total_sum = nums[i] + nums[left] + nums[right]
            if total_sum == target:
                return total_sum
            if abs(total_sum - target) < abs(closest - target):
                closest = total_sum
            if total_sum < target:
                left += 1   
            else:
                right -= 1
    return closest

nums = [-1,2,1,-4]
target  = 1
print(three_sum_closest(nums,target))

