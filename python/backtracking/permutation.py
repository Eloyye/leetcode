import unittest
from typing import List

def permute(nums: List[int]) -> List[List[int]]:
    res = []
    if len(nums) == 1:
        return [nums.copy()]
    for _ in range(len(nums)):
        n = nums.pop(0)
        perms = permute(nums)

        for p in perms:
            p.append(n)

        res.extend(perms)

        nums.append(n)
    return res

class TestPermute(unittest.TestCase):

    def test_1(self):
        inp = permute([1])
        answer = [[1]]
        inp.sort()
        answer.sort()
        self.assertEquals(inp, answer)

    def test_2(self):
        inp = permute([1,2,3])
        answer = [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
        inp.sort()
        answer.sort()
        self.assertEquals(inp, answer)

# arr = [1, 2, 3, 4]
# res = []
# for i in range(len(arr)):
#     v = arr.pop(i)
#     res.append(arr.copy())
#     arr.insert(i, v)
# print(f'res = {res}')