'''Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.
Example 1:
Input: nums = [3,2,3]
Output: [3]
Example 2:
Input: nums = [1]
Output: [1]
Example 3:
Input: nums = [1,2]
Output: [1,2]
'''
def majority_element2(nums):
       # create dictionary
       # check elemnts are present in dictionary if not assign unique
       # determine frequency of each items ,if follow the condition append it 

        seen = dict()
        M = []
        # count = 0
        for num in nums:
             
            if num in seen:
                seen[num] += 1   # if duplicate in nums move to next
            else:
                seen[num] = 1     # if element is not present it is unique 
        for num,freq in seen.items():  # frequency of items 
            if freq > len(nums)//3:     
                    M.append(num) 
        return M          

nums = [3,2,3]
print(majority_element2(nums))
