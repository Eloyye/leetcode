from python.tree.utils.TreeNode import TreeNode


def concatenate_tree(root : TreeNode) -> str:
    def is_leaf(node : TreeNode) -> bool:
        return not node.left and not node.right
    if not root:
        return ""
    res = root.val if is_leaf(root) and root.val else ""
    return concatenate_tree(root.left) + res + concatenate_tree(root.right)

if __name__ == '__main__':
    # hello_world = TreeNode.list_construct([None, "hello ", "world"])
    # print(concatenate_tree(hello_world))
    # res = concatenate_tree(TreeNode.list_construct(["place_holder", "place_holder", "place_holder", "feliz ", "navidad ", "y ", "nada"]))
    pass