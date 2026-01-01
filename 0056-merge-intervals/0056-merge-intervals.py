class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x: x[0])
        newList = [intervals[0]]

        for i in range(1, len(intervals)):
            if intervals[i][0] <= newList[-1][1]:
                newList[-1][0] = min(intervals[i][0], newList[-1][0])
                newList[-1][1] = max(intervals[i][1], newList[-1][1])
            else:
                newList.append(intervals[i])

        return newList 
        