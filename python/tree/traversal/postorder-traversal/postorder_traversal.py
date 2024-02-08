from collections import deque
from typing import Optional

from python.tree.utils.TreeNode import TreeNode


class Solution:
    def postorder_traversal_iterative(self, root: Optional[TreeNode]) -> list[int]:
        stack, res = [], deque()
        node = root
        while node or stack:
            while node:
                res.appendleft(node.val)
                stack.append(node)
                node = node.right
            node = stack.pop()
            node = node.left
        return res

    def postorderTraversal(self, root: Optional[TreeNode]) -> list[int]:
        def dfs(node : TreeNode) -> list[int]:
            if not node:
                return []
            return dfs(node.left) + dfs(node.right) + [node.val]
        return dfs(root)

