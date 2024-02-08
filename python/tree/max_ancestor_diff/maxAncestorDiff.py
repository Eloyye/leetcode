from typing import Optional

from python.tree.utils.TreeNode import TreeNode


class Solution:
    # Given the root of a binary tree,
    # find the maximum value v for which there exist different nodes a and b
    # where v = |a.val - b.val| and a is an ancestor of b.
    # A node a is an ancestor of b if either: any child of a is equal to b or any child of a is an ancestor of b.
    # optimal time complexity: O(n)
    def max_ancestor_diff(self, root: Optional[TreeNode]) -> int:
        def dfs(node : TreeNode, max_val : int, min_val : int) -> int:
            if not node:
                return max_val - min_val
            max_val = max(max_val, node.val)
            min_val = min(min_val, node.val)
            return max(dfs(node.left, max_val, min_val),
                       dfs(node.right, max_val, min_val))
        return dfs(root, root.val, root.val)

    def max_ancestor_diff_naive(self, root: Optional[TreeNode]) -> int:
        def dfs(node : TreeNode, ancestor_node : TreeNode) -> int:
            if not node:
                return 0
            return max(abs(node.val - ancestor_node.val),
                       dfs(node.left, node.left),
                       dfs(node.right, node.right),
                       dfs(node.left, node),
                       dfs(node.right, node),
                       dfs(node.right, ancestor_node),
                       dfs(node.left, ancestor_node)
                       )
        return dfs(root, root)
