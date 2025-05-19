'''You are given an integer array prices where prices[i] is the price of a given stock on the ith day.

On each day, you may decide to buy and/or sell the stock. You can only hold at most one share of the stock at any time. However, you can buy it then immediately sell it on the same day.

Find and return the maximum profit you can achieve.
Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 7
Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
Total profit is 4 + 3 = 7.
'''
# /



# Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
# Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
# Total profit is 4 + 3 = 7.



def max_profit1(prices):
    profit = 0
    for i in range(1,len(prices)):
        if prices[i]>prices[i-1]:
            x = prices[i]-prices[i-1]
            profit = profit+x
    return profit        

prices=[7,1,5,3,6,4]
print(max_profit1(prices))


# optimum

def max_profit2(prices):
       min_buy = prices[0]   ## initialize first element is minimum
       max_profit = 0
       sell_price = 0
       total_profit = 0
       for price in prices:    ##searching over array if price < min then set it to min
        if price < min_buy:
            min_buy = price
        profit = price - min_buy    ## profit = subtraction of minimu from price
        if profit > max_profit:      ## if profit > max it mention in question set it to the sell price
            sell_price = price
            max_profit = profit


            min_buy = price         ## min = price , max_profit = profit 
            max_profit = profit 
            total_profit = total_profit + max_profit   

            max_profit = 0
       return total_profit


prices=[7,1,5,3,6,4]
print(max_profit2(prices))
