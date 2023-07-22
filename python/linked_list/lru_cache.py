class Node:
    def __init__(self, key: int, val: int) -> object:
        self.key = key
        self.val = val
        self.prev = self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}  # map key to nodes

        # left=LRU and right=MRU
        self.left, self.right = Node(0, 0), Node(0, 0)
        self.left.next, self.right.prev = self.right, self.left

    # remove node from list
    def remove(self, node : Node):
        prevNode, nextNode = node.prev, node.next
        prevNode.next, nextNode.prev = nextNode, prevNode
    #append at right
    def insert(self, node : Node):
        prevNode, nextNode = self.right.prev, self.right
        prevNode.next = nextNode.prev = node
        node.next, node.prev = nextNode, prevNode
    def get(self, key: int) -> int:
        if key in self.cache:
            #update to most recently used
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].value
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        #check whether or not capacity is exceeded in cache
        if len(self.cache) > self.capacity:
            #remove from linked list and delete the LRU from hashmap
            lru = self.left.next
            #delete from linked list
            self.remove(lru)
            #delete from hashmap
            del self.cache[lru.key]
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)