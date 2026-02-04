class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        memo = {}
        res = []

        def dfs(curr):
            if curr in memo:
                return memo[curr]
            
            if len(curr) == 0:
                return [""]
            
            local_res = []

            for word in wordDict:
                if curr[:len(word)] == word:
                    suffixes = dfs(curr[len(word):])
                    for suffix in suffixes:
                        if suffix:
                            local_res.append(word + " " + suffix)
                        else:
                            local_res.append(word)
            memo[curr] = local_res
            return local_res
        

        return dfs(s)

            
