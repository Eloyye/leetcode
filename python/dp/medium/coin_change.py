from typing import List


def coinChange(self, coins: List[int], amount: int) -> int:
    invalid_value = amount + 1 # this could be float('-infinity')
    dp = [invalid_value] *(amount + 1)
    dp[0] = 0 # change that sum up to 0 is just 0

    for total_value in range(1, amount + 1):
        for coin_value in coins:
            coins_total_after_spent = total_value - coin_value
            isSpentTooMuch = coins_total_after_spent >= 0
            if isSpentTooMuch:
                dp[total_value] = min(dp[total_value], 1 + dp[coins_total_after_spent])
    isPossible = dp[amount] != invalid_value
    return dp[amount] if isPossible else -1

def coinChange2(self, coins: List[int], amount: int) -> int:
    invalid_value = float("infinity")
    dp = [invalid_value]*(amount + 1)
    #base case
    dp[0] = 0
    for total_value in range(1, amount + 1):
        for coin_value in coins:
            value_after_spent = total_value - coin_value
            isValidChange = value_after_spent >= 0
            if isValidChange:
                # minimum of choice of choosing ONE coin
                dp[total_value] = min(dp[total_value], 1 + dp[value_after_spent])
    isValid = dp[amount] != invalid_value
    return dp[amount] if isValid else -1
