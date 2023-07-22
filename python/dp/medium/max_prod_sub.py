from typing import List
import unittest

def maxProduct(nums: List[int]) -> int:
    maxProductResult = nums[0]
    #start with multiplicative identity
    _maxProduct = _minProduct = 1
    for n in nums:
        _maxProduct, _minProduct = max(n, n * _maxProduct, n * _minProduct), min(n, n*_maxProduct, n*_minProduct)
        maxProductResult = max(maxProductResult, _maxProduct)
    return maxProductResult


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
