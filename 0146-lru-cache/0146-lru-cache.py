class Node:
    def __init__(self, key, value):
        self.key, self.value = key, value
        self.prev = self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dict = {}
        
        self.left, self.right = Node(0,0), Node(0,0)
        self.left.next, self.right.prev = self.right, self.left

    def insert(self, node):
        prev, nxt = self.right.prev, self.right
        prev.next = nxt.prev = node
        node.prev, node.next = prev, nxt
         

    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev

        

    def get(self, key: int) -> int:
        if key in self.dict:
            self.remove(self.dict[key])
            self.insert(self.dict[key])
            return self.dict[key].value
        return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.dict:
            self.remove(self.dict[key])

        self.dict[key] = Node(key, value)
        self.insert(self.dict[key])
        

        if len(self.dict) > self.capacity:
            old_key = self.left.next
            self.remove(old_key)
            del self.dict[old_key.key]
        
        
        

        
            

        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)