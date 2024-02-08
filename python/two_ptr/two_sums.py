from collections import Counter
from typing import List

class Solution:
    def topKFrequent2(self, nums: List[int], k: int) -> List[int]:
        def create_bucket(nums : list[int]):
            count = Counter(nums)
            freq_to_nums = [[] for _ in range(len(nums) + 1)]
            for num, freq in count.items():
                freq_to_nums[freq].append(num)
            return freq_to_nums
        # using bucket sort because we are concerned about the frequency so
        freq_to_nums = create_bucket(nums)
        res = []
        # frequency iterated in descending order
        for i in range(len(freq_to_nums) - 1, -1, -1):
            for num in freq_to_nums[i]:
                res.append(num)
                if len(res) == k:
                    return res
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
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        complements_to_index = {}
        for i, n in enumerate(nums):
            if n in complements_to_index:
                return [complements_to_index[n], i]
            complements_to_index[n] = i

