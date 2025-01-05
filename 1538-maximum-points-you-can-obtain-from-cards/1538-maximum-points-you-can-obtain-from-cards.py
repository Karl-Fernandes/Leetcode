class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        total_pts = sum(cardPoints)
        
        window_size = n - k
        current_window_sum = sum(cardPoints[:window_size])
        min_window_sum = current_window_sum

        for i in range(window_size, n):
            current_window_sum += cardPoints[i] - cardPoints[i - window_size]
            min_window_sum = min(min_window_sum, current_window_sum)

        return total_pts - min_window_sum
        