# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def initialize_list_node(lst):
    if not lst:
        return None

    head = ListNode(lst[0])
    current = head

    for i in range(1, len(lst)):
        current.next = ListNode(lst[i])
        current = current.next

    return head