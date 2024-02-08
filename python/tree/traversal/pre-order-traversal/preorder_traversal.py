from typing import Optional

from python.tree.utils.TreeNode import TreeNode


class Solution:
    def pre_order_traversal_iterative(self, root: TreeNode) -> list[int]:
        stack, res = [], []
        node = root
        while node or stack:
            while node:
                res.append(node.val)
                stack.append(node)
                node = node.left
            node = stack.pop()
            node = node.right
        return res
    def preorderTraversal(self, root: Optional[TreeNode]) -> list[int]:
        def dfs(node : TreeNode) -> list[int]:
            if not node:
                return []
            return [node.val] + dfs(node.left) + dfs(node.right)
        return dfs(root)
