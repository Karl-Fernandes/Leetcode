class MyHashSet(object):

    def __init__(self):
        self.size = 1000
        self.table = [None] * self.size

    
    def calculateHashValue(self, key):
        return key % self.size
        

    def add(self, key):
        """
        :type key: int
        :rtype: None
        """
        hv = self.calculateHashValue(key)

        if self.table[hv] == None:
            self.table[hv] = [key]
        else:
            self.table[hv].append(key)
        

    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        hv = self.calculateHashValue(key)
        if self.table[hv] != None:
            while key in self.table[hv]:
                self.table[hv].remove(key)            
        
        
    def contains(self, key):
        """
        :type key: int
        :rtype: bool
        """
        hv = self.calculateHashValue(key)
        if self.table[hv] != None:
            if key in self.table[hv]:
                return True
        return False

        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)