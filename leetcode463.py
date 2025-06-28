'''You are given row x col grid representing a map where grid[i][j] = 1 represents land and grid[i][j] = 0 represents water.
Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells).
The island doesn't have "lakes", meaning the water inside isn't connected to the water around the island. One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.
Example 1:
Input: grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
Output: 16
Explanation: The perimeter is the 16 yellow stripes in the image above.
Example 2:
Input: grid = [[1]]
Output: 4
'''

## check the length of row and column
##  if grid[i][j] ==1 only possible case for perimeter so count all 4 sides i.e perimeter is 4
##  now check the square attach with each other if yess two sides are common so perimeter is -2
##  same for columns perimeter is -2

def island(grid):
    rows = len(grid)
    cols = len(grid[0])
    perimeter = 0
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                perimeter += 4
## check the neighbour row and column means they attach with each other so reduce two common side in case of row and column also
                if i+1 < rows and grid[i+1][j] == 1:
                    perimeter -= 2
                if j+1 < cols and grid[i][j+1] == 1:
                    perimeter -= 2


    return perimeter  


grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
print(island(grid))
