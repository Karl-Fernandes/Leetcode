class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        wordDict.sort()
        memo = {}

        def dfs(substring):
            if substring in memo:
                return memo[substring]
            
            if len(substring) == 0:
                return [""]

            if len(s) < len(wordDict[0]):
                return
        
            
            local_res = []

            for word in wordDict:
                if substring[:len(word)] == word:
                    suffixes = dfs(substring[len(word):])
                    for suffix in suffixes:
                        if suffix:
                            local_res.append(word + " " + suffix)
                        else:
                            local_res.append(word)
            
            memo[substring] = local_res
            return local_res

                    

        return dfs(s)

        