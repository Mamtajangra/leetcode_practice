# Given an array arr[] of n integers where arr[i] represents the number of chocolates in ith packet. Each packet can have a variable number of chocolates. There are m students, the task is to distribute chocolate packets such that: 

#     Each student gets exactly one packet.
#     The difference between the maximum and minimum number of chocolates in the packets given to the students is minimized.


def choc_dist(nums,k):
    nums.sort()
    mini = float("inf")
    # i = 0
    j =0
    while j<=len(nums)-k:
        x = nums[j+k-1]-nums[j]
        if x<mini:
            mini = x
        j+=1    
    return mini        


nums = [7, 3, 2, 4, 9, 12, 56]
k = 3
print(choc_dist(nums,k))
