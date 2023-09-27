from typing import List


class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        n = len(nums)
        dp = {}
        def dfs(l: int, r:int) -> int:
            if l > r:
                return 0
            if (l, r) in dp:
                return dp[(l,r)]
            dp[(l,r)] = 0
            for i in range(l, r + 1):
                #remeber we are popping this value last so l - 1 gives the "boundary" and r + 1 is also a boundary
                coins = nums[l - 1]* nums[i] * nums[r + 1]
                #solve two different subproblems
                coins += dfs(l, i - 1) + dfs(i + 1, r)
                dp[(l,r)] = max(dp[(l,r)], coins)
            return dp[(l,r)]
        return dfs(1, n - 2)

    #we need to find the last balloon to burst
    def maxCoins2(self, nums : List[int]) -> int:
        nums = [1] + nums + [1]
        n = len(nums)
        dp = [[0]* n for _ in range(n)]
        # for each of the subarrays
        for l in range(n - 2, -1, -1):
            for r in range(l + 2, n):
                # find the maximum if we pop position k last
                for k in range(l + 1, r):
                    coins = nums[l] * nums[k] * nums[r]
                    dp[l][r] = max(dp[l][r], dp[l][k] + coins + dp[k][r])
        return dp[0][n - 1]
    def maxCoins2(self, nums : List[int]) -> int:
        nums = [1] + nums + [1]
        n = len(nums)
        max_coins_between = [[0]*n for _ in range(n)]
        # we don't want to start our bounds in the right padding
        for left_bound in range(n - 2, -1, -1):
            for right_bound in range(left_bound + 2, n):
                for k in range(left_bound + 1, right_bound):
                    coins = nums[left_bound] * nums[k] * nums[right_bound]
                    max_coins_between[left_bound][right_bound] = max(max_coins_between[left_bound][right_bound], max_coins_between[left_bound][k] + coins + max_coins_between[k][right_bound])
        return max_coins_between[0][n - 1]

