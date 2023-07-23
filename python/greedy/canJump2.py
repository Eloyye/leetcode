import unittest
from typing import List


class Solution:
    # def jump(self, nums: List[int]) -> int:
    #     goalPost = len(nums) - 1
    #     num_jumps = 0
    #     i = len(nums) - 1
    #     while i >= 0:
    #         for j in range(i):
    #             if j + nums[j] >= goalPost:
    #                 goalPost = j
    #                 num_jumps += 1
    #                 i = goalPost + 1
    #                 break
    #         i -= 1
    #     return num_jumps
    def jump(self, nums: List[int]) -> int:
        farthest_reachable_position = num_jumps = last_position_from_prev_jump = 0
        for i in range(len(nums) - 1):
            farthest_reachable_position = max(farthest_reachable_position, i + nums[i])

            #this implicitly means that we haven't actually gone to the last position
            # jump isn't necessarily made at position i
            if i == last_position_from_prev_jump:
                last_position_from_prev_jump = farthest_reachable_position
                num_jumps += 1
        return num_jumps
class Jump2Test(unittest.TestCase):
    def test1(self):
        sol = Solution()
        nums = [2, 3, 1, 1, 4]
        result = sol.jump(nums)
        expected = 2
        self.assertEqual(result, expected)
    def test2(self):
        sol = Solution()
        nums =  [2,3,0,1,4]
        result = sol.jump(nums)
        expected = 2
        self.assertEqual(result, expected)
