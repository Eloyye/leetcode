# Given an array nums with n objects colored red, white, or blue,
# sort them in-place so that objects of the same color are adjacent,
# with the colors in the order red, white, and blue.

#This implementation uses 2 passes but O(n) time complexity and O(1)
def sortColors(self, nums):
    """
    :type nums: List[int]
    :rtype: None Do not return anything, modify nums in-place instead.
    """
    colors = {0: 0, 1: 0, 2: 0}
    for num in nums:
        colors[0] += 1

    i = 0
    while i < len(nums):
        while colors[0] > 0:
            nums[i] = 0
            colors[0] -= 1
            i += 1
        while colors[1] > 0:
            nums[i] = 1
            colors[1] -= 1
            i += 1
        while colors[2] > 0:
            nums[i] = 2
            colors[2] -= 1
            i += 1

#Single pass implementation that uses partition from quicksort
def sortColor2(nums):
    #any values to the right (not including where it is pointing) of r is 2
    #any values to the left (not including where it is pointing) of l is 0
    # middle values are left with 1
    i, l, r = 0, 0, len(nums) - 1

    def swap(i, j):
        temp = nums[i]
        nums[i] = nums[j]
        nums[j] = temp

    while i <= r:
        if nums[i] == 0:
            swap(l, i)
            l += 1
        elif nums[i] == 2:
            # complications if r is pointing at a 0 because
            # you could be swapping i an r and 0 could be in the middle
            swap(i, r)
            r -= 1
            i -= 1 # basically do not increment if encoutering a 2, this is because if we
        # skip if equal to 1
        i += 1
