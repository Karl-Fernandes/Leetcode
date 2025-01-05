class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        n = len(blocks)
        white_count = sum(1 for i in range(k) if blocks[i] == 'W')
        
        min_recolors = white_count
        for l in range(n - k):
            r = l + k
            
            if blocks[r] == 'W':
                white_count += 1
            if blocks[l] == 'W':
                white_count -= 1
            min_recolors = min(min_recolors, white_count)
        
        return min_recolors
