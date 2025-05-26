'''Given an array arr[] of n integers, construct a product array res[] (of the same size) such that res[i] is equal to the product of all the elements of arr[] except arr[i]. 
Example: 
Input: arr[] = [10, 3, 5, 6, 2]
Output: [180, 600, 360, 300, 900]
Explanation: 
 
For i=0, res[i] = 3 * 5 * 6 * 2 is 180.
For i = 2, res[i] = 10 * 3 * 6 * 2 is 360.
For i = 3, res[i] = 10 * 3 * 5 * 2 is 300.
For i = 4, res[i] = 10 * 3 * 5 * 6 is 900.'''

def pdt(nums):
  pdt= 1
  M = []
  for num in range(len(nums)):    ## we dont need to change product 
    pdt = pdt*nums[num]

  for num in nums:                ## pdt except itself = total pdt// that specific index value 
    result = pdt// num
    M.append(result)
  return M

nums = [10, 3, 5, 6, 2]
print(pdt(nums))  