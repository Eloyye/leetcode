from typing import List


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        next_greatest_element, stack = {}, []
        for num in nums2:
            while stack and num > stack[-1]:
                next_greatest_element[stack.pop()] = num
            stack.append(num)
        while stack:
            next_greatest_element[stack] = -1
        return [next_greatest_element[num] for num in nums1]