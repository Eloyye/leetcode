def trap(height : list[int]) -> int:
    def collect_water(l, r, height, cur_water, direction):
        def update_anchor(anchor, direction):
            return anchor + 1 if direction == "left" else anchor - 1
        anchor = l if direction == "left" else r
        max_val = height[anchor]
        anchor = update_anchor(anchor, direction)
        while l < r and max_val > height[anchor]:
            cur_water += max_val - height[anchor]
            anchor = update_anchor(anchor, direction)
        return cur_water, anchor
    l, r = 0, len(height) - 1
    water = 0

    while l < r:
        if height[l] < height[r]:
            water, l = collect_water(l, r, height, water, "left")
        else:
            water, r = collect_water(l, r, height, water, "right")
    return water


def trap_(self, height : list[int]) -> int:
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

if __name__ == '__main__':
    print(trap([2,0,2]))