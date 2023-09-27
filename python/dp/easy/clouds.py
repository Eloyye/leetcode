import unittest


def jumpingOnClouds(c):
    # Write your code here
    n = len(c)
    dp = [0]* (n)
    cur_val = c[0]
    dp[n - 1] = 0
    dp[n - 2] = 1 if c[n - 2] == c[n - 1] else float('inf')
    for i in range(n - 3, -1, - 1):
        if c[i] == cur_val:
            f, s = dp[i + 1], dp[i + 2]
            dp[i] = 1 + min(f, s)
        else:
            dp[i] = float('inf')
    return dp[0]

class CloudsTest(unittest.TestCase):
    def test1(self):
        c = [0, 0, 1, 0, 0, 1, 0]
        res = jumpingOnClouds(c)
        expected = 4
        self.assertEqual(expected, res)
    def test2(self):
        c = [0, 0 ,0 ,0 ,1,0]
        res = jumpingOnClouds(c)
        expected = 3
        self.assertEqual(expected, res)
    def test3(self):
        c = [0, 1, 0, 1, 0, 1, 0, 1, 0, 0]
        res = jumpingOnClouds(c)
        expected = 5
        self.assertEqual(expected, res)