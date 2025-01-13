class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        from itertools import zip_longest

        res = []

        for char1, char2 in zip_longest(word1, word2, fillvalue=""):
            res.append(char1)
            res.append(char2)

        return "".join(res)
