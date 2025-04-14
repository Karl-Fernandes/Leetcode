class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dict = {}
        self.access_log = {}
        self.counter = 0

        

    def get(self, key: int) -> int:
        if key in self.dict:
            self.counter += 1
            self.access_log[key] = self.counter
            return self.dict[key]
        return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.dict:
            self.dict[key] = value
        else:
            if len(self.dict) == self.capacity:
                old_key = min(self.access_log, key = self.access_log.get)
                self.dict.pop(old_key)
                self.access_log.pop(old_key)
 
            self.dict[key] = value
            
        self.counter += 1
        self.access_log[key] = self.counter
            

        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)