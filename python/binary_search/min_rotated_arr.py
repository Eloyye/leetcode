from typing import List


def findMin(nums: List[int]) -> int:
    left, right = 0, len(nums) - 1
    # curMin = nums[left] if len(nums) > 0 else 0
    while right > left:
        mid = left + (right - left) // 2
        if nums[mid] > nums[right]:
            #ascending sequence must start on the right array and doesn't include mid
            #[3 4 1 2]
            left = mid + 1
        else:
            #otherwise mid could be one of the potential candidates as well as the left portion of array
            #[4 1 2 3]
            right = mid
    return nums[left]

arr = [2,1]
print(findMin(arr))