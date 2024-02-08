from python.tree.max_ancestor_diff.maxAncestorDiff import *


def max_ancestor_diff_test():
    in_ = [8, 3, 10, 1, 6, None, 14, None, None, 4, 7, 13]
    res = Solution().max_ancestor_diff_naive(TreeNode.list_construct(in_))
    expect = 7
    assert expect == res
