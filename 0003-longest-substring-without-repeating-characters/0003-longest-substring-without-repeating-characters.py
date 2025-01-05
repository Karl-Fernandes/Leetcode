class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        res = 0
        repeated = set()
        n = len(s)

        for r in range(n):
            while s[r] in repeated:
                repeated.remove(s[l])
                l += 1
            
            distance = r - l + 1
            res = max(res, distance)
            repeated.add(s[r])
        
        return res
        