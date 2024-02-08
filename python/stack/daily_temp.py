from typing import List


class Solution:
    def daily_temperatures(self, temperatures : List[int]) -> List[int]:
        stack, res = [], [0]*len(temperatures)
        for i, temp in temperatures:
            if stack and temp > stack[-1][1]:
                i_, _ = stack.pop()
                res[i_] = i - i_
            stack.append((i, temp))
        return res
def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
    #default value if there are remaining stack is 0
    res = [0] * len(temperatures)
    stack = [] # pair: [temp, index]

    #iterate through temperatures
    for i, t in enumerate(temperatures):
        while stack and t > stack[-1][0]:
            stackT, stackIndex = stack.pop()
            res[stackIndex] = (i - stackIndex)
        stack.append([t, i])
    return res