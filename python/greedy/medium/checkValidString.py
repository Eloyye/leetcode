import unittest


class Solution:
    def checkValidString(self, s: str) -> bool:
        minOpen = maxOpen = 0
        for c in s:
            if c == '(':
                #required
                minOpen += 1
                maxOpen += 1
            elif c == ')':
                #requirement for minOpen
                if minOpen > 0:
                    minOpen -= 1
                maxOpen -= 1
                if maxOpen < 0:
                    # there are more closed parentheses than there are open parentheses
                    return False
            elif c == '*':
                if minOpen > 0:
                    #consider the case where * is a ')', which closes a corresponding open parenthesis previously visited
                    minOpen -= 1
                #consider the case where * is a '(', but it is not a hard requirement
                maxOpen += 1
        # consider the case where there are more open parentheses than there are closing parentheses.
        return minOpen == 0
class CheckValidStringTest(unittest.TestCase):
    def test1(self):
        sol = Solution()
        s = "()"
        res = sol.checkValidString(s)
        expected = True
        self.assertEqual(expected, res)
    def test2(self):
        sol = Solution()
        s = "(*)"
        res = sol.checkValidString(s)
        expected = True
        self.assertEqual(expected, res)
    def test3(self):
        sol = Solution()
        s = "(*))"
        res = sol.checkValidString(s)
        expected = True
        self.assertEqual(expected, res)

    def test4(self):
        sol = Solution()
        s = "()*)"
        res = sol.checkValidString(s)
        expected = True
        self.assertEqual(expected, res)
    def test5(self):
        sol = Solution()
        s = "("
        res = sol.checkValidString(s)
        expected = False
        self.assertEqual(expected, res)