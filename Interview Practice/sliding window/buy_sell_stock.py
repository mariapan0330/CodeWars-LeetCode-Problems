"""
Given an array representing the price of a given stock on day i, return the maximum profit you 
can earn. Note that you cannot sell a stock before you buy it. If you cannot turn a profit,
return 0.

INP: [7,1,5,3,6,4]
OUT: 5
WHY: buy on day i = 1 (price = 1) and sell on day i = 4 (price = 6), profit = 6-1 = 5
"""

def stock_max_profit(prices):
    # PLAN: left and right pointer, left = buy, right = sell
    # right pointer is the current position in for loop
    # if current position is less than buy, buy = curr
    # if it's greater than buy and greater than sell, sell = curr and update profit
    profit = 0
    buy = 0 # buy starts off at index 0
    for i, curr in enumerate(prices):
        if curr < prices[buy]:
            buy = i
        elif prices[i] - prices[buy] > profit:
            profit = prices[i] - prices[buy]
    return profit


inp1 = [7,1,5,3,6,4]
print(stock_max_profit(inp1))