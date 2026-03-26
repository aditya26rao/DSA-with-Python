def maxProfit(prices):
    min_price = float('inf')
    max_profit = 0
    for i in range(len(prices)):
        
        min_price = min(min_price,prices[i])
        max_profit = max(max_profit,prices[i] - min_price)
        
        # if prices[i] < min_price:
        #     min_price = prices[i]
        # else:
        #     profit = prices[i] - min_price
        #     if profit > max_profit:
        #         max_profit = profit
        
    return max_profit

# Driver code
prices = [7, 1, 5, 3, 6, 4]
result = maxProfit(prices)
print(result)
