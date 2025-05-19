'''You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
'''

def max_profit1(prices):
    min_buy = prices[0]                      ##initialize first element is minimum
    max_profit = 0
    for price in prices:
        if price <  min_buy:
            min_buy = price                ##0(n)
        profit = price - min_buy
        if profit > max_profit:
            max_profit = profit
    return max_profit
prices =[7,1,5,3,6,4] 
print(max_profit1(prices))           



def max_profit(prices):
    M = []
    n = len(prices)                               ## o(n**2) 
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
#             if profit>maxi:                                ## o(n**2) 
#                 maxi = profit
#     return maxi 


# prices =[7,1,5,3,6,4] 
# print(max_profit(prices))
