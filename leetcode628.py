'''Given an integer array nums, find three numbers whose product is maximum and return the maximum product.
Example 1:

Input: nums = [1,2,3]
Output: 6
'''
def maximum_pdt(nums):
    nums.sort()
    pdt = 0
    for num in nums:
        # it shows the last threee values product
        pdt1 = nums[-1] * nums[-2] * nums[-3]

        # here is the product of first two negative numbers and last positive which give max  
        # ex == -100,-90,1,2,3,4    max = -100 * (-90) *4 
        pdt2 = nums[0] * nums[1] * nums[-1]

        # to find maximum from pdt1 and pdt2
        pdt = max(pdt1,pdt2)
    return pdt 

# check 
nums = [1,2,3]
print(maximum_pdt(nums))
                                    #   it gives time compleexity o(nlog(n)

                                    # or 


def maximum_pdt1(nums):
    max1 = max2 = max3 = float("-inf")     ##determine three largest number an check with smaller value this float value is by default
    min1 = min2 =  float("inf")             ## similarly check with maximum value
    for num in nums:
        # if value > max1,max2,max3 it become num
        if num > max1:
            max3 = max2
            max2 = max1
            max1 = num
        elif num > max2:
            max3 = max2
            max2 = num
        elif num > max3:
            max3 = num

            # here we are checking minimum if siome value is less than minimum it become the minimum again 
        if num < min1:
            min2 = min1
            min1 = num
        elif num < min2:
            min2 = num

    return max(max1 * max2 * max3 , min1 * min2* max1)

# check 
nums = [-1,-2,-3]
print(maximum_pdt1(nums))        # time complexity is o(n)