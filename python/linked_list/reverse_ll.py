from typing import Optional

from python.linked_list.utils.ListNode import ListNode


# Definition for singly-linked list.

def reverseList(head: Optional[ListNode]) -> Optional[ListNode]:
    prev_node = None
    current_node = head
    while current_node is not None:
        # temporary variable
        current_node.next, current_node, prev_node = prev_node, current_node.next, current_node
    return prev_node


def reverseList2(head: Optional[ListNode]) -> Optional[ListNode]:
    prev = None
    current = head
    while current is not None:
        nextNode = current.next
        current.next = prev
        prev, current = current, nextNode
    return prev

if __name__ == "__main__":
    lst = [1, 2, 3, 11, 4, 88]
    hd = ListNode.initialize_list_node(lst)
    new_hd = reverseList(hd)
    new_hd.print()

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