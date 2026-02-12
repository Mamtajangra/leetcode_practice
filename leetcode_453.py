'''Given an integer array nums of size n, return the minimum number of moves required to make all array elements equal.
In one move, you can increment n - 1 elements of the array by 1.
Example 1:
Input: nums = [1,2,3]
Output: 3
Explanation: Only three moves are needed (remember each move increments two elements):
[1,2,3]  =>  [2,3,3]  =>  [3,4,3]  =>  [4,4,4]'''


# if we increase n-1 (brute force) its complexity will be n**2
        # that's why i choose to fix the minimum number in nums and move other numbers backward and count there moves and add them to get final count
        # firstly in case 1st ,min is 1 and if i move 2 to 1 so it requires one move then count is 1
        # secondly i try to move 3 to 1 it required 2 moves  and count is 2 here 
        # now add up the total count that is 3
        # count will be like nums[0] - mini +nums[1] -mini +nums[2] -mini + nums[3] - mini....... nums[n] - mini  so it become
        #   sum(nums) - n* mini



def min_moves(nums):
    n = len(nums)
    mini = min(nums)
    count = sum(nums) - mini* n
    return count

nums = [1,2,3,4,5,6,7,8]
print(min_moves(nums))
