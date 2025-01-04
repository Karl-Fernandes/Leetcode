class Solution:
    def countKConstraintSubstrings(self, s: str, k: int) -> int:
        n = len(s)
        count = { '0': 0, '1': 0 }  # Dictionary to track the counts of '0's and '1's
        l = 0
        result = 0

        for r in range(n):
            # Expand the window by including the character at index r
            count[s[r]] += 1

            # Shrink the window if it violates the k-constraint
            while count['0'] > k and count['1'] > k:
                count[s[l]] -= 1
                l += 1

            # Add the number of valid substrings ending at r
            result += r - l + 1

        return result
