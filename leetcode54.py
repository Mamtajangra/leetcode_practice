'''Given an m x n matrix, return all elements of the matrix in spiral order.
Example 1:

Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]
'''
def spiral_matrix(matrix):
    spiral = []
    if not matrix:
        return spiral
    n_row = len(matrix)
    n_col = len(matrix[0])
    top = 0
    bottom = len(matrix)-1
    left = 0
    # rows and columns are different 
    right = len(matrix[0]) -1
    # spiral = []
    while top <= bottom and left <= right:
                                                #  l,t    ------->  r,t
                                                    #    ,        ,
                                                    #    ,        ,
                                                    #    ,        ,
                                                    # b,l<-------- b,r
                                                    
        # ist move left to right changes occur in top and in columns move to the next column after checking 1st one
        for col in range(left,right+1):
            spiral.append(matrix[top][col])
        top = top + 1

        # 2nd move from top to bottom in right side changes occur in rows in right side and subtract 1 from right to move down
        for row in range(top,bottom+1):
            spiral.append(matrix[row][right])
        right = right-1

        # 3rd move right to left with -1 decrement only changes occur in columns in bottom 
        if top <= bottom:     ## ye safety barriers hote hai taaki hmm uss row ya column pe dobara visit na karein 
            for col in range(right,left-1,-1):
                spiral.append(matrix[bottom][col])
            bottom = bottom-1
            
            # 4th move from bottom to top with -1 decrement and effect occured in rows present in left side
        if left <= right:    
            for row in range(bottom,top-1,-1):
                spiral.append(matrix[row][left])
            left = left+1
    return spiral



# check 
matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(spiral_matrix(matrix))



