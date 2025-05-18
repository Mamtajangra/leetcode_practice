'''Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.
Example 1:
Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]

Example 2:
nput: nums = [0]
Output: [0]'''
def move_zero(nums):
    non_zero = []
    zero = []
    for num in nums:
        if num!= 0:
            non_zero.append(num)
        else:
            zero.append(num)

    final = non_zero + zero
    for j in range(len(nums)):
        nums[j] = final[j]


    return final   

nums = [0,1,0,3,12]
print(move_zero(nums))



# optimize two pointer fix one if another one found nonzero then swap
def move_zero1(nums):
    i = 0
    for j in range(len(nums)):
        if  nums[j] != 0:
            nums[i],nums[j] = nums[j], nums[i]
            i = i+1
    return nums 


nums = [0,1,0,3,12]
print(move_zero1(nums))

                                                                                                                                                                                                





