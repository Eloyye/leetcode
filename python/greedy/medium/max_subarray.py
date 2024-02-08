from typing import List
import unittest

def maxSubArray2(nums: List[int]) -> int:
    res, cur_sum = nums[0], 0
    for num in nums:
        cur_sum += num
        res = max(res, cur_sum)
        cur_sum = max(0, cur_sum)
    return cur_sum


def maxSubArray(nums: List[int]) -> int:
    max_subarray_result = nums[0]
    current_sum = 0
    for n in nums:
        current_sum += n
        max_subarray_result = max(max_subarray_result, current_sum)
        current_sum = max(0, current_sum)
    return max_subarray_result


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