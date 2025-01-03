class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        characters = {}
        l = 0
        res = 0
        distance = 0
        for r in range(len(s)):
            if s[r] in characters:
                characters[s[r]] += 1
            else:
                characters[s[r]] = 1
            while characters[s[r]] > 2:
                characters[s[l]] -= 1
                l += 1
            distance = r - l + 1
            res = max(res, distance)
        return res
                


        