from typing import Optional

from python.tree.utils.TreeNode import TreeNode


def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
    def dfs(node):
        if not node:
            return False
        elif node.value == subRoot.val:
            def sameTree(root1, root2):
                if not root1 and not root2:
                    return True
                elif (root1 and root2) and root1.value == root2.value:
                    return sameTree(root1.left, root2.left) and sameTree(root1.right, root2.right)
                else:
                    return False
            if sameTree(node, subRoot):
                return sameTree(node, subRoot)
        return dfs(node.left) or dfs(node.right)
    return dfs(root)