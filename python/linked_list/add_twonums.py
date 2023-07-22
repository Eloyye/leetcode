from typing import Optional

from python.linked_list.utils.ListNode import ListNode


def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    #creating a new node
    dummy = ListNode()
    cur = dummy

    carry = 0
    # carry because of edge case 8 + 7 = 15 ->
    while l1 or l2 or carry:
        v1, v2 = l1.val if l1 else 0, l2.val if l1 else 0

        #new digit
        val = v1 + v2 + carry
        carry = val // 10
        # this is because [0,9]
        val = val % 10
        cur.next = ListNode(val)

        #update ptr
        cur = cur.next
        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None
    return dummy.next