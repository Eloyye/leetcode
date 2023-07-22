import unittest

def countSubstrings(s: str) -> int:
    num_substrings = 0
    def countPalindromes(l: int, r: int) -> int:
        count_palindromes = 0
        while l >= 0 and r < len(s) and s[l] == s[r]:
            count_palindromes += 1
            l -= 1
            r += 1
        return count_palindromes
    for i in range(len(s)):
        num_substrings += countPalindromes(i, i)
        num_substrings += countPalindromes(i, i + 1)
    return num_substrings

def incorrectCountSubstrings(s:str) -> int:
    num_substrings = 0
    def countPalindromes(l: int, r: int) -> int:
        count_palindromes = 0
        while l >= 0 and r < len(s) and s[l] == s[r]:
            count_palindromes += 1
            l -= 1
            r += 1
        return count_palindromes
    for i in range(len(s)):
        num_substrings += countPalindromes(i, i)
    return num_substrings


class countSubstringsTest(unittest.TestCase):
    def test1(self):
        string = "abc"
        self.assertEqual(countSubstrings(string), incorrectCountSubstrings(string))
    def test2(self):
        string = "aaa"
        self.assertEqual(countSubstrings(string), incorrectCountSubstrings(string))
    def test3(self):
        string = "babad"
        self.assertEqual(countSubstrings(string), incorrectCountSubstrings(string))
    def test4(self):
        string = "cbbd"
        self.assertEqual(countSubstrings(string), incorrectCountSubstrings(string))
