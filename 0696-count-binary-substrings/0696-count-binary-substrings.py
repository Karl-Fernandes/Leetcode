class Solution:
    def countBinarySubstrings(self, s: str) -> int:

        def partitionMiddle(l, r, c):
            while l >= 0 and r < len(s) and s[l] == s[l + 1] and s[r] == s[r - 1]:
                r += 1
                l -= 1
                c += 1
            return c
                    


        total = 0
        for i in range(len(s) - 1):
            if s[i] != s[i + 1]:
                total += partitionMiddle(i - 1, i + 2, 1)
        
        return total