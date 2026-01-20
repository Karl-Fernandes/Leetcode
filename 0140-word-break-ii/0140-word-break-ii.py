class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        wordDict.sort()
        res = []

        def dfs(substring, curr):
            if len(s) < len(wordDict[0]):
                return
            
            if len(substring) == 0:
                res.append(curr)
                return            
            
            for word in wordDict:
                if substring[:len(word)] == word:
                    if not curr:
                        dfs(substring[len(word):], word)
                    else:
                        dfs(substring[len(word):], curr + " " + word)

        dfs(s, "")
        return res

        