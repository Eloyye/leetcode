from typing import List


def combinationSum(candidates: List[int], target: int) -> List[List[int]]:
    res = []
    def dfs(i, cur_list, total):
        if total == target :
            res.append(cur_list.copy())
            return
        #failure conditions
        if i >= len(candidates) or total > target:
            return
        # add it to current combinations
        cur_list.append(candidates[i])
        #find all the combinations that include itself
        dfs(i, cur_list, total + candidates[i])
        #finding all combinations by moving on to another candidate
        cur_list.pop()
        #finding all combinations that meet target
        dfs(i + 1, cur_list, total)
    dfs(0, [], 0)
    return res

inp = [2,3,6,7]
target = 7
res = combinationSum(inp, target)
print(f'combinationSum({inp}, {target}) = {res}')