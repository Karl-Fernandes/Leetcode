from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        
        for word in strs:
            # Sort characters in the word to create a key
            key = ''.join(sorted(word))
            groups[key].append(word)
        
        return list(groups.values())
