from typing import List


def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
    if sum(cost) > sum(gas):
        return -1
    tank, start_position = 0,0
    for i in range(len(gas)):
        tank += gas[i] - cost[i] # this is the tank once we move out of i
        if tank < 0:
            #we want to reset
            start_position = i + 1
            tank = 0
    return start_position