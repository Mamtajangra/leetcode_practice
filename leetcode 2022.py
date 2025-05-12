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


                                                          # or 
'''matrix length should m*n and create subarray temporary n=0
loop in original and append the elements in subarray if tn<n.Moreover,if tn==nmeans no more space to append then 
append subarray to N for fresh values we need tn=0 again at last return N '''

def one_to_two_d(original,m,n):
    if len(original)!=m*n:
        return []
    N = []
    sub_arr = []
    tn = 0
    for i in original:
        if tn < n:
            sub_arr.append(i)
            tn+= 1
            if tn == n:
                N.append(sub_arr)
                sub_arr = []
                tn = 0
    return N
    

original = [1,2,3,4]
m = 2
n = 2
print(one_to_two_d(original,m,n))      