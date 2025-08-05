from typing import List

class Solution:
    def maximizeGreatness(self, A):
        A.sort()
        res = 0
        for a in A:
            if a > A[res]:
                res += 1
        return res
