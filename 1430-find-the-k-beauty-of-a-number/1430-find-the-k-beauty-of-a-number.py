class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        num_str = str(num)
        n = len(num_str)
        res = 0

        for l in range(n - k + 1):
            substring = num_str[l:l + k]
            divisor = int(substring)
            if divisor != 0 and num % divisor == 0:
                res += 1

        return res
