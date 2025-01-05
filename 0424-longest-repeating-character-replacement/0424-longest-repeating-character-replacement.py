class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        res = 0
        l, r = 0, 0
        n = len(s)

        for r in range(n):
            if s[r] in count:
                count[s[r]] += 1
            else:
                count[s[r]] = 1
        
            window_size = r - l + 1
            highest_freq = max(count.values())
            if window_size - highest_freq <= k:
                res = max(res, window_size)
            else:
                count[s[l]] -= 1
                l += 1
            
        return res