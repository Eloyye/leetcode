from typing import Optional

from python.linked_list.utils.ListNode import ListNode

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        # save one node before
        groupPrev = dummy

        while True:
            kth = self.getKth(groupPrev, k)
            if not kth:
                break
            # one node after the group
            groupNext = kth.next

            #reverse group
            prev, curr = kth.next, groupPrev.next

            while curr != groupNext:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp
            #first node in group
            tmp = groupPrev.next
            groupPrev.next = kth
            groupPrev = tmp
        return dummy.next

    def getKth(self, curr : ListNode, k : int) -> ListNode:
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr