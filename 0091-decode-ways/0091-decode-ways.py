class Solution:
    def numDecodings(self, s: str) -> int:
        memo = {}
        
        def dfs(i):
            if i == len(s):
                return 1  # reached end, valid decode
            if s[i] == '0':
                return 0  # no decode starts with 0
            
            if i in memo:
                return memo[i]
            
            # Decode one digit
            ways = dfs(i + 1)
            
            # Decode two digits, if valid
            if (i + 1 < len(s)) and (int(s[i:i+2]) <= 26):
                ways += dfs(i + 2)
            
            memo[i] = ways
            return ways
        
        return dfs(0)
