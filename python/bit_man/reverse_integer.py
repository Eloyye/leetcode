class Solution:
    def reverse(self, x: int) -> int:
        res = 0
        is_neg = False
        MIN, MAX = -(2**31), (2**31) - 1
        for i, digit in enumerate(str(x)):
            if digit == '-':
                is_neg = True
            else:
                res += int(digit) * (10 ** (i if not is_neg else i - 1))
        res = res if not is_neg else -res
        return res if MIN <= res <= MAX else 0


def test1():
    x = 123
    reverse = Solution().reverse
    assert reverse(x) == 321


def test2():
    x = -123
    reverse = Solution().reverse
    assert reverse(x) == -321


def test3():
    x = 120
    reverse = Solution().reverse
    assert reverse(x) == 21
