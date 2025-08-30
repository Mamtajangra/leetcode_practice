'''Given the coordinates of four points in 2D space p1, p2, p3 and p4, return true if the four points construct a square.
The coordinate of a point pi is represented as [xi, yi]. The input is not given in any order.
A valid square has four equal sides with positive length and four equal angles (90-degree angles).
Example 1:

Input: p1 = [0,0], p2 = [1,1], p3 = [1,0], p4 = [0,1]
Output: true'''

def square(p1,p2,p3,p4):
    if p1==p2==p3==p4:
        return False
    def dist(x,y):
        return ((x[0]-y[0])**2 + (x[1]-y[1])**2)
    total_dist = [dist(p1,p2),dist(p2,p3),dist(p3,p4),dist(p4,p1),dist(p1,p3),dist(p2,p4)] 
    total_dist.sort()
    if total_dist[0]== total_dist[1]== total_dist[2]==total_dist[3] and total_dist[4]==total_dist[5] :
        return True
    return False



p1 = [0,0]
p2 = [1,1]
p3 = [1,0]
p4 = [0,1]
print(square(p1,p2,p3,p4))


