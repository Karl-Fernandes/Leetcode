class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:

        res = ""

        for index in range(max(len(word1), len(word2))):
            if index < len(word1) and index < len(word2):
                res += word1[index] + word2[index]
            elif index >= len(word2):
                res += word1[index::]
                break
            else:
                res += word2[index::]
                break
        
        return res

        