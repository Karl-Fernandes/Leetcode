class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        visited = defaultdict(list)



        for word in strs:
            current = [0] * 26
            
            for char in word:
                current[ord(char) - ord('a')] += 1

            key = tuple(current)
            visited[key].append(word)
        
        return list(visited.values())
            


            
            



                