def trap(self, height):
    """
    :type height: List[int]
    :rtype: int
    """
    left, right = 0, len(height) - 1
    water = 0

    while right > left :
        if height[left] < height[right]: # we want to see if we can improve on left pointer
            max_left = height[left]
            left += 1 #increment
            while left < right and max_left >= height[left]: # trapping water, any elevation below is water
                water += max_left - height[left]
                left += 1
        else:
            #very similar condition for trying to improve right pointer
            max_right = height[right]
            right -= 1
            while left < right and max_right >= height[right]:
                water += max_right - height[right]
                right -= 1
    return water