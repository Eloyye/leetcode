from typing import Optional

from python.linked_list.utils.ListNode import ListNode


def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
    dummy = ListNode(next=head)
    left = dummy
    right = head

    # bias by n
    while n > 0 and right:
        right = right.next
        n -= 1

    #keep shifting both pointer
    while right:
        left = left.next
        right = right.next

    #delete node
    left.next = left.next.next

    return dummy.next