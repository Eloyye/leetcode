# Definition for a binary tree node.
from collections import deque


class TreeNode:
    def __init__(self, val: int = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

    @staticmethod
    def list_construct(lst : list[int]):
        if not lst:
            return None
        head = TreeNode(lst[0])
        q = deque([head])
        i = 1
        while q and i < len(lst):
            current_node = q.popleft()
            if i < len(lst) and lst[i]:
                current_node.left = TreeNode(lst[i])
                q.append(current_node.left)
            i += 1
            if i < len(lst) and lst[i]:
                current_node.right = TreeNode(lst[i])
                q.append(current_node.right)
            i += 1
        return head

