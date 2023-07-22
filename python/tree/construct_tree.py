from typing import Optional, List

from python.tree.utils.TreeNode import TreeNode


def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
    in_map = {val: i for i, val in enumerate(inorder)}
    def constr(pre_l, pre_r, in_l, in_r):
        # note that pre_r and in_r are indices of the subtree, non-inclusive
        # finished iterating through the subtree
        if pre_l >= pre_r or in_l >= in_r:
            return None
        root_val = preorder[pre_l]
        root_node = TreeNode(root_val)
        in_root_index = in_map[root_val]
        num_left = in_root_index - in_l
        root_node.left = constr(pre_l + 1, pre_l + 1 + num_left, in_l, in_root_index)
        root_node.right = constr(pre_l + 1 + num_left, pre_r, in_root_index + 1, in_r)
        return root_node

    return constr(0, len(preorder), 0, len(inorder))