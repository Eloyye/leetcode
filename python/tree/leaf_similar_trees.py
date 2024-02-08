from typing import Optional

from python.tree.utils.TreeNode import TreeNode


class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def get_leaf_nodes(node: Optional[TreeNode]) -> list[int]:
            if not node:
                return []
            if node.left == node.right == None:
                return [node.val]
            return get_leaf_nodes(node.left) + get_leaf_nodes(node.right)
        res1, res2 = get_leaf_nodes(root1), get_leaf_nodes(root2)
        return res1 == res2

def test1():
    root1, root2 = [3,5,1,6,2,9,8,None,None,7,4], [3,5,1,6,7,4,2,None,None,None,None,None,None,9,8]
    root1, root2 = TreeNode.list_construct(root1), TreeNode.list_construct(root2)
    leaf_similar = Solution().leafSimilar
    assert leaf_similar(root1, root2)
def test2():
    root1, root2 = [1,2,3], [1,3,2]
    root1, root2 = TreeNode.list_construct(root1), TreeNode.list_construct(root2)
    leaf_similar = Solution().leafSimilar
    assert not leaf_similar(root1, root2)
