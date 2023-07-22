#Given an array of integers nums which is sorted in ascending order, and an integer target,
# write a function to search target in nums.
# If target exists, then return its index. Otherwise, return -1.
from typing import List


#You must write an algorithm with O(log n) runtime complexity.
def search(self, nums: List[int], target: int) -> int:
    left, right = 0, len(nums) - 1
    # >= because we want to also allow the case of len(nums) == 1
    while right >= left:
        mid = (right + left) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            #target must be on the right of mid
            #we have already checked mid so we want the pointer to the right mid
            left = mid + 1
        else:
            #target on left of mid
            right = mid - 1
    return -1