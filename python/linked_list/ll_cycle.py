from typing import Optional

from python.linked_list.utils.ListNode import ListNode, initialize_list_node


#O(n) time complexity and O(n) space complexity
def hasCycle(head: Optional[ListNode]) -> bool:
    save = set()
    node = head
    while node:
        if node in save:
            return True
        save.add(node)
        node = node.next
    return False

def hasCycle(head: Optional[ListNode]) -> bool:
    slow = fast = head
    while fast and fast.next:
        if fast == slow:
            return True
        fast = fast.next.next
        slow = slow.next
    return False

n = initialize_list_node([1])
hasCycle(n)

