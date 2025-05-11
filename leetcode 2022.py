def one_to_2d(original,m,n):
    if len(original)!= m*n:   ## check length is equal to m*n
        return []           
        '''first of all we will initialize an empty list then a loop over m 
        because m is the length of original n denotes the columns,moreover we will find out rows like
        via slicing i*n to (i+1)*n and append this to row then return '''
    N = []
    for i in range(m):
        row = original[i*n:(i+1)*n]
        N.append(row)
    return N


original = [1,2,3,4]
m = 2
n = 2
print(one_to_2d(original,m,n))    
