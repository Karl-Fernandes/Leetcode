from collections import deque
from typing import List

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output = []
        q = deque()  

        for i in range(len(nums)):
            if q and q[0] <= i - k:
                q.popleft()

            while q and nums[q[-1]] < nums[i]:
                q.pop()

            q.append(i)

            if i >= k - 1:
                output.append(nums[q[0]])

        return output
