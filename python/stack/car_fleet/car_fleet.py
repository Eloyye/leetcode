from typing import List


def car_fleet2(target: int, positions: List[int], speeds: List[int]) -> int:
    pair = [(position, speed) for position, speed in zip(positions, speeds)]
    stack = []
    for position, speed in sorted(pair)[::-1]:
        time_to_target = (target - position) / speed
        stack.append(time_to_target)
        if len(stack) >= 2 and stack[-1] <= stack[-2]:
            stack.pop()
    return len(stack)


def car_fleet(target: int, position: List[int], speed: List[int]) -> int:
    pair = [[p, s] for p, s in zip(position, speed)]

    #stack here keeps track of the number of car fleets
    # the order of the stack goes from decreasing initial position
    stack = []
    # Reverse Sorted Order
    for p, s in sorted(pair)[::-1]:
        stack.append((target - p) / s)
        if len(stack) >= 2 and stack[-1] <= stack[-2]:
            stack.pop()
    return len(stack)
