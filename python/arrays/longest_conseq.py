def longestConsecutive(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if len(nums) == 0:
        return 0
    my_set = {num for num in nums}
    longest = 1
    longest_so_far = 1
    for i, num in enumerate(nums):
        if i > 0 and (num - 1 not in my_set):
            # end of set and count
            while num + longest_so_far in my_set:
                longest_so_far += 1
                if (longest_so_far > longest):
                    longest = longest_so_far
            longest_so_far = 1
    return longest

longestConsecutive([-1, 1, 0])