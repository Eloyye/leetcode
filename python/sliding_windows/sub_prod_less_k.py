def numSubarrayProductLessThanK(self, nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: int
    """
    if k <= 1:
        return 0
    prod = 1
    ans = left = 0
    for right, val in enumerate(nums):
        prod *= val
        while prod >= k: # condition is violated
            prod /= nums[left] #shrink the sliding window by removing the value pointer at start
            left += 1 #shrink sliding window
        ans += right - left + 1 # number of combinations is length of current subarray that includes RIGHT

    return ans

# def structure_of_sliding_window(arr):
#     left = 0
#     right = 0
#     while right < len(arr):
#         if condition is not met:
#             left +=1
#         right += 1