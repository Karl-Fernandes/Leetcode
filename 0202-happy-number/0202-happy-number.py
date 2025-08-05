class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while n != 1:
            if n in seen:
                return False
            seen.add(n)
            next_n = 0
            while n:
                next_n += (n % 10) ** 2
                n //= 10
            n = next_n
        return True