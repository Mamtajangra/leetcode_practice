# brute force
def max_profit(prices):
    M = []
    n = len(prices)
    for i in range(n):
        for j in range(i+1,n):
            x = prices[j]-prices[i]
            if x>0:
                M.append(x)
    return max(M,default =0) 


prices =[7,1,5,3,6,4] 
print(max_profit(prices))



# or 

# def max_profit(prices):
#     maxi = 0
#     n = len(prices)
#     for i in range(n):
#         for j in range(i+1,n):
#             profit = prices[j]-prices[i]
#             if profit>maxi:
#                 maxi = profit
#     return maxi 


# prices =[7,1,5,3,6,4] 
# print(max_profit(prices))
