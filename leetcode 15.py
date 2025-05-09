# brute force  to find sum of three values according to conditions 

def sum_three(nums):
    M= set()
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            for k in range(j+1,len(nums)):
                # x = [nums[i],nums[j],nums[k]]
                if (i!=j and j!=k and i!=k) and (nums[i]+nums[j]+nums[k]==0):
                    x = [nums[i],nums[j],nums[k]]
                    x.sort()
                    # to convert list to tuple 
                    M.add(tuple(x))
    # wea want to obtain list at the end so convert set M into list                 
    return list(M)    



nums = [-1,0,1,2,-1,-4]
print(sum_three(nums))


# two pointers

def sum_three(nums):
    nums.sort()
    M=set()
    for i in range(len(nums)-2):
            left=i+1
            right = len(nums)-1
            while left< right:
                total = nums[left]+nums[right]+nums[i]
                if total ==0:
                    x = [nums[i],nums[left],nums[right]]
                    M.add(tuple(x))
                    while left<right and nums[left] == nums[left+1]:
                        left = left+1
                    while left<right and  nums[right] == nums[right-1]:
                        right = right-1  
                    left+=1
                    right-=1    
                elif total<0:
                    left = left+1
                        
            
                else:
                    right = right-1
    return list(M) 


nums = [-1,0,1,2,-1,-4]
print(sum_three(nums))