# we want to find uniue element present initially in nums 
def remove_duplicate(nums):
    nums1 = list(set(nums))
    # slicing to get unique elements in left side 
    nums[:len(nums1)] = nums1
    return nums1

# check 
nums = [0,0,1,1,1,2,2,3,3,4]
print(remove_duplicate(nums))