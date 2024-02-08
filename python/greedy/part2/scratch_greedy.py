def can_complete_circuit(gases: list[int], costs: list[int]) -> int:
    if sum(costs) > sum(gases):
        return -1
    tank, start = 0, 0
    for i, gas, cost in enumerate(zip(gases,costs)):
        tank += gas - cost
        if tank < 0:
            start = i + 1
            tank = 0
    return start
