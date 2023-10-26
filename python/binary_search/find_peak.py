import unittest
from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        nums.insert(0, float('-inf'))
        nums.append(float('-inf'))
        l, r = 1, len(nums) - 2
        while r > l:
            mid = (r + l) // 2
            max_nei = max(nums[mid - 1], nums[mid + 1])
            if nums[mid - 1] < nums[mid] and nums[mid + 1] < nums[mid]:
                return mid - 1
            elif max_nei == nums[mid - 1]:
                r = mid - 1
            else:
                l = mid + 1
        return l - 1

class Solution2(unittest.TestCase):
    def test1(self):
        nums = [1]
        sol = Solution().findPeakElement
        res = sol(nums)
        expected =
        self.assertEqual(expected, res)