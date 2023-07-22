from collections import defaultdict
from typing import List

#linear time complexity through Bucket sorting
def topKFrequent(nums: List[int], k: int) -> List[int]:
    count = defaultdict(int) # mapping val to frequency in nums
    freq = [[] for _ in range(len(nums) + 1)] # bucket containing values from [0, n]
    for n in nums:
        count[n] += 1
    for n, c in count.items(): # items() enumerates???
        freq[c].append(n)
    res = []
    #iterate through freq in reverse order because of most frequent
    # if we want a least frequent element, we iterate in increasing order
    for i in range(len(freq) - 1, -1, -1):
        # given all the elements, get top k frequent elements
        for n in freq[i]:
            res.append(n)
            if len(res) == k:
                return res

