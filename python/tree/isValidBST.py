from typing import Optional

from python.tree.utils.TreeNode import TreeNode


def isValidBST(self, root: Optional[TreeNode]) -> bool:
    def isValidBSTGivenLeft(node, left, right) -> bool:
        if not node:
            return True
        if not (left < node.val < right):
            return False
        return isValidBSTGivenLeft(node.left, left, node.val) and isValidBSTGivenLeft(node.right, node.val, right)
    return isValidBSTGivenLeft(root, float('-inf'), float('inf'))


