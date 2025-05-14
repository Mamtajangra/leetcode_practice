#  Maximum Points You Can Obtain from Cards
'''There are several cards arranged in a row, and each card has an associated number of points. The points are given in the integer array cardPoints.

In one step, you can take one card from the beginning or from the end of the row. You have to take exactly k cards.

Your score is the sum of the points of the cards you have taken.

Given the integer array cardPoints and the integer k, return the maximum score you can obtain.

Example 1:

Input: cardPoints = [1,2,3,4,5,6,1], k = 3
Output: 12
Explanation: After the first step, your score will always be 1. However, choosing the rightmost card first will maximize your total score. The optimal strategy is to take the three cards on the right, giving a final score of 1 + 6 + 5 = 12.
'''
def max_points(cardPoints,k):
    max_score = 0
    for i in range(0,k+1):
        left = cardPoints[:i]
        right = cardPoints[len(cardPoints)-(k-i):]
        total = sum(left)+ sum(right)
        max_score = max(max_score,total)
    return max_score    

cardPoints = [1,2,3,4,5,6,1]
k = 3
print(max_points(cardPoints,k))