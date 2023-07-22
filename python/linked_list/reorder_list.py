from typing import Optional

from python.linked_list.utils.ListNode import ListNode


def reorderList(self, head: Optional[ListNode]) -> None:
    """
    Do not return anything, modify head in-place instead.
    """
    # Find middle pointer by using fast and slow pointer
    # we want there to be two lists: left list, and right list
    slow, fast = head, head.next
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    # we designate slow to be the end of the left list
    # slow.next is the first value of the right list
    # last element of the reordered list
    second = slow.next
    prev = slow.next = None

    #reverse list
    while second:
        tmp = second.next
        second.next = prev
        prev = second
        second = tmp

    # head of the right reverse linked list is prev

    #merge two halfs
    first, second = head, prev

    while second:
        tmp1, tmp2 = first.next, second.next
        first.next = second
        second.next = tmp1
        first = tmp1
        second = tmp2
