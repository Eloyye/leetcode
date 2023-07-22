from python.graphs.utils.Node import Node
import unittest

def cloneGraph(node : Node) -> Node:
    originalToCopy = {None : None}
    visited = set()
    def constructNodeCopiesAt(node : Node) -> None:
        if not node or node in visited:
            return
        visited.add(node)
        #construct a copy of the node
        nodeCopy = Node(node.val)
        #add to hashmap
        originalToCopy[node] = nodeCopy
        #iterate through all the neighbors
        for neighbor in node.neighbors:
            constructNodeCopiesAt(neighbor)

    constructNodeCopiesAt(node)
    visited = set()
    def constructGraphCopyAt(node : Node) -> None:
        if not node or node in visited:
            return
        copy : Node = originalToCopy[node]
        visited.add(node)
        for neighbor in node.neighbors:
            copy.neighbors.append(originalToCopy[neighbor])
            constructGraphCopyAt(neighbor)

    constructGraphCopyAt(node)
    return originalToCopy[node]

def cloneGraph2(node : Node) -> Node:
    originalNodesToCopyNodes = {}
    def convertOriginalNodeToCopy(originalNode : Node):
        if originalNode in originalNodesToCopyNodes:
            return originalNodesToCopyNodes[originalNode]
        copyNode = Node(originalNode.val)
        originalNodesToCopyNodes[originalNode] = copyNode
        for neighborNode in originalNode.neighbors:
            copyNode.neighbors.append(convertOriginalNodeToCopy(neighborNode))
        return copyNode
    return convertOriginalNodeToCopy(node) if node else None


class CloneGraphTest(unittest.TestCase):
    def firstExample(self):
        node1 = Node(1)
        node2 = Node(2)
        node3 = Node(3)
        node4 = Node(4)
        node1.neighbors.extend([node2, node4])
        node2.neighbors.extend([node1, node3])
        node3.neighbors.extend([node2, node4])
        node4.neighbors.extend([node1, node3])
        assert cloneGraph(node1)