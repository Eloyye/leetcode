
import unittest

def numDecodings3(s: str) -> int:
    string_length = len(s)
    first = second = third = 1
    for i in range(string_length - 1, -1, -1):
        isInvalidZero = s[i] == "0"
        second = third if not isInvalidZero else 0
        canBeTwoDigits = (i + 1) < string_length
        isTen = s[i] == "1"
        isValidTwenty = (s[i] == "2") and (s[i + 1] in "0123456") if canBeTwoDigits else False
        if canBeTwoDigits and (isTen or isValidTwenty):
            second += first
    return second

def numDecodings2(s: str) -> int:
    string_length = len(s)
    dp = [1] * (string_length + 1)
    for i in range(string_length - 1, -1, -1):
        isInvalidZero = s[i] == "0"
        # we can
        dp[i] = dp[i + 1] if not isInvalidZero else 0
        canBeTwoDigit = (i + 1) < string_length
        isTen = s[i] == "1"
        isValidTwenty = (s[i] == "2") and (s[i + 1] in "0123456") if canBeTwoDigit else False
        if canBeTwoDigit and (isTen or isValidTwenty):
            dp[i] += dp[i + 2]
    return dp[0]

def numDecodings(s: str) -> int:
    dp = {len(s): 1}

    def numOfEncodingsAt(i : int) -> int:
        isCached = i in dp
        if isCached:
            return dp[i]
        isInvalidZero = s[i] == "0"
        if isInvalidZero:
            return 0
        res = numOfEncodingsAt(i + 1)
        canBeTwoDigit = (i + 1) < len(s)
        isTens = s[i] == "1"
        isValidTwenty = (s[i] == "2") and (s[i + 1] in "0123456") if canBeTwoDigit else False
        if canBeTwoDigit and (isTens or isValidTwenty):
            res += numOfEncodingsAt(i + 2)
        dp[i] = res
        return res

    return numOfEncodingsAt(0)

class numDecodingsTest(unittest.TestCase):
    def test1(self):
        s = "12"
        self.assertEqual(numDecodings3(s), 2)
    def test2(self):
        s = "226"
        self.assertEqual(numDecodings3(s), 3)
    def test3(self):
        s = "06"
        self.assertEqual(numDecodings3(s), 0)

