class Solution:
    def countSubstrings(self, s: str) -> int:
        if not s:
            return 0

        def expand_around_center(s: str, left: int, right: int) -> int:
            count = 0
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
                count += 1
            return count

        total = 0

        for i in range(len(s)):
            total += expand_around_center(s, i, i)
            total += expand_around_center(s, i, i + 1)

           
        return total