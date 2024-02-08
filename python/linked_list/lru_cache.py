class Node:
    def __init__(self, key: int, val: int):
        self.key = key
        self.val = val
        self.prev = self.next = None


class LRUList:
    def __init__(self):
        self.lru_sentinel, self.mru_sentinel = Node(0, 0), Node(0, 0),
        self.lru_sentinel.next, self.mru_sentinel.next = self.mru_sentinel, self.lru_sentinel

    def remove(self, node: Node):
        prev_node, next_node = node.prev, node.next
        prev_node.next, next_node.prev = next_node, prev_node

    def insert(self, node: Node):
        prev_node, next_node = self.mru_sentinel.prev, self.mru_sentinel
        prev_node.next = next_node.prev = node
        node.next, node.prev = next_node, prev_node

    def evict(self):
        lru = self.lru_sentinel.next
        self.remove(lru)
        return lru


class LRUCache2:
    def __init__(self, capacity: int):
        self.capacity = capacity
        # key to node rather than key to val
        self.key_node_cache: dict[int, Node] = {}
        self.lru_list = LRUList()

    def get(self, key: int) -> int:
        if key in self.key_node_cache:
            self.lru_list.remove(self.key_node_cache[key])
            self.lru_list.insert(self.key_node_cache[key])
            return self.key_node_cache[key].val
        return -1

    def put(self, key: int, value: int):
        if key in self.key_node_cache:
            self.lru_list.remove(self.key_node_cache[key])
        self.key_node_cache[key] = Node(key, value)
        self.lru_list.insert(self.key_node_cache[key])
        if len(self.key_node_cache) > self.capacity:
            lru_node = self.lru_list.evict()
            del self.key_node_cache[lru_node.key]


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}  # map key to nodes

        # left=LRU and right=MRU
        self.left, self.right = Node(0, 0), Node(0, 0)
        self.left.next, self.right.prev = self.right, self.left

    # remove node from list
    def remove(self, node: Node):
        prevNode, nextNode = node.prev, node.next
        prevNode.next, nextNode.prev = nextNode, prevNode

    # append at right
    def insert(self, node: Node):
        prevNode, nextNode = self.right.prev, self.right
        prevNode.next = nextNode.prev = node
        node.next, node.prev = nextNode, prevNode

    def get(self, key: int) -> int:
        if key in self.cache:
            # update to most recently used
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

        # check whether or not capacity is exceeded in cache
        if len(self.cache) > self.capacity:
            # remove from linked list and delete the LRU from hashmap
            lru = self.left.next
            # delete from linked list
            self.remove(lru)
            # delete from hashmap
            del self.cache[lru.key]
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
