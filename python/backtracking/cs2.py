from typing import List


def combinationSum2(candidates: List[int], target: int) -> List[List[int]]:
    res = []
    #sort to prepare to get rid of duplicates
    candidates.sort()
    def dfs(i, subset, total):
        #total sum in subset is equal to target
        if total == target:
            res.append(subset.copy())
            return
        #total sum is invalid, greater than target or exceeding i
        if i == len(candidates) or total > target:
            return
        #incude candidates[i]
        subset.append(candidates[i])
        dfs(i + 1, subset, total + candidates[i])
        subset.pop()
        #not include candidates[i]
        while (i + 1) < len(candidates) and candidates[i] == candidates[i + 1]:
            i += 1
        dfs(i + 1, subset, total)
    dfs(0, [], 0)
    return res