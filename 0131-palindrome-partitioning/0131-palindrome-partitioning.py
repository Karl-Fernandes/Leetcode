class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        curr = []

        def dfs(i):
            if i >= len(s):
                res.append(curr.copy())
                return
            
            for j in range(i, len(s)):
                if isPalindrome(s, i, j):
                    curr.append(s[i: j +1])
                    dfs(j + 1)
                    curr.pop()

        def isPalindrome(s, i, j):
            for k in range(j - i):
                if s[i + k] != s[j - k]:
                    return False
            
            return True
        
        dfs(0)
        return res
        