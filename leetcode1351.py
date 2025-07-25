'''Given a m x n matrix grid which is sorted in non-increasing order both row-wise and column-wise, return the number of negative numbers in grid.
Example 1:
Input: grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
Output: 8
Explanation: There are 8 negatives number in the matrix.
Example 2:
Input: grid = [[3,2],[1,0]]
Output: 0
'''

def negative(grid):
    count = 0
    r = len(grid)
    c = len(grid[0])
    for row in range(r):
        for col in range(c):
            if grid[row][col] < 0:
                    
                count += 1
    return count 


grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
print(negative(grid))