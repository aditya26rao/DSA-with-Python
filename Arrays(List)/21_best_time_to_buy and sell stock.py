def buyStockSellStock(prices):
    # -------------------------------
    # Method 1: Brute Force
    # TC: O(n^2)
    # SC: O(1)
    # -------------------------------
    # n = len(prices)
    # max_profit = 0
    #
    # for i in range(n):
    #     for j in range(i+1, n):
    #         if prices[j] > prices[i]:
    #             max_profit = max(max_profit, prices[j] - prices[i])
    #
    # return max_profit

    # -------------------------------
    # Method 2: Two Pointers
    # TC: O(n)
    # SC: O(1)
    # -------------------------------
    # left = 0   # buy day
    # right = 1  # sell day
    # max_profit = 0
    #
    # while right < len(prices):
    #     if prices[right] > prices[left]:
    #         profit = prices[right] - prices[left]
    #         max_profit = max(max_profit, profit)
    #     else:
    #         left = right  # shift buy day to cheaper price
    #     right += 1
    #
    # return max_profit

    # -------------------------------
    # Method 3: Optimal Solution
    # TC: O(n)
    # SC: O(1)
    # -------------------------------
    min_price = float("inf")
    max_profit = 0

    for price in prices:
        
        # update min_price if current price is lower
        min_price = min(price, min_price)
        # calculate profit if sold today and update max_profit
        max_profit = max(max_profit, price - min_price)
        
        # if price < min_price:
        #     min_price = price
        # else:
        #     profit = price - min_price
        #     if profit > max_profit:
        #         max_profit = profit

    return max_profit


# Example usage
prices = [7, 2, 1, 5, 6, 4, 8]
print(buyStockSellStock(prices))  # Output: 7
