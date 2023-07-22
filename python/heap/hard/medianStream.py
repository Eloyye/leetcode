import heapq
import unittest


class MedianFinder:

    def __init__(self):
        self.lowPartition, self.highPartition = [], [] #lp := max heap; hp := min heap
    def addNum(self, num: int) -> None:
        if len(self.lowPartition) == len(self.highPartition):
            heapq.heappush(self.highPartition, -heapq.heappushpop(self.lowPartition, -num))
        else:
            heapq.heappush(self.lowPartition, -heapq.heappushpop(self.highPartition, num))
    def findMedian(self) -> float:
        if len(self.lowPartition) == len(self.highPartition):
            return (self.lowPartition[0] + self.highPartition[0]) / 2.0
        else:
            return float(self.highPartition[0])

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()

class MedianStream(unittest.TestCase):
    def test1(self):
        mf = MedianFinder()
        mf.addNum(1)
        mf.addNum(2)
        self.assertEqual(mf.findMedian(), 1.5)
        mf.addNum(3)
        self.assertEqual(mf.findMedian(), 2.0)
        mf.addNum(4)
        self.assertEqual(mf.findMedian(), 2.5)
    def test2(self):
        mf = MedianFinder()
        mf.addNum(-1)
        self.assertEqual(mf.findMedian(), -1.0)
        mf.addNum(-2)
        self.assertEqual(mf.findMedian(), -1.5)
        mf.addNum(-3)
        self.assertEqual(mf.findMedian(), -2.0)
        mf.addNum(-4)
        self.assertEqual(mf.findMedian(), -2.5)
        mf.addNum(-5)
        self.assertEqual(mf.findMedian(), -3.0)
    def test3(self):
        mf = MedianFinder()
        for i in range(1, 11):
            mf.addNum(i)
            mf.findMedian()