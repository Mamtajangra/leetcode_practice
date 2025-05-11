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