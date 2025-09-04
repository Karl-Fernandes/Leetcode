class Node:
    def __init__(self, key=0, value=0):
        self.key, self.value = key, value
        self.prev = self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity 
        self.dict = {}
        
        self.head, self.tail = Node(), Node()
        self.head.next, self.tail.prev = self.tail, self.head

    def _remove(self, node: Node):
        prv, nxt = node.prev, node.next
        prv.next, nxt.prev = nxt, prv 

    def _insert(self, node: Node):
        prv, nxt = self.head, self.head.next
        prv.next = nxt.prev = node
        node.prev, node.next = prv, nxt
    
    def get(self, key: int) -> int:
        if key in self.dict:
            self._remove(self.dict[key])
            self._insert(self.dict[key])
            return self.dict[key].value
        
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.dict:
            self._remove(self.dict[key])
        
        self.dict[key] = Node(key, value)
        self._insert(self.dict[key])

        if len(self.dict) > self.capacity:
            oldest = self.tail.prev
            self._remove(oldest)
            del self.dict[oldest.key]



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)