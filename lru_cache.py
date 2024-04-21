class ListNode():
        def __init__(self, key, val):
            self.key = key
            self.val = val 
            self.prev = None
            self.next = None
            
class LRUCache:

    # LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hashmap = dict()
        self.head = ListNode(-1,  -1)
        self.tail = ListNode(-1,  -1)
        self.head.next = self.tail
        self.tail.prev = self.head
        
    # int get(int key) Return the value of the key if the key exists, otherwise return -1.
    def get(self, key: int) -> int:
        # Intuition: use hashmap k:v pairs
        if key not in self.hashmap:
            return -1
        
        node = self.hashmap[key]
        self.remove(node)
        self.add(node)
        
        return node.val
    
    """
    void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-     value pair to the cache. If the number of keys exceeds the capacity from this operation, evict the     least recently used key.
    """
    def put(self, key: int, value: int) -> None:
        # Generic hashmap takes care of the update functionality - just reassign the value
        if key in self.hashmap:
            self.remove(self.hashmap[key])
        
        node = ListNode(key, value)
        self.hashmap[key] = node
        # insert node at front of list
        self.add(node)
            
        # For eviction, keep a pointer for most recent and least recent items
        if len(self.hashmap) > self.capacity:
            target = self.tail.prev
            self.remove(target)
            del self.hashmap[target.key]
            
    def add(self, node):
        temp = self.head.next
        node.prev = self.head
        node.next = temp
        self.head.next = node
        temp.prev = node
    
    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)