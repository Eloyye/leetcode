from typing import List
import unittest

def rob(self, nums: List[int]) -> int:
    nums.append(0)
    for i in range(len(nums) - 4, -1, -1):
        nums[i] += max(nums[i + 2], nums[i + 3])
    return max(nums[0], nums[1])

class RobTest(unittest.TestCase):
    def test1(self):
        inp = [1,2,3,1]
        out = 4
        self.assertEqual(rob(self, inp), out)
    def test2(self):
        inp = [2,7,9,3,1]
        out = 12
        self.assertEqual(rob(self, inp), out)
    def test3(self):
        inp = [2,1,1,2]
        out = 4
        self.assertEqual(rob(self, inp), out)