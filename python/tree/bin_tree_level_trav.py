from collections import deque
from typing import Optional, List

from python.tree.utils.TreeNode import TreeNode


def levelOrder(root: Optional[TreeNode]) -> List[List[int]]:
    res = []
    q = deque()
    if root:
        q.append(root)
    while q:
        level_nodes = []
        for _ in range(len(q)):
            node : TreeNode = q.popleft()
            level_nodes.append(node.val)
            # iterate through all the neighbors
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        res.append(level_nodes)
    return res
