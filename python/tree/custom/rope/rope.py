from collections import deque
from typing import Self


# from re import split as regex_split
class RopeNode:
    def __init__(self, weight: int=0, string: str="", left=None, right=None):
        self.weight, self.string, self.left, self.right = weight, string, left, right

    @staticmethod
    def calculate_leaves(rope_node):
        if not rope_node:
            return 0
        if not rope_node.left and not rope_node.right:
            return rope_node.weight
        return RopeNode.calculate_leaves(rope_node.left) + RopeNode.calculate_leaves(rope_node.right)

    # print in like a yaml format
    def print_tree(self):
        def print_tree_helper(node, level):
            if not node:
                return
            print("  " * level + f"{node.string} ({node.weight})")
            print_tree_helper(node.left, level + 1)
            print_tree_helper(node.right, level + 1)

        print_tree_helper(self, 0)

    # 1-indexed
    def get(self, i: int) -> str:
        if i <= 0:
            raise Exception(f"invalid index: {i}. Retrieval is 1-indexed")

        def get_helper(node, i: int) -> str:
            if node.weight < i and node.right:
                return get_helper(node.right, i - node.weight)
            if node.left:
                return get_helper(node.left, i)
            if i - 1 < len(node.string):
                return node.string[i - 1]
            raise Exception(f"Index retrieved is out of bounds")

        return get_helper(self, i)

    @staticmethod
    def construct_rope(string: str):
        q = deque([RopeNode(weight=len(val), string=val, left=None, right=None) for val in string.split(' ')])
        while q and len(q) > 1:
            left_over = len(q) % 2 == 1
            queue_range = range(len(q))[::2]
            for i in queue_range:
                v1 = q.popleft()
                v2 = q.popleft() if not left_over or i < len(queue_range) else None
                sum_weights = RopeNode.calculate_leaves(v1)
                node = RopeNode(weight=sum_weights, left=v1, right=v2, string="t")
                q.append(node)
        if len(q) != 1:
            raise Exception(
                f"Error: unable to construct rope. Expected single rope Node as output but got {len(q)} nodes")
        return q[0]

    def insert(self, index: int, string: str) -> Self:
        RopeNode.construct_rope()

    def delete(self):
        pass

    @staticmethod
    def concatenate(str1: str, str2: str) -> Self:
        node1 = RopeNode.construct_rope(str1)
        node2 = RopeNode.construct_rope(str2)
        return RopeNode(weight=RopeNode.calculate_leaves(node1), string="", left=node1, right=node2)


if __name__ == '__main__':
    rope = RopeNode(string="hello world and feliz navidad")
    print(rope.get(1))
