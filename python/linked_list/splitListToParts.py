import unittest
from typing import Optional, List

from python.linked_list.utils.ListNode import ListNode


class Solution:
    def convert_list_to_ll(self, lst):
        if not lst:
            return None
        dummy = ListNode()
        head = dummy
        for val in lst:
            head.next = ListNode(val)
            head = head.next
        return dummy.next
    def convert_lists_to_list_of_ll(self, lsts) -> List[Optional[ListNode]]:
        res = []
        for lst in lsts:
            res.append(self.convert_list_to_ll(lst))
        return res
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        lst = []
        cur = head
        while cur:
            lst.append(cur.val)
            cur = cur.next
        if k > len(lst):
            new_lst = [[n] for n in lst]
            rest = [[] for _ in range(k - len(lst))]
            return self.convert_lists_to_list_of_ll(new_lst + rest)
        num_of_more_than_ones = len(lst) % k
        pieces_in_part = len(lst) // k
        i = 0
        res = []
        while i < len(lst):
            if num_of_more_than_ones > 0:
                res.append(lst[i : (i + pieces_in_part + 1)])
                i = i + pieces_in_part + 1
                num_of_more_than_ones -= 1
            else:
                res.append(lst[i : (i + pieces_in_part)])
                i = i + pieces_in_part
        return self.convert_lists_to_list_of_ll(res)
class SplitListToPartsTests(unittest.TestCase):
    def test1(self):
        splitListToParts = Solution().splitListToParts
        head = ListNode.initialize_list_node([1,2,3])
        k = 5
        res = splitListToParts(head, k)
        expected_in_lst = [[1],[2],[3],[],[]]
        expected = Solution().convert_lists_to_list_of_ll(expected_in_lst)
        self.assertEqual(expected, res)
    def test2(self):
        splitListToParts = Solution().splitListToParts
        head = ListNode.initialize_list_node([1,2,3,4,5,6,7,8,9,10])
        k = 3
        res = splitListToParts(head, k)
        expected = [[1,2,3,4],[5,6,7],[8,9,10]]
        self.assertEqual(expected, res)
    def test3(self):
        splitListToParts = Solution().splitListToParts
        head = ListNode.initialize_list_node([1,2,3,4,5,6,7,8,9,10, 11])
        k = 3
        res = splitListToParts(head, k)
        expected = [[1,2,3,4],[5,6,7, 8],[9,10, 11]]
        self.assertEqual(expected, res)
