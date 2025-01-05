class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        res = 0
        index_map = {}  # Dictionary to store the last index of each character

        for r in range(len(s)):
            if s[r] in index_map and index_map[s[r]] >= l:
                # Move `l` to the right of the last occurrence of s[r]
                l = index_map[s[r]] + 1
            
            # Update the most recent index of s[r]
            index_map[s[r]] = r

            # Update the result with the length of the current window
            res = max(res, r - l + 1)
        
        return res
