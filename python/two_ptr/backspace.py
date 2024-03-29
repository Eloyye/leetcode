import unittest

class Solution2:
    def backspace_compare(self, s1 : str, s2: str) -> bool:
        def evaluate(s : str) -> str:
            def resolve_backspace(s, i, backspaces):
                while i >= 0 and s[i] == '#':
                    backspaces += 1
                    i -= 1
                return i, backspaces
            i = len(s) - 1
            res = ""
            backspaces = 0
            while i >= 0:
                while i >= 0 and s[i] == '#':
                    backspaces += 1
                    i -= 1
                while backspaces > 0:
                    if i >= 0 and s[i] == "#":
                        backspaces += 1
                    else:
                        backspaces -= 1
                    i -= 1
                if i >= 0 and s[i] != '#' and backspaces == 0:
                    res = s[i] + res
                    i -= 1
            return res

        e1 = evaluate(s1)
        e2 = evaluate(s2)
        print(f'e1: {e1}, e2: {e2}')
        return e1 == e2

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        i, j = len(s) - 1, len(t) - 1
        while i >= 0 or j >= 0:
            i = self.resolve_backspace(i, s)
            j = self.resolve_backspace(j, t)
            if (i < 0 <= j) or (j < 0 <= i) :
                return False
            if i < 0 and j < 0:
                return True
            if s[i] == t[j]:
                i -= 1
                j -= 1
            else:
                return False
        return True

    def resolve_backspace(self, i, s):
        num_delete = 0
        while s[i] == '#' or num_delete > 0:
            if i >= 0 and s[i] == '#':
                num_delete += 1
            else:
                num_delete -= 1
            i -= 1
        return i


class BcTest(unittest.TestCase):
    def test1(self):
        f = Solution2().backspace_compare
        s, t = "ab#c", "ad#c"
        res = f(s, t)
        expected = True
        self.assertEqual(expected, res)
    def test2(self):
        f = Solution2().backspace_compare
        s, t = "ab##", "c#d#"
        res = f(s, t)
        expected = True
        self.assertEqual(expected, res)
    def test3(self):
        f = Solution2().backspace_compare
        s, t = "a#c", "b"
        res = f(s, t)
        expected = False
        self.assertEqual(expected, res)
    def test4(self):
        f = Solution2().backspace_compare
        s, t = "bxj##tw", "bxo#j##tw"
        res = f(s, t)
        expected = True
        self.assertEqual(expected, res)
    def test5(self):
        f = Solution2().backspace_compare
        s, t = "xywrrmp", "xywrrmu#p"
        res = f(s, t)
        expected = True
        self.assertEqual(expected, res)
    def test6(self):
        f = Solution2().backspace_compare
        s, t = "a##c", "#a#c"
        res = f(s, t)
        expected = True
        self.assertEqual(expected, res)
    def test7(self):
        f = Solution2().backspace_compare
        s, t = "bbbextm", "bbb#extm"
        res = f(s, t)
        expected = False
        self.assertEqual(expected, res)
    def test8(self):
        f = Solution2().backspace_compare
        s, t = "nzp#o#g", "b#nzp#o#g"
        res = f(s, t)
        expected = True
        self.assertEqual(expected, res)
    def test9(self):
        f = Solution2().backspace_compare
        s, t = "aaa###a", "aaaa###a"
        res = f(s, t)
        expected = False
        self.assertEqual(expected, res)
    def test10(self):
        f = Solution2().backspace_compare
        s, t = "e##e#o##oyof##q", "e##e#fq##o##oyof##q"
        res = f(s, t)
        expected = True
        self.assertEqual(expected, res)

def backspaceCompare(s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """
    n, m = len(s), len(t)
    s_ptr, t_ptr = n - 1, m - 1
    s_b, t_b = 0, 0
    while s_ptr >= 0 or t_ptr >= 0:
        while s_ptr >= 0:
            if s[s_ptr] == '#':
                s_b += 1
                s_ptr -= 1
            elif s_b > 0:
                s_b -= 1
                s_ptr -= 1
            else:
                break
        while t_ptr >= 0:
            if t[t_ptr] == '#':
                t_b += 1
                t_ptr -= 1
            elif t_b > 0:
                t_b -= 1
                t_ptr -= 1
            else:
                break
        if s_ptr >= 0 and t_ptr >= 0 and s[s_ptr] != t[t_ptr]:
            return False
        if (s_ptr >= 0) != (t_ptr >= 0):
            return False
        s_ptr -= 1
        t_ptr -= 1
    return True

backspaceCompare("ab#c", "ad#c")