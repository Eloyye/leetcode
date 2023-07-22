from typing import List


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