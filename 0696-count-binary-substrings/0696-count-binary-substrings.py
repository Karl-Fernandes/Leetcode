class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        current = 1
        prev = 0
        res = 0

        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                current += 1
            else:
                res += min(current, prev)
                prev = current
                current = 1
        res += min(current, prev)
        
        return res