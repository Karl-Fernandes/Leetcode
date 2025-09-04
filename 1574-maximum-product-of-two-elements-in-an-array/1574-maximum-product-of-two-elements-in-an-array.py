class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max1, max2 = 0, 0

        for n in nums:
            if n > max2:
                max1, max2 = max2, n
            elif n > max1:
                max1 = n
        
        return (max1 - 1) * (max2 - 1)
        

        