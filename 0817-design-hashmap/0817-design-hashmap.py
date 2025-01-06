class MyHashMap(object):

    def __init__(self):
        self.size = 10000
        self.table = {i: {} for i in range(self.size)}

    def calculateHashValue(self, key):
        return key % self.size

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        hv = self.calculateHashValue(key)
        self.table[hv][key] = value

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        hv = self.calculateHashValue(key)
        if key in self.table[hv]:
            return self.table[hv][key]
        return -1  

    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        hv = self.calculateHashValue(key)
        if key in self.table[hv]:
            del self.table[hv][key]
