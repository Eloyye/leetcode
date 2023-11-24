from typing import List
import unittest

def maxProduct(nums: List[int]) -> int:
    max_product_result = nums[0]
    temp_max = temp_min = 1
    for num in nums:
        temp_max = max(num, num * temp_max, num * temp_min)
        temp_min = min(num, num * temp_max, num * temp_min)
        max_product_result = max(max_product_result, temp_max)
    return max_product_result

class MaxProductTest(unittest.TestCase):
    def test1(self):
        nums = [2, 3, -2, 4]
        out = 6
        self.assertEqual(maxProduct(nums), out)
    def test2(self):
        nums = [-2, 0, -1]
        out = 0
        self.assertEqual(maxProduct(nums), out)
    def test3(self):
        nums = [-3,-1,-1]
        out = 3
        self.assertEqual(maxProduct(nums), out)
