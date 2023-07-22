from typing import List


def subsets(nums: List[int]) -> List[List[int]]:
    res = []
    def dfs(i, subset):
        #base case if we iterate through all of nums
        if i == len(nums):
            res.append(subset)
            return
        #include nums[i]
        subset.append(nums[i])
        dfs(i + 1, subset)
        subset.pop()
        #not include nums[i]
        dfs(i + 1, subset)
    dfs(0, [])
    return res