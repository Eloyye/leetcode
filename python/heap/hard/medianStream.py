import heapq
import unittest


# heapq implements a minheap
class MaxHeap:
    def __init__(self):
        self.max_heap = []

    def peek(self):
        return self.max_heap[0]

    def push(self, num: int):
        heapq.heappush(self.max_heap, -num)

    def push_and_pop(self, num: int) -> int:
        return -heapq.heappushpop(self.max_heap, -num)

    def pop(self) -> int:
        return -heapq.heappop(self.max_heap)

    def size(self) -> int:
        return len(self.max_heap)


class MinHeap:
    def __init__(self):
        self.min_heap = []

    def peek(self):
        return self.min_heap[0]

    def push(self, num: int):
        heapq.heappush(self.min_heap, num)

    def push_and_pop(self, num: int) -> int:
        return heapq.heappushpop(self.min_heap, num)

    def pop(self) -> int:
        return heapq.heappop(self.min_heap)

    def size(self) -> int:
        return len(self.min_heap)


class MedianFinder2:
    def __init__(self):
        self.low_partition, self.high_partition = MaxHeap(), MinHeap()

    def add_num(self, num: int):
        if self.low_partition.size() == self.high_partition.size():
            self.high_partition.push(self.low_partition.push_and_pop(num))
        else:
            self.low_partition.push(self.high_partition.push_and_pop(num))

    def find_median(self) -> float:
        if self.low_partition.size() == self.high_partition.size():
            return (self.low_partition.peek() + self.high_partition.peek()) / 2.0
        return float(self.high_partition.peek())


class MedianFinder:

    def __init__(self):
        self.lowPartition, self.highPartition = [], []  # lp := max heap; hp := min heap

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
