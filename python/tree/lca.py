from python.tree.utils.TreeNode import TreeNode


def lowestCommonAncestor(root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
    # create an interval [a, b]
    # check whether current node is
    interval = [min(p.val, q.val), max(p.val, q.val)]
    if interval[0] <= root.val <= interval[1]:
        return root
    elif interval[1] < root.val:
        return lowestCommonAncestor(root.left, p, q)
    else:
        return lowestCommonAncestor (root.right, p, q)