from typing import Optional

from python.tree.utils.TreeNode import TreeNode


def isBalanced(root: Optional[TreeNode]) -> bool:

    # dfs is a modified maximum depth of tree, but returns -1 if unbalanced and >= 0 is max depth tree val
    def dfs(node: TreeNode) -> TreeNode:
        if not node:
            return 0
        l, r = dfs(node.left), dfs(node.right)
        if l == -1 or r == -1 or abs(r - l) > 1:
            return -1
        return 1 + max(l , r)

    return dfs(root) != -1