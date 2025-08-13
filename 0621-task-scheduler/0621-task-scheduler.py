class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        maxHeap = [-c for c in count.values()]
        heapq.heapify(maxHeap)

        cache = deque()
        time = 0

        while maxHeap or cache:
            time += 1

            if maxHeap:
                count = heapq.heappop(maxHeap) + 1
                if count:
                    cache.append([count, time + n])
                
            if cache and cache[0][1] == time:
                value = cache.popleft()
                heapq.heappush(maxHeap, value[0])
        
        return time
                

