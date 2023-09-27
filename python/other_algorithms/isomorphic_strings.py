import unittest


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
            n, m = len(s), len(t)
            if n != m:
                return False
            map1 = {}
            map2 = {}
            for i in range(n):
                s1, t1 = s[i], t[i]
                if (s1 in map1 and t1 != map1[s1]) or (t1 in map2 and s1 != map2[t1]):
                    return False
                map1[s1] = t1
                map2[t1] = s1
            return True

class IsomorphicTest(unittest.TestCase):
    def test1(self):
        sol = Solution()
        s, t = "egg", "add",
        res = sol.isIsomorphic(s, t)
        expect = True
        self.assertEqual(expect, res)
    def test2(self):
        sol = Solution()
        s, t = "egg", "adv",
        res = sol.isIsomorphic(s, t)
        expect = False
        self.assertEqual(expect, res)
    def test3(self):
        sol = Solution()
        s, t = "badc", "baba",
        res = sol.isIsomorphic(s, t)
        expect = False
        self.assertEqual(expect, res)

