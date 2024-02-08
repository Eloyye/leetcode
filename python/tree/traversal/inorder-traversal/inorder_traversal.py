from collections import deque
from typing import Optional

from python.tree.utils.TreeNode import TreeNode


class Solution:
    def inorder_traversal_stack(self, root: Optional[TreeNode]) -> list[int]:
        stack, result = [], []
        node = root
        while node or stack:
            # keep going left until you cannot
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            result.append(node.val)
            node = node.right
        return result
    def inorderTraversal(self, root: Optional[TreeNode]) -> list[int]:
        def dfs(node: TreeNode) -> list[int]:
            if not node:
                return []
            return dfs(node.left) + [node.val] + dfs(node.right)

        return dfs(root)
