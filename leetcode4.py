'''Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
The overall run time complexity should be O(log (m+n)).
Example 1:
Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.
Example 2:
Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
'''

'''     ## add two lists
        ## sort the resulted list
        ## check whether len of resulted list is odd
        ## if odd then return mid one 
        ## if not return mid two 
'''

def median(nums1,nums2):
    m = len(nums1)
    n = len(nums2)
    nums_total = nums1 + nums2
    nums_total.sort()
    n = len(nums_total)
    x = n//2
    if len(nums_total) % 2 != 0:
            
        return nums_total[x]
    else:
        mid1 = nums_total[x - 1]
        mid2 = nums_total[x]
        return (mid1 + mid2)/2 

nums1 = [1,2]
nums2 = [3,4]
print(median(nums1,nums2))    
