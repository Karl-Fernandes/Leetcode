import heapq

class MedianFinder:
    def __init__(self):
        # small = max-heap (store as negatives), large = min-heap
        self.small = []  # max-heap (negatives)
        self.large = []  # min-heap

    def addNum(self, num: int) -> None:
        # Step 1: Push to max-heap first (as negative)
        heapq.heappush(self.small, -num)

        # Step 2: Balance: ensure every element in small <= every element in large
        if self.large and (-self.small[0] > self.large[0]):
            val = -heapq.heappop(self.small)
            heapq.heappush(self.large, val)

        # Step 3: Keep sizes balanced (small can only be 1 element larger than large)
        if len(self.small) > len(self.large) + 1:
            val = -heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        elif len(self.large) > len(self.small):
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -val)

    def findMedian(self) -> float:
        # If odd, median is root of the max-heap
        if len(self.small) > len(self.large):
            return -self.small[0]
        # If even, median is average of max-heap root and min-heap root
        return (-self.small[0] + self.large[0]) / 2
