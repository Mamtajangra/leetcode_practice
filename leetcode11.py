'''

You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.
Example 1:

Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
'''
# container with most water
def most_water(height):
    max_area = 0
    n = len(height)
    for i in range(n):
            for j in range(i+1,n):
                # height of lines are minimum 
                h = min(height[i],height[j])
                w = j-i
                area = w*h
                max_area=max(max_area,area)
    return max_area    



height =  [1,8,6,2,5,4,8,3,7]
print(most_water(height))


''' The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.'''
# two pointer


 # use two pointer
        #calculate area
        # max_area
        # move left, right according to max_area 

def most_water1(height):
    maximum = 0
    left = 0
    right = len(height)-1
    while left < right:
        w = right - left
        h = min(height[left],height[right])
        area = w * h 
        maximum = max(maximum,area)
        if height[left] < height[right]:
             left += 1
        else:
             right -= 1
    return maximum  


height =  [1,8,6,2,5,4,8,3,7]
print(most_water1(height))
         
