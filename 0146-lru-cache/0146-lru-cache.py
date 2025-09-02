class Node:
    def __init__(self, value=0, key=0):
        self.key, self.value = key, value
        self.prev = self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity 
        self.dict = {}

        self.head = Node()
        self.tail = Node()

        self.head.next, self.tail.prev = self.tail, self.head
        
    def _remove(self, node: Node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev
    
    def _insert(self, node: Node):
        prev, nxt = self.head, self.head.next
        prev.next = nxt.prev = node
        node.next, node.prev = nxt, prev

    def get(self, key: int) -> int:
        if key in self.dict:
            self._remove(self.dict[key])
            self._insert(self.dict[key])
            return self.dict[key].value
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.dict:
            self._remove(self.dict[key])
        
        self.dict[key] = Node(value, key)
        self._insert(self.dict[key])

        if len(self.dict) > self.capacity:
            old_key = self.tail.prev
            self._remove(old_key)
            del self.dict[old_key.key]

        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)