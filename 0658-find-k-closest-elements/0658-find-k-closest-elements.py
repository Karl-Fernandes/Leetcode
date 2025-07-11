class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        n = len(arr)
        min_total = float('inf')
        start_index = 0

        for i in range(n - k + 1):
            total = 0
            for j in range(i, i + k):
                total += abs(arr[j] - x)

            if total < min_total:
                min_total = total
                start_index = i

        return arr[start_index:start_index + k]
