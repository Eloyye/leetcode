import unittest


class Solution:
    def partitionString(self, s: str) -> int:
        nums = set()
        min_partitions = 0
        for c in s:
            if c in nums:
                min_partitions += 1
                nums.clear()
            nums.add(c)
        min_partitions += 1
        return min_partitions

class PartitionStringTests(unittest.TestCase):
    def test1(self):
        s = "abacaba"
        partition_string = Solution().partitionString
        expect = 4
        res = partition_string(s)
        self.assertEqual(expect, res)
    def test2(self):
        s = "ssssss"
        partition_string = Solution().partitionString
        expect = 6
        res = partition_string(s)
        self.assertEqual(expect, res)