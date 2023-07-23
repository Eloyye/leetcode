import unittest
from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        end_pos = len(nums) - 1
        goal_post =  end_pos
        for i in range(end_pos, -1, -1):
            max_position_reachable = i + nums[i]
            if max_position_reachable >= goal_post:
                #move goalpost because if we can reach to this goalpost, then we can reach to the last position
                goal_post = i
        return not goal_post
class CanJumpTest(unittest.TestCase):
    def test1(self):
        sol = Solution()
        nums = [2,3,1,1,4]
        self.assertTrue(sol.canJump(nums))
    def test2(self):
        sol = Solution()
        nums = [3,2,1,0,4]
        self.assertFalse(sol.canJump(nums))
    def test3(self):
        sol = Solution()
        nums = [1,1, 0, 1]
        self.assertFalse(sol.canJump(nums))
    def test3(self):
        sol = Solution()
        nums = [5,9,3,2,1,0,2,3,3,1,0,0]
        self.assertTrue(sol.canJump(nums))

