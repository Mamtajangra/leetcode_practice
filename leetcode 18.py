
# using two pointer approach firstly sort the array initialize set to store unique values
def four_sum(nums,target):
    nums.sort()
    M = set()
    # here we will fix left right ,i ,j means agar hamko 4 number chahiye to ensure karna hai ki i ke baad 3 numbers ho so that we wrote len-3
    for i in range(len(nums)-3):
        for j in range(i+1,len(nums)-2):
            # in two pointer  firstly fix left and right,left is first element of j loop and right is one less from len(num)
            left = j+1
            right = len(nums)-1

            '''check three conditions like total == target,<target,>targetbut one condition arise between
            if num left == its next element so skip that similarly for right'''


            while left< right:
                total = nums[i]+nums[j]+nums[left]+nums[right]
                x = [nums[i],nums[j],nums[left],nums[right]]
                if total == target:
                    M.add(tuple(x))    ## tuple is immutable so use it instead of list 
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
    return list(M)                


# check 
nums = [1,0,-1,0,-2,2] 
target = 0
print(four_sum(nums,target))
