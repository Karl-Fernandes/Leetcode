from collections import defaultdict
from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Map each course to its prerequisites
        preMap = defaultdict(list)
        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        visiting = set()   # nodes in current DFS path
        visited = set()    # nodes fully processed

        def dfs(crs):
            # Cycle detected
            if crs in visiting:
                return False
            # Already processed this course, no cycle found here
            if crs in visited:
                return True

            visiting.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre):
                    return False
            visiting.remove(crs)
            visited.add(crs)

            return True

        for c in range(numCourses):
            if not dfs(c):
                return False

        return True
