class MyHashMap(object):

    def __init__(self):
        self.size = 10000
        self.table ={i: [] for i in range(self.size)}

    def calculateHashValue(self, key):
        return key % self.size
        

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        hv = self.calculateHashValue(key)


        if self.table[hv] != None:
            for idx, (existing_key, _) in enumerate(self.table[hv]):
                if existing_key == key:
                    self.table[hv][idx] = (key, value)
                    return
            self.table[hv].append((key, value))
        else:
            self.table[hv].append((key, value))
                



    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        hv = self.calculateHashValue(key)

        for element in self.table[hv]:
            if element[0] == key:
                return element[1]
        return -1
        

    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        hv = self.calculateHashValue(key)

        for idx, (existing_key, _) in enumerate(self.table[hv]):
            if existing_key == key:
                self.table[hv].pop(idx) 
                return
        




# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)