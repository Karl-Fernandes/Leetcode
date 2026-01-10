class Solution:
    def reverse(self, x: int) -> int:
        res = 0
        isMinus = False

        if x < 0:
            isMinus = True
            x *= -1
        
        while x > 0:
            digit = x % 10
            res = res * 10 + digit
            x //= 10
        
        res = -res if isMinus else res
        if res < -2**31 or res > 2**31 - 1:
            return 0
        return res