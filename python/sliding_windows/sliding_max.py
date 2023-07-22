import collections
from typing import List


def maxSlidingWindow(nums: List[int], k: int) -> List[int]:
    #keep track of the maximum values of each window
    out = []
    # use a monotonically decreasing deque data structure to handle keeping max and removing
    q = collections.deque()
    # start with left and right pointers of windows problem
    l = r = 0
    #iterate until reaching nums
    while r < len(nums):
        #if the new value is greater than the tail of the deque, then we want to pop those values
        while q and nums[q[-1]] < nums[r]:
            q.pop()
        #append the final value onto the list
        q.append(r)

        #
        first_val_queue = q[0]
        if l > q[0]:
            q.popleft()
        # window is of size k, further iterations just shifts the window
        if (r + 1) >= k:
            out.append(nums[q[0]])
            l += 1
        r += 1
    return out

def maxSlidingWindow2(nums, k):
    deque = collections.deque() # deque storing the indices in monotonically decreasing order
    out = []
    l = r = 0
    while r < len(nums):
        while deque and nums[deque[-1]] < nums[r]:
            deque.pop()
        deque.append(r)
        if l > deque[0]:
            deque.popleft()
        if (r + 1) >= k:
            out.append(deque[0])
            l += 1
        r += 1
    return out

nums = [1,3,-1,-3,5,3,6,7]
k = 3
res = maxSlidingWindow(nums, k)
print(f"result: {res}")