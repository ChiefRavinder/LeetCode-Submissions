class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}

        # Dummy head and tail
        self.left, self.right = Node(0, 0), Node(0, 0)
        self.left.next, self.right.prev = self.right, self.left

    # Remove node from the list
    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev

    # Insert node at the right (most recently used)
    def add(self, node):
        prev, nxt = self.right.prev, self.right
        prev.next = nxt.prev = node
        node.prev, node.next = prev, nxt

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])  # Move to most recently used
            self.add(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])  # Remove old node

        self.cache[key] = Node(key, value)
        self.add(self.cache[key])  # Add as most recently used

        if len(self.cache) > self.capacity:
            lru = self.left.next  # Store the least recently used node
            self.remove(lru)  # Remove it from the list
            del self.cache[lru.key]  # Remove from cache dictionary
