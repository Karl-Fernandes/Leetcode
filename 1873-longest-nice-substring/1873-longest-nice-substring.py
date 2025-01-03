class Solution:
    def isNice(self, l: int, r: int, s: str) -> bool:
        seen_lower = set()
        seen_upper = set()
        
        for i in range(l, r + 1):
            char = s[i]
            if char.islower():
                seen_lower.add(char)
            elif char.isupper():
                seen_upper.add(char.lower())
    
  
        return seen_lower == seen_upper


    def longestNiceSubstring(self, s: str) -> str:
        res = ""

        for l in range(len(s)):
            for r in range(l, len(s)):
                if self.isNice(l, r ,s):
                    if r - l + 1 > len(res):
                        res = s[l: r + 1]
                
        return res
                    




        