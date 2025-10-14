'''There are several cards arranged in a row, and each card has an associated number of points. The points are given in the integer array cardPoints.
In one step, you can take one card from the beginning or from the end of the row. You have to take exactly k cards.
Your score is the sum of the points of the cards you have taken.
Given the integer array cardPoints and the integer k, return the maximum score you can obtain.

Example 1:

Input: cardPoints = [1,2,3,4,5,6,1], k = 3
Output: 12
Explanation: After the first step, your score will always be 1. However, choosing the rightmost card first will maximize your total score. The optimal strategy is to take the three cards on the right, giving a final score of 1 + 6 + 5 = 12.
'''
def max_score(cardPoints,k):
    n = len(cardPoints)
        # initialize left and right pointer in front side means in window 
    left = 0
    right = n-k-1   ## length of list - window -1
    k_sum = 0       ## suppose sum is zero
    for i in range(n-k,n):    ## sum of k having range next to the right upto length of list
        k_sum += cardPoints[i]
        max_sum = k_sum  
        # loop upto length - 1  
    while right < n-1:  
            # one member added to the right then ksum subtract that value    
        right = right +1
        k_sum = k_sum - cardPoints[right]

            # added that number to the left and also move left index
        k_sum = k_sum +cardPoints[left]
        left = left +1    
        max_sum = max(max_sum, k_sum)
    return max_sum 


# check
cardPoints = [1,2,3,4,5,6,1]
k = 3
print(max_score(cardPoints,k))








