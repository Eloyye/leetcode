from typing import List


def largestRectangleArea(self, heights: List[int]) -> int:
    maxArea = 0
    #maintain an increasing order stack
    stack = [] # pair: (index, height)

    for i, h in enumerate(heights):
        # we don't know if we can extend it backwards
        start = i
        while stack and stack[-1][1] > h:
            index, height = stack.pop()
            maxArea = max(maxArea, height * (i - index))
            start = index
        stack.append((start, h))

    for i, h in stack:
        maxArea = max(maxArea, h * (len(heights) - i))
    return maxArea

