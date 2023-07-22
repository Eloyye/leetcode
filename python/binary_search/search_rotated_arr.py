from typing import List


def search(nums: List[int], target: int) -> int:
    left, right = 0, len(nums) - 1
    while right >= left:
        mid = left + (right - left) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] >= nums[left]:
            #left portion is sorted
            if target >= nums[left] and target < nums[mid]:
                right -= 1
            else:
                left += 1
        else:
            #right portion is sorted
            if target <= nums[right] and target > nums[mid]:
                left = mid + 1
            else:
                right = mid - 1
    return -1

def search2(nums: List[int], target: int) -> int:
    l, r = 0, len(nums) - 1
    while r >= l:
        m = l + (r - l) // 2
        if nums[m] == target:
            return m
        elif nums[m] >= nums[l]:
            if target >= nums[l] and target < nums[m]:
                r = m - 1
            else:
                l = m + 1
        else:
            if target <= nums[r] and target > nums[m]:
                l = m + 1
            else:
                r = m - 1
    return -1


nums = [4,5,6,7,0,1,2]
target = 0
print(search(nums, target))