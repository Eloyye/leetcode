def maxArea(self, height):
    """
    :type height: List[int]
    :rtype: int
    """
    l, r = 0, len(height) - 1
    max_val = 0
    # idea is that we only want to move to try to increase the height
    while r > l:
        area = min(height[l], height[r]) * (r - l)
        max_val = max(area, max_val)
        if height[r] > height[l]:
            #we want to see if left pointer can do better
            l += 1
        else:
            # see if the right pointer can do better
            r -= 1
    return max_val