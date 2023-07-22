from typing import List
import unittest

#simple palindrome algorithm
def isPalindrome(word):
    l, r = 0, len(word) - 1
    while r > l:
        if word[r] != word[l]:
            return False
        l, r = l + 1, r - 1
    return True

# Given a string s, partition s such that every
# substring of the partition is a palindrome.
# Return all possible palindrome partitioning of s.
def partition(s: str) -> List[List[str]]:
    res = []
    # Includes all valid palindromes for substrings that start with s[i] and contains current subset
    def dfs(i: int, subset: List[str]):
        if i == len(s):
            res.append(subset.copy())
            return
        # to create partition, we separate into two strings s[i: j + 1] and s[j + 1: ...]
        for j in range(i, len(s)):
            word = s[i : j + 1]
            if isPalindrome(word):
                subset.append(word)
                #check for s[j + 1: ...]
                dfs(j + 1, subset)
                subset.pop()
    dfs(0, [])
    return res

class PartitionTest(unittest.TestCase):

    def test_1(self):
        self.assertEqual(partition("aab"), [["a","a","b"],["aa","b"]])

    def test_2(self):
        self.assertEqual(partition("a"), [["a"]])

    def test_3(self):
        self.assertEqual(partition("ab"), [["a","b"]])

    def test_4(self):
        self.assertEqual(partition("abc"), [["a","b","c"]])

    def test_5(self):
        self.assertEqual(partition("abba"), [["a","b","b","a"],["a","bb","a"],["abba"]])

