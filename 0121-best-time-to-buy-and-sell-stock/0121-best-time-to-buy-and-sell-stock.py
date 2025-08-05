class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minimum = prices[0]
        res = 0

        for price in prices:
            if price < minimum:
                minimum = price
            else:
                profit = price - minimum
                res = max(profit, res)
        
        return res
            
        