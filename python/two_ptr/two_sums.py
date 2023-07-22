def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    visited = {}
    for i, num in enumerate(nums):
        if visited[target - num]:
            return [visited.get(target - num), i]
        else:
            visited[num] = i

twoSum([2,7,11,15], 9)