'''Given an unsorted array and an integer x, the task is to find if there exists a pair of elements in the array whose absolute difference is x. 
Examples: 
Input: arr[] = [5, 20, 3, 2, 50, 80], x = 78
    Output: Yes
    Explanation: The pair is {2, 80}.

    Input: arr[] = [90, 70, 20, 80, 50], x = 45
    Output: No
    Explanation: No such pair exists.'''

def diff(arr,x):
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[j] - arr[i] == x:
                return True
    return False

arr =   [5, 20, 3, 2, 50, 80]
x = 78 
print(diff(arr,x))      