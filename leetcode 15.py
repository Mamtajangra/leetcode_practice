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