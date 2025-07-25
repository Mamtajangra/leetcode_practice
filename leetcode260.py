'''Given an integer array nums, in which exactly two elements appear only once and all the other elements appear exactly twice. Find the two elements that appear only once. You can return the answer in any order.
You must write an algorithm that runs in linear runtime complexity and uses only constant extra space.
Example 1:
Input: nums = [1,2,1,3,2,5]
Output: [3,5]
Explanation:  [5, 3] is also a valid answer.
Example 2:
Input: nums = [-1,0]
Output: [-1,0]
'''

'''create dictionary
   list
   if number in dict move to the next
   if not initialize it 1
   now count the items occuring once
   append it to list'''

def single_number(nums):
    seen ={}
    m = []
    for num in nums:
        if num in seen:
            seen[num] += 1
        else:
            seen[num] = 1
    for num,count in seen.items():       
        if count  == 1:
            m.append(num) 
    return m   

nums =  [1,2,1,3,2,5] 
print(single_number(nums))          
        