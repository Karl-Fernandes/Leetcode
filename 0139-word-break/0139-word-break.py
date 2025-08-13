class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        word_set = set(wordDict)
        max_len = max(len(word) for word in wordDict)
        
        n = len(s)
        dp = [False] * (n + 1)
        dp[n] = True
        
        for i in range(n - 1, -1, -1):
            # Check from shortest to longest for better average case
            for length in range(1, min(max_len + 1, n - i + 1)):
                if s[i:i + length] in word_set and dp[i + length]:
                    dp[i] = True
                    break
        
        return dp[0]