from typing import List

# Floyd's Turtle and Hare
def findDuplicate(self, nums: List[int]) -> int:
    slow = fast = nums[0]

    while True:
        #advance the pointer
        slow = nums[slow] # next pointer; slow.next
        fast = nums[nums[fast]] # fast.next.next

        # we have detected a cycle, but it doesn't mean that current position
        # of slow and fast point to the duplicate val
        if fast == slow:
            break

    slow_start = nums[0]
    while slow_start != slow:
        slow = nums[slow]
        slow_start = nums[slow_start]

    return slow_start