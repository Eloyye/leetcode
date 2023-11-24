def quicksort(nums: list[int]) -> list[int]:
    N = len(nums)
    # base case
    if N <= 1:
        return nums
    middle_index = N // 2
    pivot = nums[middle_index]
    # left and right is not sorted,
    # it's just guaranteed to be less than
    # or greater than the pivot, respectively
    left = [num for num in nums if num < pivot]
    middle = [num for num in nums if num == pivot]
    right = [num for num in nums if num > pivot]
    return quicksort(left) + middle + quicksort(right)

if __name__ == "__main__":
    nums = [3, 6, 8, 10, 1, 2, 1]
    res = quicksort(nums)
    print(res)
