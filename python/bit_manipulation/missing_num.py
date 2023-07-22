import math
from typing import List
def missingNumber(nums: List[int]) -> int:
    def getXORList(size: int) -> int:
        prod = 0
        for n in range(1, size + 1):
            prod ^= n
        return prod
    prod = getXORList(len(nums))
    for n in nums:
        prod ^= n
    return prod

def missingNumber2(nums: List[int]) -> int:
    prod = len(nums)
    for i, n in enumerate(nums):
        prod = prod ^ n ^ i
    return prod

print(missingNumber2([3,0,1]))