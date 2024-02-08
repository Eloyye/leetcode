import random
from collections import Counter


def majority_is_odd(nums: list[int]) -> bool:
    max_val, max_freq = float('-inf'), float('-inf')
    for num, freq in Counter(nums[:3]).items():
        if freq > max_freq:
            max_val, max_freq = num, freq
    return max_val % 2 == 1

def find_outlier(nums: list[int]) -> int:
    if len(nums) < 3:
        raise Exception("Error: majority_is_odd has too few arguments")
    is_odd = majority_is_odd(nums)
    for n in nums:
        if is_value_outlier(is_odd, n):
            return n
    raise Exception('Error: majority_is_odd somehow did not return')


def is_value_outlier(condition, n):
    return n % 2 == condition


if __name__ == '__main__':
    input_list = [num for num in range(100) if num % 2 == 0] + [5]
    random.shuffle(input_list)
    print(input_list)
    print(find_outlier(input_list))
