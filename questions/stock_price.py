#stock_prices_yesterday = [10, 7, 5, 8, 11, 9]
stock_prices_yesterday = [10, 7, 3]

def get_max_profit(prices):
    max_profit = prices[1] - prices[0]
    min_price = prices[0]

    for i in range(1, len(prices)):
        price = prices[i]

        profit = price - min_price

        max_profit = max(max_profit, profit)

        min_price = min(min_price, price)

    return max_profit

max_profit = get_max_profit(stock_prices_yesterday)
print(max_profit)
# returns 6 (buying for $5 and selling for $11)
