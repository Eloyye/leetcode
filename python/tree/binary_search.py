import unittest

from python.tree.isValidBST import isValidBST
from python.tree.utils.TreeNode import TreeNode


class InvalidBSTError(Exception):
    pass

class Solution:
    def binary_search(self, root : TreeNode, val : int) -> TreeNode:
        def binary_search_helper(root : TreeNode, val : int) -> TreeNode:
            if root.val == val:
                return root
            elif root.val < val:
                return binary_search_helper(root.right, val)
            else:
                return binary_search_helper(root.left, val)
        if not isValidBST(root):
            raise InvalidBSTError
        return binary_search_helper(root, val)

class BinarySearchTests(unittest.TestCase):
    def test1(self):
        binary_search = Solution().binary_search
        lst = [3, 2, 4, 1, None, None, 5]
        root = TreeNode.list_construct(lst)
        val = 5
        res = binary_search(root, val)
        self.assertIsNotNone(res)