from typing import List


class Solution:

    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        for i, num in enumerate(nums):
            if num <= 0:
                nums[i] = n + 2
        for i, num in enumerate(nums):
            if (num - 1) < n and (num - 1) > -1:
                ab = abs(nums[num - 1])
                nums[num - 1] = - ab

        for i, num in enumerate(nums):
            if num > 0:
                return i + 1

