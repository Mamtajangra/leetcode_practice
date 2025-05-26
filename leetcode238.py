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
print(pdt(nums))                       ## o(n**2)




def pdt1(nums):
## firstly we are going to handle the case of zero and more than one zero 

  count = 0
  idx = -1
        ## to check zeroes in array ,if there is zero increase count by 1 and store there indicies
  for i,num in enumerate(nums):
    if num == 0:
      count += 1
      idx = i
        # print(idx)
        ## if count(zero) is more than one means array acquire 0 values
  if count > 1:
    return [0] * len(nums)

            ## if there is single zero determine pdt if current index is not equal to zero
  if count == 1:
    result = [0] * len(nums)

    pdt = 1
    for i,num in enumerate(nums):
      if i != idx:
        pdt = pdt * num

                 ## that product is present at the same index  of zero   
        result[idx] = pdt
    return result 

## determine the product of nonzero array firstly findout simple pdt and append result to a list according to the way that divide the pdt with current index value
  pdt1 = 1
  for i,num in enumerate(nums):
    pdt1 = pdt1 * num


    final = []   
    for num in nums:
      final.append(pdt1 //num)
  return final   



nums = [10, 3, 5, 6, 2]
print(pdt1(nums))   
