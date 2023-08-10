import unittest
from typing import List


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0]*(amount + 1)

    def change2(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount + 1)
        dp[0] = 1

        for coin in coins:
            for i in range(coin, amount + 1):
                dp[i] += dp[i - coin]

        return dp[amount]


class Change2Solution(unittest.TestCase):
    def test1(self):
        sol = Solution()
        amount, coins = 5, [1, 2, 5],
        res = sol.change2(amount, coins)
        actual = 4
        self.assertEqual(res, actual)
    def test2(self):
        sol = Solution()
        amount, coins = 3, [2],
        res = sol.change2(amount, coins)
        actual = 0
        self.assertEqual(res, actual)
    def test3(self):
        sol = Solution()
        amount, coins = 10, [10],
        res = sol.change2(amount, coins)
        actual = 1
        self.assertEqual(res, actual)
