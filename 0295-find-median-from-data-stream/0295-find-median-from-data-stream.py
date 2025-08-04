class MedianFinder:

    def __init__(self):

        self.small = [] # maintain a heap for the smaller half
        self.large = [] # maintain a heap for the larger half
        

    def addNum(self, num: int) -> None:
        heapq.heappush(self.small, -num)

        if self.large and (-self.small[0] > self.large[0]):
            val = -heapq.heappop(self.small)   
            heapq.heappush(self.large, val)

        # Maintain the balance
        if len(self.small) > len(self.large) + 1:
            val = -heapq.heappop(self.small)   
            heapq.heappush(self.large, val)
        elif len(self.large) > len(self.small):
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -val)

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return -self.small[0]
        else:
            total = -self.small[0] + self.large[0]
            return total / 2

        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()