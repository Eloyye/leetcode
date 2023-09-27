from collections import Counter
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # freq -> list of nums that corresponds to freq
        count = Counter(nums)
        freq_to_nums = [[] for _ in range(len(nums) + 1)]
        for num, freq in count.items():
            freq_to_nums[freq].append(num)
        res = []
        for i in range(len(freq_to_nums) - 1, - 1, -1):
            for num in freq_to_nums[i]:
                res.append(num)
                if len(res) == k:
                    return res