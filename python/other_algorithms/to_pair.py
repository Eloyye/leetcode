def to_display_pair(nums):
    if not nums:
        return "()"
    else:
        return f"(pair {nums[0]} {to_display_pair(nums[1:])})"
def to_pair(nums):
    return to_pair_helper(nums, "nil")
def to_pair_helper(nums, end_str):
    if not nums:
        return end_str
    else:
        return f"pair({nums[0]}, {to_pair_helper(nums[1:], end_str)})"



nums = [3, 6, 8, 10, 1, 2, 1]
out = [1, 1, 2, 3, 6, 8, 10]
print(to_pair(nums))
print(to_display_pair(out))