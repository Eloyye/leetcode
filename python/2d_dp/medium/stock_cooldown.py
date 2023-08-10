from enum import Enum
from typing import List


class StockDecision(Enum):
    BUY = 0
    SELL = 1
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp : dict[tuple[int, StockDecision], int] = {} # (position, buy or sell) -> maximum profit at position when buying or selling
        def dfs(position : int, decision: StockDecision) -> int:
            if position >= len(prices):
                return 0
            if (position, decision) in dp:
                return dp[(position, decision)]
            profit_when_hold = dfs(position + 1, decision)
            if decision == StockDecision.BUY:
                profit_from_buying = dfs(position + 1, StockDecision.SELL) - prices[position]
                dp[(position, decision)] = max(profit_when_hold, profit_from_buying)
            else:
                profit_from_selling = dfs(position + 2, StockDecision.BUY) + prices[position]
                dp[(position, decision)] = max(profit_when_hold, profit_from_selling)
            return dp[(position, decision)]

        return dfs(0, StockDecision.BUY)

        