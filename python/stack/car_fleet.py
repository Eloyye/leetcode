from typing import List


def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
    pair = [[p, s] for p, s in zip(position, speed)]

    #stack here keeps track of the number of car fleets
    # the order of the stack goes from decreasing initial position
    stack = []
    # Reverse Sorted Order
    for p, s in sorted(pair)[::-1]:
        stack.append(stack(target - p) / s)
        if len(stack) >= 2 and stack[-1] <= stack[-2]:
            stack.pop()
    return len(stack)
