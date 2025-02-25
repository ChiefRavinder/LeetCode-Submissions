class Node:
    def __init__(self,key,val):
        self.val=val
        self.key=key
        self.next=self.prev=None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity=capacity
        self.cache={}

        self.left,self.right=Node(0,0),Node(0,0)
        self.left.next, self.right.prev = self.right, self.left
        
    #remove from left
    def remove(self,node):
        prv,nxt= node.prev, node.next
        prv.next,nxt.prev=nxt,prv

    #add to right
    def add(self,node):
        prv,nxt=self.right.prev,self.right
        prv.next=node
        nxt.prev=node
        node.next,node.prev=nxt,prv
        
    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.add(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        
        self.cache[key]=Node(key,value)
        self.add(self.cache[key])

        if len(self.cache)>self.capacity:
            lru = self.left.next  # Store the least recently used node
            self.remove(lru)  # Remove it from the doubly linked list
            del self.cache[lru.key]  # Delete from the cache dictionary
            

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)