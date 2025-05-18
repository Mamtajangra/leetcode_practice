'''Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.
Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
'''
def set_zero(matrix):
    set_row = set()         
    '''firstly construct two sets for rows and columns..then row length is equal to length of matrix column length is quite 
    different so we initialize it [0] kyunki sabme 4 items hai means column mein'''
    set_col = set()
    n_row = len(matrix)
    n_col = len(matrix[0])
    '''apply loop in row and column and extract the index ultimately fix these indicies in row set and col set'''
    for row in range(n_row):
            for col in range(n_col):
               if matrix[row][col] ==0:
                set_row.add(row)
                set_col.add(col)
               ''' here we just fixed indicies but we want to change row and column to zero pehle uss index ko dekha row wale ko 
               fir complete column ko aur value sab zero kardi and same for column '''
    for row in set_row:
            for col in range(n_col):
                matrix[row][col]=0
    for col in set_col:
            for row in range(n_row):
                matrix[row][col] =0    

    return matrix
matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
print(set_zero(matrix))                    


