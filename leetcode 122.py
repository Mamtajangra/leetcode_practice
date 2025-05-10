def total_profit(prices):
    maxi = 0
    result = 0
    for i in range(len(prices)):
        profit = prices[i] - prices[i-1]
        if profit>maxi:
            result = result + profit
    return result 



prices = [7,1,5,3,6,4]
print(total_profit(prices))



# Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
# Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
# Total profit is 4 + 3 = 7.