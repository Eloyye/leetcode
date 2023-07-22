from typing import List
import unittest
#     Take the sum of entire nums and see if it does not divide by 2 -> cannot partition equally

def canPartition(self, nums: List[int]) -> bool:
    total = sum(nums)
    total_sum_is_odd = total % 2
    if total_sum_is_odd:
        return False
    dp = set()
    dp.add(0)
    target = total // 2
    for i in range(len(nums) -1, -1, -1):
        nextDP = set()
        for t in dp:
            if (t + nums[i]) == target:
                return True
            nextDP.add(t + nums[i])
            nextDP.add(t)
        dp = nextDP

    return False

def canPartition2(nums: List[int]) -> bool:
    total_sum = sum(nums)
    if total_sum % 2 != 0:
        return False
    target_sum = total_sum // 2
    dp = [False] * (target_sum + 1)
    dp[0] = True
    for num in nums:
        for i in range(target_sum, num - 1, -1):
            dp[i] = dp[i] or dp[i - num]
    return dp[target_sum]

def canPartition3(nums: List[int]) -> bool:
    total_sum = sum(nums)
    if total_sum % 2:
        return False
    target_num = total_sum // 2
    dp = [False]*(target_num + 1)
    dp[0] = True
    for n in nums:
        for i in range(target_num, n - 1, -1):
            dp[i] = dp[i] or dp[i - n]
    return dp[target_num]

class CanPartitionTest(unittest.TestCase):
    def test1(self):
        nums = [1,5,11,5, 7, 13]
        ans = True
        self.assertEqual(canPartition2(nums), ans)
