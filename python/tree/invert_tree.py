from typing import Optional

from python.tree.utils.TreeNode import TreeNode


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root
        tmp = root.right
        root.right = self.invertTree(root.left) if root.left else None
        root.left = self.invertTree(tmp) if tmp else None
        return root