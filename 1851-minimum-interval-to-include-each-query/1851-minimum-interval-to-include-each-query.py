class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort(key = lambda x: x[0])
        min_heap = []
        res = [-1] * len(queries)
        queries = sorted(enumerate(queries), key=lambda x: x[1])

        print(queries)

        pointer = 0
        for query in queries:
            while pointer < len(intervals) and intervals[pointer][0] <= query[1]:
                heapq.heappush(min_heap, (intervals[pointer][1] - intervals[pointer][0] + 1, intervals[pointer][1]))
                pointer += 1
            
            while min_heap and min_heap[0][1] < query[1]:
                heapq.heappop(min_heap)

            if min_heap:
                res[query[0]] = min_heap[0][0]

        return res 


                        
        
        


            
        