from typing import Optional

from python.linked_list.utils.Node import Node


def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
    oldToCopy = {None : None}
    cur = head
    #allocate new copy s.t old node corresponds to new node
    while cur:
        copy = Node(cur.val)
        oldToCopy[cur] = copy
        cur = cur.next

    # set to beginning of list
    cur = head
    while cur:
        copy = oldToCopy[cur]
        copy.next = oldToCopy[cur.next]
        copy.random = oldToCopy[cur.random]
        cur = cur.next

    return oldToCopy[head]
