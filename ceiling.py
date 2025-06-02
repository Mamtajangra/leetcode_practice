'''Given a sorted array and a value x, find index of the ceiling of x. The ceiling of x is the smallest element in an array greater than or equal to x.

Note: In case of multiple occurrences of ceiling of x, return the index of the first occurrence.

Examples : 

    Input: arr[] = [1, 2, 8, 10, 10, 12, 19], x = 5
    Output: 2
    Explanation: Smallest number greater than 5 is 8, whose index is 2.

    Input: arr[] = [1, 2, 8, 10, 10, 12, 19], x = 20
    Output: -1
    Explanation: No element greater than 20 is found. So output is -1.

    Input: arr[] = [1, 1, 2, 8, 10, 10, 12, 19], x = 0
    Output: 0
    Explanation: Smallest number greater than 0 is 1, whose indices are 0 and 1. The index of the first occurrence is 0.'''
def ceiling(arr,k):
  count = 0
  for i in range(len(arr)):
    if arr[i] < k:
      count = count + 1
  return count
  

arr =  [1, 2, 8, 10, 10, 12, 19]  
k = 5
print(ceiling(arr,k))