class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        visited = {letter: 0 for letter in string.ascii_lowercase}
        pattern = {letter: 0 for letter in string.ascii_lowercase}  
        total = []
        n = len(p)


        if len(p) > len(s):
            return []

        for r in range(len(p)): 
            visited[s[r]] += 1
            pattern[p[r]] += 1
        
        if visited == pattern:
            total.append(0)
        
        for r in range(n, len(s)):
            l = r - n
            visited[s[l]] -= 1
            visited[s[r]] += 1

            if visited == pattern:
                total.append(l + 1)
        
        return total
