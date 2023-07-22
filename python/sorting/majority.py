
#Given an array nums of size n, return the majority element.
#
#The majority element is the element that appears more than ⌊n / 2⌋ times.
#
# You may assume that the majority element always exists in the array.
def majorityElementHashMap(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    hm = {}
    res, maxCount = 0,0
    for n in nums:
        hm[n] = 1 + hm.get(n, 0)
        res = n if hm[n] > maxCount else res
        maxCount = max(maxCount, hm[n])
    return res


# We use the Boyer Moore's algorithm to do this O(n) time AND O(1) space complexity
# This uses the fact that there EXIST A MAJORITY ELEMENT
def majorityElement(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    # the idea is to keep track of the count of what we think is the majority, res and count
    # iterate through nums and increment count if num is res and decrement if it isn't
    # if decrement to -1, then reassign res to current value
    res, count = 0,0
    for n in nums:
        if count == 0:
            res = n
        count += (1 if n == res else -1)
    return res
