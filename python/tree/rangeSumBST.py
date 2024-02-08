# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        def range_sum(node : Optional[TreeNode]) -> int:
            if not node:
                return 0
            val = node.val if low <= node.val <= high else 0
            return val + range_sum(node.left) + range_sum(node.right)
        return range_sum(root)
