from typing import Optional

from python.linked_list.utils.ListNode import ListNode


# Definition for singly-linked list.

def reverseList(head: Optional[ListNode]) -> Optional[ListNode]:
    prev = None
    current = head
    while head is not None:
        nextNode = current.next
        current.next = prev
        prev, current = current, nextNode
    return prev

def reverseListRecurse(head: Optional[ListNode]) -> Optional[ListNode]:
    #base case
    if head is None or head.next is None:
        return head
    #recursive case
    # p points to the head of the linked list which is located on far end of head
    p = reverseListRecurse(head.next)
    #have the tail point of reversed list point to head
    head.next.next = head
    #the tail of the linked list so far
    head.next = None
    return p