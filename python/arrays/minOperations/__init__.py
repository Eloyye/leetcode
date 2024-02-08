from collections import Counter


def min_operations_generalized(nums: list[int], allowed_operations: list[int]):
    freqs = Counter(nums)
    operations = 0
    allowed_operations.sort(reverse=True)
    for freq in freqs.values():
        for ops in allowed_operations:
            remain, vals = freq % ops, freq // ops


    return operations

def minOperations(nums: list[int]) -> int:
    freqs = Counter(nums)
    operations = 0
    for freq in freqs.values():
        if freq == 1:
            return -1
        remain = freq % 3
        num_threes = freq // 3
        num_twos = 0
        if remain == 1:
            num_threes = max(0, num_threes - 1)
            num_twos += 2
        elif remain == 2:
            num_threes = num_threes
            num_twos += 1
        operations += num_twos + num_threes
    return operations

if __name__ == '__main__':
    pass
