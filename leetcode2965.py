'''You are given a 0-indexed 2D integer matrix grid of size n * n with values in the range [1, n2]. Each integer appears exactly once except a which appears twice and b which is missing. The task is to find the repeating and missing numbers a and b.
Return a 0-indexed integer array ans of size 2 where ans[0] equals to a and ans[1] equals to b.
Example 1:
Input: grid = [[1,3],[2,2]]
Output: [2,4]
Explanation: Number 2 is repeated and number 4 is missing so the answer is [2,4].
Example 2:
Input: grid = [[9,1,7],[8,9,2],[3,4,6]]
Output: [9,5]
Explanation: Number 9 is repeated and number 5 is missing so the answer is [9,5].
'''
import numpy as np
def missing(grid):
    x = np.array(grid)
    y = np.reshape(x,-1).tolist()          ## convert to 1d
    y.sort()
    n = len(grid)



    total_sum = n*n*(n*n+1)//2            ## total sum for 2 d  because n is 2 times here and it also given range is n*n
    y_sum = int(np.sum(y))   
    
## convert to int value otherwise it is numpy int value 
    diff = total_sum - y_sum
    repeat = 0
    
    
    for i in range(len(y)-1):
        if y[i] == y[i+1]:
            repeat = y[i]


    missing = repeat + diff
    return [missing,repeat]

grid = [[9,1,7],[8,9,2],[3,4,6]]
print(missing(grid))


