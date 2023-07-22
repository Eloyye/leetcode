from typing import List


def maxProfit(self, prices: List[int]) -> int:
    max_profit, min_buy = 0, float("infinity")
    for p in prices:
        min_buy = min(min_buy, p)
        max_profit = max(max_profit, p - min_buy)
    return max_profit

def maxProfit_neetcode(prices: List[int]) -> int:
    l, r = 0, 1
    max_profit = 0
    while r < len(prices):
        if prices[l] < prices[r]:
            profit = prices[r] - prices[l]
            max_profit = max(max_profit, profit)
        else:
            l += 1
        r += 1
    return max_profit