from typing import List
import unittest

def maxSubArray(nums: List[int]) -> int:
    #remember we can take in [-1] and we can have a negative maximum_subarray_total
    maximum_subarray_total = nums[0]
    current_subarray_total = 0
    for num in nums:
        current_subarray_total += num
        maximum_subarray_total = max(maximum_subarray_total, current_subarray_total)
        current_subarray_total = 0 if current_subarray_total < 0 else current_subarray_total
    return maximum_subarray_total


class maxSubArrayTest(unittest.TestCase):
    def test1(self):
        inp = [-2,1,-3,4,-1,2,1,-5,4]
        answer = 6
        self.assertEqual(maxSubArray(inp), answer)
    def test2(self):
        inp = [1]
        answer = 1
        self.assertEqual(maxSubArray(inp), answer)
    def test3(self):
        inp = [5,4,-1,7,8]
        answer = 23
        self.assertEqual(maxSubArray(inp), answer)