from python.tree.utils.TreeNode import TreeNode


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