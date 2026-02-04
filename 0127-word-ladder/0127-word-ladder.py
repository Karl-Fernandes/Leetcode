class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        
        if beginWord == endWord:
            return 1
        

        graph = defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + "*" + word[i+1:]
                graph[pattern].append(word)
        

        q = deque([beginWord])
        visited = set()
        visited.add(beginWord)

        res = 1
        while q:
            for _ in range(len(q)):
                curr = q.popleft()
                if curr == endWord:
                    return res
                

                for i in range(len(curr)):
                    pattern = curr[:i] + "*" + curr[i+1:]
                    for nei in graph[pattern]:
                        if nei not in visited:
                            q.append(nei)
                            visited.add(nei)        
            res += 1
        
        return 0
        
        
