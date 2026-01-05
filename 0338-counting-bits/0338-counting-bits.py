class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []
        for num in range(n + 1):
            current_sum = 0
            for i in range(32):
                if num & (1 << i):
                    current_sum += 1
            
            res.append(current_sum)
        
        return res

        
        