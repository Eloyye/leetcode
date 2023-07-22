def countBits(self, n):
    """
    :type n: int
    :rtype: List[int]
    """
    dp = [0]* (n + 1)
    highest_pow_2 = 1
    for i in range(1, n + 1):
        if highest_pow_2 * 2 == i:
            highest_pow_2 *= 2
        dp[i] = 1 + dp[i - highest_pow_2]
    return dp

