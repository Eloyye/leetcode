import heapq
import unittest
from collections import deque, defaultdict, Counter
from typing import List


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        task_frequency = Counter(tasks)
        count_max_heap = [-count for count in task_frequency.values()]
        heapq.heapify(count_max_heap)

        time = 0
        count_cooldown_queue = deque()
        while count_max_heap or count_cooldown_queue:
            time += 1
            if count_max_heap:
                # Processing from heap essentially "decrements" count, basically converging to 0
                processed_count = 1 + heapq.heappop(count_max_heap)
                # don't add it to the queue if dropped to 0, because at that point we are finished!
                if processed_count:
                    count_cooldown_queue.append([processed_count, time + n])
            #add items from queue back to the heap if cooldown is reached
            head_queue_cooldown_time = count_cooldown_queue[0][1] if count_cooldown_queue else None
            reachedCooldown = count_cooldown_queue and head_queue_cooldown_time == time
            if reachedCooldown:
                heapq.heappush(count_max_heap, count_cooldown_queue.popleft()[0])
        return time



class LeastIntervalTest(unittest.TestCase):
    def test1(self):
        sol = Solution()
        tasks = ["A","A","A","B","B","B"]
        n = 2
        out = sol.leastInterval(tasks, n)
        expected = 8
        self.assertEqual(out, expected)
    def test2(self):
        sol = Solution()
        tasks = ["A","A","A","B","B","B"]
        n = 0
        out = sol.leastInterval(tasks, n)
        expected = 6
        self.assertEqual(out, expected)

