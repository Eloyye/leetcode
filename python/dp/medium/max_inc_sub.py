from typing import List
import unittest

def lengthOfLIS2(nums: List[int]) -> int:
    dp = [1 for _ in range(len(nums) + 1)]
    max_value = dp[0]
    for i in range(len(nums) -1, -1, -1):
        for j in range(i + 1, len(nums)):
            if nums[j] > nums[i]:
                dp[i] = max(dp[i], 1 + dp[j])
                max_value = max(dp[i], max_value)
    return max_value


def lengthOfLIS(nums: List[int]) -> int:
    dp = [1 for _ in range(len(nums) + 1)]
    for i in range(len(nums) - 1, -1 , -1):
        for j in range(i + 1, len(nums)):
            if nums[j] > nums[i]:
                dp[i] = max(dp[i], 1 + dp[j])
    return max(dp)

def lengthOfLISubarray(nums: List[int]) -> int:
    max_len = 1
    cur_max_len = 0
    prevValue = float("-infinity")
    for n in nums:
        cur_max_len = 1 + cur_max_len if n > prevValue else 1
        prevValue = n
        max_len = max(max_len, cur_max_len)
    return max_len


class lengthOfLISTest(unittest.TestCase):
    def test1(self):
        nums = [10,9,2,5,3,7,101,18]
        answer = 4
        self.assertEqual(lengthOfLIS(nums), 4)