import unittest
from typing import List

class Solution:
    def reverse_list(self, nums : List[int]) -> List[int]:
        left, right = 0, len(nums) - 1
        while right > left:
            nums[left], nums[right] = nums[right], nums[left]
            right -= 1
            left += 1
        return nums

class ReverseListTest(unittest.TestCase):
    def test1(self):
        sol = Solution()
        nums = [1, 2, 3, 4, 5]
        res = sol.reverse_list(nums.copy())
        expected = nums.copy()
        expected.reverse()
        self.assertEqual(expected, res)

