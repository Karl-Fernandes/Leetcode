class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda f: f[1])
        A, lastf = [], float('-inf')

        for i in range(len(intervals)):
            if intervals[i][0] >= lastf:
                A.append(intervals[i])
                lastf = intervals[i][1]
        
        return (len(intervals) - len(A))
        