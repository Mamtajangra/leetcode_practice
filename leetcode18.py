'''Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:

    0 <= a, b, c, d < n
    a, b, c, and d are distinct.
    nums[a] + nums[b] + nums[c] + nums[d] == target

You may return the answer in any order.
Example 1:

Input: nums = [1,0,-1,0,-2,2], target = 0
Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
'''
# using two pointer approach firstly sort the array initialize set to store unique values
def four_sum(nums,target):
    nums.sort()
    M = []
    # here we will fix left right ,i ,j means agar hamko 4 number chahiye to ensure karna hai ki i ke baad 3 numbers ho so that we wrote len-3
    for i in range(len(nums)-3):
        if i > 0 and nums[i] == nums[i-1]:
            continue
        for j in range(i+1,len(nums)-2):
            if j > i+1 and nums[j] == nums[j-1]:
                continue
            # in two pointer  firstly fix left and right,left is first element of j loop and right is one less from len(num)
            left = j+1
            right = len(nums)-1

            '''check three conditions like total == target,<target,>targetbut one condition arise between
            if num left == its next element so skip that similarly for right'''
            while left< right:
                total = nums[i]+nums[j]+nums[left]+nums[right]
                x = [nums[i],nums[j],nums[left],nums[right]]
                if total == target:
                    M.append(x)    ## tuple is immutable so use it instead of list 
                    while left<right and nums[left]==nums[left+1]:
                        left = left+1
                    while left<right and nums[right]==nums[right-1]:   
                        right = right-1
                 ##these conditions for moving loop to next condition       
                    left= left+1
                    right= right-1

                elif total<target:
                    left = left+1
                else:
                    right = right-1

                    
# return list 
    return (M)                


# check 
nums = [1,0,-1,0,-2,2] 
target = 0
print(four_sum(nums,target))
