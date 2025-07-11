class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        total = 0
        res = []

        for num in range(k):
            total += abs(arr[num] - x)
            res.append(arr[num])

        for r in range(k, len(arr)):
            l = r - k
            previous_total = total
            total += abs(arr[r] - x) - abs(arr[l] - x)
            if total < previous_total:
                res.remove(arr[l])
                res.append(arr[r])
        
        return res
            


        