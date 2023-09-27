import unittest
from collections import defaultdict, Counter
from typing import List


class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        cardToFreq = Counter(hand)
        hand.sort()
        for card in hand:
            if cardToFreq[card] > 0:
                    for i in range(groupSize):
                        if cardToFreq[card + i] == 0:
                            return False
                        cardToFreq[card + i] -= 1
        return True

class StraightHandsTest(unittest.TestCase):
    def test1(self):
        sol = Solution()
        hand = [1,2,3,6,2,3,4,7,8]
        groupSize = 3
        result = sol.isNStraightHand(hand, groupSize)
        expected = True
        self.assertEqual(expected, result)
    def test2(self):
        sol = Solution()
        hand = [1,2,3,4,5]
        groupSize = 4
        result = sol.isNStraightHand(hand, groupSize)
        expected = False
        self.assertEqual(expected, result)
