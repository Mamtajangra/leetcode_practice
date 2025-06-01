'''Given two arrays of equal size n and an integer k. The task is to permute both arrays such that sum of their corresponding element is greater than or equal to k i.e a[i] + b[i] >= k. The task is to print "Yes" if any such permutation exists, otherwise print "No".
Examples : 
Input : a[] = {2, 1, 3}, 
        b[] = { 7, 8, 9 }, 
        k = 10. 
Output : Yes
Permutation  a[] = { 1, 2, 3 } and b[] = { 9, 8, 7 } 
satisfied the condition a[i] + b[i] >= K.

Input : a[] = {1, 2, 2, 1}, 
        b[] = { 3, 3, 3, 4 }, 
        k = 5. 
Output : No'''


''' firstly we sorted list in ascending order and convert b in descending via loop we will check the condition '''
def permutation(a,b,k):
  a.sort()            ## ascending order

  b.sort()                  ## ascending order
  b = b[::-1]                   ## into descending

  for i in range(len(a)):           ## also use b insted of a
      if a[i] + b[i] < k:          
        return False
  return True      

a = [1, 2, 2, 1] 
b = [ 3, 3, 3, 4 ]
k = 5
print(permutation(a,b,k))      