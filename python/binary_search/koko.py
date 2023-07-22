def minEatingSpeed(self, piles: List[int], h: int) -> int:
    def possible(k: int) -> bool:
        return ( (p - 1) // k  + 1 for p in piles ) <= h
    # instead of finding a value within an input array, we want to find a value within a range of
    # possible values
    left, right = 1, max(piles)
    while right > left:
        mid = left + (right - left) // 2
        if possible(mid):
            # we try to see if we can do better
            right = mid
        else:
            left = mid + 1
    # left == right
    return left