class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:

        n = min(len(word1), len(word2))
        res = ""

        for index in range(n):
            res += word1[index] + word2[index]
        
        if len(word1) > len(word2):
            res += word1[n:]
        else:
            res += word2[n:]
        
        return res

        