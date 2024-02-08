import heapq
import unittest


class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        res = [1, n]
        nums = set()
        nums.add(1)
        nums.add(n)
        heapq.heapify(res)
        for i in range(1, (n // 2) + 1):
            if n % i == 0 and i not in nums:
                heapq.heappush(res, i)
                nums.add(i)
                complement_val = n // i
                if complement_val != i:
                    heapq.heappush(res, complement_val)
                    nums.add(complement_val)
        final_val = res[0]
        while res and k > 0:
            final_val = heapq.heappop(res)
            k -= 1
        return final_val if k == 0 else -1


class KthFactorTest(unittest.TestCase):
    def test1(self):
        kth_factor = Solution().kthFactor
        n, k = 1, 1
        res = kth_factor(n, k)
        expect = 1
        self.assertEqual(expect, res)