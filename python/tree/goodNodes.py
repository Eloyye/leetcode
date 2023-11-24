from python.tree.utils.TreeNode import TreeNode


class Solution:
    def goodNodes2(root: TreeNode) -> int:
        def dfs(node, maxVal) -> int:
            if not node:
                return 0
            res = 0
            if node and node.val >= maxVal:
                res += 1
                maxVal = node.val
            res += dfs(node.left, maxVal) + dfs(node.right, maxVal)
            return res
        res = dfs(root, float('-inf'))
        return res
    def goodNodes(root: TreeNode) -> int:
        res = 0
        def dfs(node : TreeNode, maxVal : int) -> None:
            nonlocal res
            if not node:
                return
            if node and node.val >= maxVal:
                res += 1
                maxVal = node.val
            dfs(node.left, maxVal)
            dfs(node.right, maxVal)

        dfs(root, float('-infinity'))
        return res