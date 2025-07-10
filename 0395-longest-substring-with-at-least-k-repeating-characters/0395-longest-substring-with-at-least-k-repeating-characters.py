class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        max_available = len(set(s))
        n = len(s)
        res = 0

        for available_char in range(1, max_available + 1):

            h = {}
            l = r = 0

            while (r < n):

                if (s[r] not in h):
                    h[s[r]] = 0
                
                h[s[r]] += 1


                if len(h) < available_char:
                    r += 1

                elif len(h) == available_char:
                    count = 0
                    for value in h.values():
                        if value >= k:
                            count += 1
                    
                    if count == available_char:
                        res = max(res, r - l + 1)
                    
                    r += 1
                        
                else:
                    while len(h) > available_char:
                        h[s[l]] -= 1
                        if h[s[l]] == 0:
                            del h[s[l]]
                        l += 1
                    
                    r += 1
        return res
 


        