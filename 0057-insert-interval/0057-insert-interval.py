class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        newList = []
        i = 0
        while i < len(intervals):
            if intervals[i][1] < newInterval[0]:
                newList.append(intervals[i])
                i += 1
                continue
            break
        
        while i < len(intervals) and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1
        
        newList.append(newInterval)
        
        if i < len(intervals):
            newList.extend(intervals[i:])

        return newList
        

        

                

        