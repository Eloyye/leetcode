from typing import List


def longestConsecutive(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    numsFast = set(nums)
    longest = 0
    for n in nums:
        if (n - 1) not in numsFast:
            length = 1
            while n + length in numsFast:
                length += 1
            longest = max(longest, length)
    return longest

longestConsecutive([-1, 1, 0])