class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        n = len(s)
        l = 0
        res = 0
        count = set()

        for r in range(n):
            while s[r] in count:
                count.remove(s[l])
                l += 1

            count.add(s[r])

            if r - l + 1 == 3:
                res += 1
                count.remove(s[l])
                l += 1

        return res
