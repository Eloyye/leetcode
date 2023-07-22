from typing import Optional

from python.tree.utils.TreeNode import TreeNode


class Solution:
    #use dfs
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_diameter = 0
        def dfs(node : TreeNode) -> TreeNode:
            nonlocal max_diameter
            if not node:
                return 0
            # maximum non-splitting path for left and right subtree
            l, r = dfs(node.left), dfs(node.right)
            #update max diameter if we do actually split in node
            max_diameter = max(max_diameter, l + r + 2)
            # return the longest non-splitting path, but can only be one direction and one edge
            return 1 + max(l, r)
        dfs(root)
        return max_diameter
