from typing import List, Optional

from python.linked_list.utils.ListNode import ListNode


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def mergeList(list1, list2):
            head = ListNode()
            cur = head
            while list1 and list2:
                if list1.val < list2.val:
                    cur.next = list1
                    list1 = list1.next
                else:
                    cur.next = list2
                    list2 = list2.next
                cur = cur.next
            cur.next = list1 if list1 else list2
            return head.next
        if not lists:
            return None
        while len(lists) > 1:
            res_list = []
            for i in range(0, len(lists) - 1, 2):
                val1, val2 = lists[i], lists[i + 1]
                merge_list = mergeList(val1, val2)
                res_list.append(merge_list)
            if len(lists) % 2:
                res_list.append(lists[-1])
            lists = res_list
        return lists[0] if lists[0] else None